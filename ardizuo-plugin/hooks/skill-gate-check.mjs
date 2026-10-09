// UserPromptSubmit: one-line workflow reminder, only for prompts that look like development work.
// Superpowers already injects skill guidance at SessionStart, so this stays conditional and short.
import { emit, run } from "./lib/common.mjs";

const DEV_WORK =
  /\b(implement|build|create|add|fix|refactor|migrate|debug|optimi[sz]e|feature|bug|component|endpoint|api|schema|integrate|upgrade|rewrite|hook|deploy)\b/i;

await run(async (input) => {
  const prompt = typeof input.prompt === "string" ? input.prompt.trim() : "";
  if (prompt.length < 15 || prompt.startsWith("/") || !DEV_WORK.test(prompt)) return;
  emit({
    hookSpecificOutput: {
      hookEventName: "UserPromptSubmit",
      additionalContext:
        "skill-gate-check: development task detected. Per the global workflow, check relevant installed skills/agents first, keep changes within the requested scope, and verify (tests/lint/build) before claiming completion.",
    },
  });
});
