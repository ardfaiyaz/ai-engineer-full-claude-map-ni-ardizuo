---
name: vault-learning
description: Prepare verified software development lessons, architectural decisions and session summaries for an approved knowledge vault.
disable-model-invocation: true
---

# <img src="../../assets/lucide/notebook-pen.svg" width="18" height="18" alt="" /> Vault Learning

Vault location:
`${CLAUDE_DEV_VAULT}` when set; otherwise `$HOME/Documents/Claude-Dev-Vault`. Resolve the path at runtime.

1. Identify meaningful, verified development knowledge.
2. Separate reusable lessons from project-specific decisions.
3. Prepare concise Markdown notes with source context.
4. Exclude secrets, credentials and raw conversations.
5. Show the proposed note and destination to the user.
6. Require explicit user approval before writing.
7. Preserve previous architectural decisions.
8. Never automatically delete or overwrite vault notes.

Keep notes organized by repository.
