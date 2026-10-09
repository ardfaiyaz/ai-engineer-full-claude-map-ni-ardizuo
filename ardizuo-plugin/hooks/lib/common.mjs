// Shared helpers for the global Claude Code hooks in ~/.claude/hooks.
// Every hook must fail open: errors are swallowed and the process exits 0.
import { existsSync, statSync } from "node:fs";
import os from "node:os";
import path from "node:path";

export const CLAUDE_DIR = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
export const VAULT_DIR =
  process.env.CLAUDE_DEV_VAULT || path.join(os.homedir(), "Documents", "Claude-Dev-Vault");
export const STAGING_DIR = path.join(CLAUDE_DIR, "state", "vault-staging");

export async function readInput() {
  try {
    const chunks = [];
    for await (const chunk of process.stdin) chunks.push(chunk);
    const raw = Buffer.concat(chunks).toString("utf8").trim();
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function emit(obj) {
  process.stdout.write(JSON.stringify(obj));
}

// Runs a hook body and always exits 0 so a hook bug can never block Claude Code.
export async function run(fn) {
  try {
    await fn(await readInput());
  } catch (err) {
    if (process.env.CLAUDE_HOOK_DEBUG) process.stderr.write(`[hook] ${err?.stack || err}\n`);
  }
  process.exit(0);
}

// Session ids become file names, so allow only a safe character set.
export function safeSessionId(id) {
  return typeof id === "string" && /^[A-Za-z0-9_-]{1,128}$/.test(id) ? id : null;
}

function sanitizeName(name) {
  return (name || "unknown").replace(/[^A-Za-z0-9._-]+/g, "-").replace(/^-+|-+$/g, "") || "unknown";
}

// Finds the project root by walking up to the nearest .git (file or dir); no git spawn.
export function projectInfo(cwd) {
  const start = path.resolve(cwd || process.cwd());
  let dir = start;
  while (true) {
    if (existsSync(path.join(dir, ".git"))) return { root: dir, name: sanitizeName(path.basename(dir)) };
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return { root: start, name: sanitizeName(path.basename(start)) };
}

// Project-relative path; files outside the project are reduced to their basename
// so absolute home paths never reach the staging log.
export function relativeToProject(root, file) {
  const rel = path.relative(root, path.resolve(root, file));
  if (!rel || rel.startsWith("..") || path.isAbsolute(rel)) return `<outside-project>/${path.basename(file)}`;
  return rel.split(path.sep).join("/");
}

const SENSITIVE =
  /(^|[\\/])(\.env[^\\/]*|id_[^\\/]*|[^\\/]*\.(pem|key|p12|pfx|keystore|jks)|[^\\/]*(credential|secret|password)[^\\/]*|\.npmrc|\.pypirc|\.netrc)$/i;

export function isSensitivePath(file) {
  return SENSITIVE.test(file || "");
}

export function isDir(p) {
  try {
    return statSync(p).isDirectory();
  } catch {
    return false;
  }
}
