# 🔄 log-to-vault hook

**Event:** `PostToolUse` · **Role:** Stages project-relative file-change metadata after approved tooling.

<br />

## 📥 Installation

The script `ardizuo-plugin/hooks/log-to-vault.mjs` is installed by the one-package local installer. It imports the bundled `hooks/lib/common.mjs` helper.

```powershell
.\scripts\install-all.ps1            # Preview local files
.\scripts\install-all.ps1 -Apply     # Apply, after review
```

<br />

## 📄 Activation (optional)

The installer **does not register hooks on file-copy alone**. To review and activate all five global hooks, run:

```powershell
node .\scripts\register-hooks.mjs          # Preview
node .\scripts\register-hooks.mjs --apply  # Back up settings, then register
```

This merges registrations without removing existing hook entries. Do not manually replace another developer's `settings.json`.

<br />

## 🛡️ Verification and safety

Run `node --check` on the installed `.mjs` file. Inside Claude Code, open `/hooks`, perform a safe test event, and check the result. **Staging is not a vault note and should not include source contents or keys.** A script being installed is not proof that the corresponding event has run.

<br />

## 🛠️ Troubleshooting and removal

If the hook fails, check the relative import of `./lib/common.mjs`, Node availability, `CLAUDE_CONFIG_DIR`, and write permissions. Back up `settings.json`, remove only this registered hook command and leave unrelated hook entries intact. Keep private staging data out of Git.

[All hooks](./README.md) · [Full installation](../../installation/full-setup.md)
