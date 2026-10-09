# Security policy

## Never publish personal runtime data

Keep `~/.claude.json`, `~/.claude/settings.local.json`, `.env` files, OAuth/API tokens, SSH keys, private projects, hook logs, session history, and private Obsidian vault notes out of this repository. A `.gitignore` is **not** sufficient protection if you explicitly force-add a file; inspect the staged diff before committing.

## Installation design

- Dry-run first; explicit `-Apply` required for changes.
- Resolve the actual user-scoped Claude configuration directory rather than assuming a username.
- Do not overwrite unknown existing files, run elevated commands automatically or execute unaudited remote scripts.
- Third-party MCPs/plugins need their own permission and authentication review, with least privilege by default.
- `doctor.ps1` does not prove MCP authentication or real agent execution; validate those manually.
- Restore/backups remain **outside the Git repository** and may contain private local rules. Never publish backups.

## Before the first public code release

Audit all files **and Git history** for secrets, document licenses/credits, review hooks for unauthorized side effects, and test on a clean Windows profile or VM.

Report security issues privately to the repository maintainer using GitHub's private vulnerability reporting where available; do not post credentials in public issues.
