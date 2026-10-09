// Stop: once per session, after enough tracked edits, suggest /log-to-vault to the user.
// Never blocks: it only ever emits a user-facing systemMessage.
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { STAGING_DIR, emit, run, safeSessionId } from "./lib/common.mjs";

const MIN_FILES = 3;

await run(async (input) => {
  const sid = safeSessionId(input.session_id);
  if (!sid) return;
  const log = path.join(STAGING_DIR, `${sid}.jsonl`);
  const marker = path.join(STAGING_DIR, `${sid}.nudged`);
  if (!existsSync(log) || existsSync(marker)) return;

  const files = new Set();
  for (const line of readFileSync(log, "utf8").split("\n")) {
    try {
      if (line) files.add(JSON.parse(line).file);
    } catch {}
  }
  if (files.size < MIN_FILES) return;

  writeFileSync(marker, new Date().toISOString());
  emit({
    systemMessage: `${files.size} files changed this session. Run /log-to-vault to review and save a session note to your knowledge vault.`,
  });
});
