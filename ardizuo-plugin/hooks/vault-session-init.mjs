// SessionStart (startup|resume): surface the latest approved session note for this project
// without deleting staging files. Read-only on the vault.
import { readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";
import { STAGING_DIR, VAULT_DIR, emit, isDir, projectInfo, run } from "./lib/common.mjs";

const MAX_CHARS = 1200;



function section(text, heading) {
  const match = text.match(new RegExp(`^##\\s+${heading}\\s*$([\\s\\S]*?)(?=^##\\s|(?![\\s\\S]))`, "im"));
  return match ? match[1].trim() : "";
}

await run(async (input) => {
  if (!isDir(VAULT_DIR)) return;

  const { name } = projectInfo(input.cwd);
  const notesDir = path.join(VAULT_DIR, "Sessions", name);
  if (!isDir(notesDir)) return;

  const latest = readdirSync(notesDir).filter((f) => f.endsWith(".md")).sort().pop();
  if (!latest) return;

  const text = readFileSync(path.join(notesDir, latest), "utf8");
  const title = (text.match(/^#\s+(.+)$/m) || [])[1] || latest;
  const next = section(text, "Next steps");
  let context = `vault-session-init: latest session note for project "${name}" is Sessions/${name}/${latest} — "${title}".`;
  if (next) context += `\nNext steps recorded there:\n${next}`;
  context += "\nSession notes are saved only via /log-to-vault with the user's approval.";
  if (context.length > MAX_CHARS) context = context.slice(0, MAX_CHARS - 3) + "...";

  emit({ hookSpecificOutput: { hookEventName: "SessionStart", additionalContext: context } });
});
