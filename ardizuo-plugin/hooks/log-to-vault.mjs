// PostToolUse (async): record file-change metadata for the current session in a local staging
// file. Never writes to the vault and never records file contents, prompts or responses.
import { appendFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { STAGING_DIR, isSensitivePath, projectInfo, relativeToProject, run, safeSessionId } from "./lib/common.mjs";

await run(async (input) => {
  const sid = safeSessionId(input.session_id);
  const file = input.tool_input?.file_path || input.tool_input?.notebook_path;
  if (!sid || typeof file !== "string" || isSensitivePath(file)) return;

  const { root, name } = projectInfo(input.cwd);
  const entry = {
    ts: new Date().toISOString(),
    tool: String(input.tool_name || ""),
    project: name,
    file: relativeToProject(root, file),
  };
  mkdirSync(STAGING_DIR, { recursive: true });
  appendFileSync(path.join(STAGING_DIR, `${sid}.jsonl`), JSON.stringify(entry) + "\n");
});
