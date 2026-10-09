// PostToolUse (Write|Edit|MultiEdit): read-only heuristic scan of the edited file for likely
// dead code. Findings are returned to Claude as context; this hook never modifies files.
import { readFileSync, statSync } from "node:fs";
import path from "node:path";
import { emit, projectInfo, relativeToProject, run } from "./lib/common.mjs";

const MAX_BYTES = 300 * 1024;
const MAX_FINDINGS = 10;
const JS_EXT = new Set([".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"]);
const SKIP_PATH = /[\\/](node_modules|dist|build|out|coverage|\.next|\.turbo|vendor|__generated__)[\\/]|\.min\.js$|\.d\.ts$/i;
const TEST_PATH = /\.(test|spec)\.[^.]+$|[\\/](__tests__|tests?)[\\/]/i;

const lineOf = (text, index) => text.slice(0, index).split("\n").length;
const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function unusedNames(text, imports) {
  // Usage is counted in the file with import statements blanked out.
  let body = text;
  for (const imp of imports) body = body.replace(imp.statement, " ".repeat(imp.statement.length));
  const findings = [];
  for (const imp of imports) {
    for (const name of imp.names) {
      if (!new RegExp(`(^|[^\\w$])${escapeRe(name)}($|[^\\w$])`).test(body)) {
        findings.push(`L${imp.line}: import '${name}' appears unused`);
      }
    }
  }
  return findings;
}

function jsImports(text) {
  const imports = [];
  const re = /^\s*import\s+(?!['"])([\s\S]*?)\s+from\s+['"][^'"]+['"];?/gm;
  for (const m of text.matchAll(re)) {
    const clause = m[1].replace(/^type\s+/, "");
    const names = [];
    const ns = clause.match(/\*\s+as\s+([\w$]+)/);
    if (ns) names.push(ns[1]);
    const named = clause.match(/\{([\s\S]*?)\}/);
    if (named) {
      for (const part of named[1].split(",")) {
        const p = part.trim().replace(/^type\s+/, "");
        if (p) names.push(p.split(/\s+as\s+/).pop().trim());
      }
    }
    const def = clause.replace(/\{[\s\S]*?\}/, "").replace(/\*\s+as\s+[\w$]+/, "").split(",")[0].trim();
    if (/^[\w$]+$/.test(def)) names.push(def);
    imports.push({ statement: m[0], names, line: lineOf(text, m.index + m[0].indexOf("import")) });
  }
  return imports;
}

function pyImports(text, file) {
  if (path.basename(file) === "__init__.py") return []; // imports there are usually re-exports
  const imports = [];
  const re = /^(?:from\s+([\w.]+)\s+import\s+(\([\s\S]*?\)|[^\n]+)|import\s+([^\n]+))/gm;
  for (const m of text.matchAll(re)) {
    if (m[1] === "__future__") continue;
    const list = (m[2] || m[3]).replace(/[()]/g, "").replace(/#.*$/gm, "");
    const names = [];
    for (const part of list.split(",")) {
      const p = part.trim();
      if (!p || p === "*") continue;
      const alias = p.split(/\s+as\s+/);
      names.push(alias.length > 1 ? alias[1].trim() : m[3] ? p.split(".")[0] : p);
    }
    imports.push({ statement: m[0], names, line: lineOf(text, m.index) });
  }
  return imports;
}

function commentedCode(lines, marker, codeLike) {
  const findings = [];
  let start = -1;
  let count = 0;
  const flush = () => {
    if (count >= 3) findings.push(`L${start + 1}-L${start + count}: ${count} consecutive lines of commented-out code`);
    start = -1;
    count = 0;
  };
  lines.forEach((line, i) => {
    const t = line.trim();
    if (t.startsWith(marker) && !t.startsWith("#!") && codeLike(t.slice(marker.length).trim())) {
      if (start < 0) start = i;
      count++;
    } else flush();
  });
  flush();
  return findings;
}

const jsCodeLike = (s) =>
  /(;|\{|\}|=>)\s*$/.test(s) ||
  /^(const|let|var|function|return|import|export|if|else|for|while|class|await|try|catch)\b/.test(s) ||
  /^[\w$.]+\s*(\(|=[^=])/.test(s);
const pyCodeLike = (s) =>
  /^(def|class|return|import|from|if|elif|else|for|while|try|except|with|print)\b/.test(s) ||
  /^[\w.\[\]]+\s*(\(|=[^=])/.test(s);

function scan(file, text) {
  const ext = path.extname(file).toLowerCase();
  const lines = text.split("\n");
  const findings = [];
  if (JS_EXT.has(ext)) {
    findings.push(...unusedNames(text, jsImports(text)));
    findings.push(...commentedCode(lines, "//", jsCodeLike));
    lines.forEach((l, i) => /^\s*debugger\s*;?\s*$/.test(l) && findings.push(`L${i + 1}: debugger statement`));
    if (!TEST_PATH.test(file)) {
      lines.forEach((l, i) => /\bconsole\.log\(/.test(l) && !/^\s*\/\//.test(l) && findings.push(`L${i + 1}: console.log left in non-test code`));
    }
  } else if (ext === ".py") {
    findings.push(...unusedNames(text, pyImports(text, file)));
    findings.push(...commentedCode(lines, "#", pyCodeLike));
    lines.forEach((l, i) => /^\s*(breakpoint\(\)|(i?pdb)\.set_trace\(\))/.test(l) && findings.push(`L${i + 1}: debugger breakpoint`));
  }
  return findings;
}

await run(async (input) => {
  const file = input.tool_input?.file_path;
  if (typeof file !== "string" || SKIP_PATH.test(file)) return;
  const ext = path.extname(file).toLowerCase();
  if (!JS_EXT.has(ext) && ext !== ".py") return;
  if (statSync(file).size > MAX_BYTES) return;

  const findings = scan(file, readFileSync(file, "utf8"));
  if (!findings.length) return;

  const { root } = projectInfo(input.cwd);
  const shown = findings.slice(0, MAX_FINDINGS);
  const more = findings.length > shown.length ? `\n- ...and ${findings.length - shown.length} more` : "";
  emit({
    hookSpecificOutput: {
      hookEventName: "PostToolUse",
      additionalContext:
        `dead-code-check (read-only heuristic) for ${relativeToProject(root, file)}:\n- ${shown.join("\n- ")}${more}\n` +
        "Verify each finding before acting; remove only code you introduced or that is confirmed dead, and leave unrelated code untouched.",
    },
  });
});
