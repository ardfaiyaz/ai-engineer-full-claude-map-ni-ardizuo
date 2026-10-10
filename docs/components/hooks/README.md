# 🪝 Claude Code hooks


Five existing Ardizuo hook handlers are included as `.mjs` files. **Installing a hook file is not the same as registering or executing it.** This page replaces five repetitive hook help pages; no hook code was removed.


## 📋 Included lifecycle handlers


| Event | Script | Purpose |
| --- | --- | --- |
| `SessionStart` | `vault-session-init.mjs` | Opens or resumes an approved local vault session. |
| `UserPromptSubmit` | `skill-gate-check.mjs` | Applies the configured skill gate before a request. |
| `PostToolUse` | `log-to-vault.mjs` | Tracks approved file changes for vault logging. |
| `PostToolUse` | `dead-code-check.mjs` | Flags potential dead code after supported edits. |
| `Stop` | `stop-vault-log.mjs` | Finalizes or queues an approved session summary. |


## 📥 Install and register


Run in **PowerShell** from the repository root:

```powershell
.\scripts\install-all.ps1 -Hooks              # Preview local assets and hook registration
.\scripts\install-all.ps1 -Apply -Hooks       # Copy missing files and register five hooks
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
```

Existing `settings.json` hooks are preserved. On a conflict, the installer stops rather than overwriting another handler. Hook event execution must be checked in a real Claude Code session using `/hooks`.


## 🛡️ Privacy and troubleshooting


A vault-related hook must not publish project secrets. Keep private notes outside GitHub. If a hook is registered but does not run, check `/hooks`, restart Claude Code, and inspect its own script under `ardizuo-plugin/hooks/`.

[Component catalog](../README.md) · [Hook registration instructions](../../installation/ardizuo-development-pack.md)
