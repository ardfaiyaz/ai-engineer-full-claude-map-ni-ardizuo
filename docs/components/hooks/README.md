# 🪝 Claude Code hooks


Five existing Ardizuo hook handlers are included as `.mjs` files. **Installing a hook file is not the same as registering or executing it.** This page replaces five repetitive hook help pages; no hook code was removed.


<br />
<br />


## 📋 Included lifecycle handlers


| Event | Script | Purpose |
| --- | --- | --- |
| `SessionStart` | `vault-session-init.mjs` | Opens or resumes an approved local vault session. |
| `UserPromptSubmit` | `skill-gate-check.mjs` | Applies the configured skill gate before a request. |
| `PostToolUse` | `log-to-vault.mjs` | Tracks approved file changes for vault logging. |
| `PostToolUse` | `dead-code-check.mjs` | Flags potential dead code after supported edits. |
| `Stop` | `stop-vault-log.mjs` | Finalizes or queues an approved session summary. |


<br />
<br />


## 📥 Install and register


Run in **PowerShell** from the repository root:

```powershell
.\scripts\install-all.ps1 -Hooks              # Preview local assets and hook registration
.\scripts\install-all.ps1 -Apply -Hooks       # Copy missing files and register five hooks
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
```

Existing `settings.json` hooks are preserved. On a conflict, the installer stops rather than overwriting another handler. Hook event execution must be checked in a real Claude Code session using `/hooks`.


<br />
<br />


## 🧩 External guardrail systems (installed by -All, not Ardizuo hooks)


| System | Route | Note |
| --- | --- | --- |
| [Probity](https://github.com/nizos/probity) | Plugin `probity@probity`; per project `npm install -D @nizos/probity` + `probity.config.ts` | TDD and rule enforcement; rules activate only where a config exists |
| [TDD Guard](https://github.com/nizos/tdd-guard) | Plugin `tdd-guard@tdd-guard` | Predecessor of Probity; type `tdd-guard off` in a prompt if it blocks work |

Ponytail, Everything Claude Code (`hooks_enabled` defaults to true) and Claude-Mem also add their own hooks. There are still **five** Ardizuo hook handlers; the others belong to their plugins. After installing, open `/hooks`, and disable a plugin with `claude plugin disable <id>` if two hooks fight over the same event. See the [master extension catalog](../extension-catalog.md).


<br />
<br />


## 🛡️ Privacy and troubleshooting


A vault-related hook must not publish project secrets. Keep private notes outside GitHub. If a hook is registered but does not run, check `/hooks`, restart Claude Code, and inspect its own script under `ardizuo-plugin/hooks/`.

[Component catalog](../README.md) · [Hook registration instructions](../../installation/ardizuo-development-pack.md)
