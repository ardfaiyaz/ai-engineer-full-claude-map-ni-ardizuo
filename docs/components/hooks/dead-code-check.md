# <img src="../../assets/lucide/workflow.svg" width="18" height="18" alt="" /> dead-code-check hook

**Event:** `PostToolUse` · **Role:** Surfaces possible dead-code issues after edits.

<br />

## <img src="../../assets/lucide/download.svg" width="18" height="18" alt="" /> Installation

The script `ardizuo-plugin/hooks/dead-code-check.mjs` is installed by the one-package local installer. It imports the bundled `hooks/lib/common.mjs` helper.

```powershell
.\scripts\install-all.ps1            # Preview local files
.\scripts\install-all.ps1 -Apply     # Apply, after review
```

<br />

## <img src="../../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Activation (optional)

The installer **does not register hooks on file-copy alone**. To review and activate all five global hooks, run:

```powershell
node .\scripts\register-hooks.mjs          # Preview
node .\scripts\register-hooks.mjs --apply  # Back up settings, then register
```

This merges registrations without removing existing hook entries. Do not manually replace another developer's `settings.json`.

<br />

## <img src="../../assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Verification and safety

Run `node --check` on the installed `.mjs` file. Inside Claude Code, open `/hooks`, perform a safe test event, and check the result. **Treat suggestions as candidates, not proof that code is safe to remove.** A script being installed is not proof that the corresponding event has run.

<br />

## <img src="../../assets/lucide/wrench.svg" width="18" height="18" alt="" /> Troubleshooting and removal

If the hook fails, check the relative import of `./lib/common.mjs`, Node availability, `CLAUDE_CONFIG_DIR`, and write permissions. Back up `settings.json`, remove only this registered hook command and leave unrelated hook entries intact. Keep private staging data out of Git.

[All hooks](./README.md) · [Full installation](../../installation/full-setup.md)
