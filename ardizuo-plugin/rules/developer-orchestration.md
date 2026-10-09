# <img src="../assets/lucide/workflow.svg" width="18" height="18" alt="" /> Global Development Orchestration

These rules apply across all local repositories.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Task Selection

For significant development tasks, consult the task mappings in:

${CLAUDE_CONFIG_DIR}/workflows/skill-gates.json (or ~/.claude/workflows/skill-gates.json)

The mappings are advisory. Read the file when relevant, not for every trivial request.

Select only the relevant existing skills, agents and tools.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Parallel Work

For complex tasks involving independent work, consult:

${CLAUDE_CONFIG_DIR}/workflows/wave-protocol.md (or ~/.claude/workflows/wave-protocol.md)

Use Superpowers or SuperClaude orchestration where appropriate.
Avoid multiple agents editing the same files.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Completion

Follow these principles before declaring substantial work complete:

- Verify requirements and implementation correctness.
- Review security and maintainability where relevant.
- Run appropriate available checks.
- Report actual verification results.
- Disclose unresolved issues.

For detailed quality requirements, consult:

${CLAUDE_CONFIG_DIR}/workflows/completion-mandate.md (or ~/.claude/workflows/completion-mandate.md)

## <img src="../assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Safety

- Preserve project-specific architecture and instructions.
- Do not execute unnecessary tools.
- Require approval before destructive or external actions.
- Do not configure or perform social media automation.
