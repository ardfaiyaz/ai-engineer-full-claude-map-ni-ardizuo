# ⌨️ log-to-vault command

**Purpose:** Propose a sanitized session note and save it **only after the user explicitly approves its exact content**.

<br />

## 📥 Install

The command lives under `ardizuo-plugin/commands/log-to-vault.md` and is copied by the original development pack installer.

```powershell
.\scripts\install-all.ps1 -Apply
```

<br />

## 📝 Set up memory

Create an [Obsidian vault](../../../vault/README.md), open it as a folder, and optionally set `CLAUDE_DEV_VAULT` if it uses a nondefault directory.

In Claude Code, execute `/log-to-vault` **after genuine project work**, review the proposed note, and select either Save, Revise or Don't save. Check the actual file in Obsidian and verify it is available on a later session.

**Never record:** credentials, raw transcripts, personal identifiers, absolute home paths, proprietary code dumps, or `.env` values. If there is no substantive session work, no note is needed.

<br />

## 🛠️ Troubleshooting

If the command cannot find notes or staging metadata, check the vault directory, global command discovery, and the approved write target. File writes and session hooks are separate; none occur simply because this page exists.

[Memory docs](../../../vault/README.md) · [Security](../../../SECURITY.md)
