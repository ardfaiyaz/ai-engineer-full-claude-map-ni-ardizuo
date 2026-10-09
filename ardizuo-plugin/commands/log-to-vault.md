---
description: Draft a sanitized development session note and save it to the knowledge vault only after explicit user approval
argument-hint: "[optional title or focus]"
---

Draft a development session note for the knowledge vault. Nothing may be written to the vault until the user approves the exact draft.

Optional title or focus from the user: $ARGUMENTS

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 1. Gather

- Project name: the basename of the git root containing the current working directory (or the working directory's basename if there is no git repo). Replace characters outside `A-Za-z0-9._-` with `-`.
- File-change metadata: in `${CLAUDE_CONFIG_DIR}/state/vault-staging/` (or `~/.claude/state/vault-staging/` when unset), read the most recently modified `*.jsonl` whose entries have `"project"` equal to this project name. Each line has `ts`, `tool`, `project`, `file`. If none exists, rely on your own knowledge of this session.
- Your own understanding of what was done, decided and verified in this session.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 2. Draft

Use this structure, under 60 lines:

```markdown
---
date: YYYY-MM-DD
project: <project>
tags: [session]
---

# <concise title>

## Summary
## Changes
## Decisions
## Verification
## Open issues
## Next steps
```

Keep `## Next steps` accurate: the SessionStart hook surfaces it in the next session for this project.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. Sanitize (mandatory)

The note must not contain:
- raw prompts, conversation transcripts, or tool output dumps
- secrets of any kind: API keys, tokens, passwords, connection strings, private keys, `.env` values, or anything matching patterns like `sk-`, `ghp_`, `eyJ`, `AKIA`, `-----BEGIN`
- personal data: names of private individuals, emails, phone numbers, addresses, customer or user records
- absolute paths under the user's home directory (use project-relative paths)
- code blocks longer than 10 lines

Re-read the draft against this list and remove anything that violates it.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 4. Approval (mandatory)

Show the complete draft and the target path inside the configured vault: `${CLAUDE_DEV_VAULT}/Sessions/<project>/YYYY-MM-DD-<slug>.md`, or if `CLAUDE_DEV_VAULT` is unset, `$HOME/Documents/Claude-Dev-Vault/Sessions/<project>/YYYY-MM-DD-<slug>.md`. Resolve the actual directory for this user at runtime; never use the author's Windows username. Then ask the user directly (use a supported interactive prompt if available): **Save as shown** / **Revise first** / **Don't save**.

- **Save as shown**: only after an explicit affirmative reply, write the approved file with an available file-writing tool. Never overwrite: if the name exists, add `-2`, `-3`, … Report the saved path.
- **Revise first**: apply the user's changes, show the new draft, and ask again.
- **Don't save**: write nothing and say so.

Do not modify repository code, the staging files, or any other vault note as part of this command.
