# 📝 Obsidian

**Why you might need it:** Optional local Markdown knowledge vault for sessions, ADRs, PRDs and reusable learning notes.

<br />

## 📁 1. Get it from the official source

[Obsidian — official installation page](https://obsidian.md/download)

Install Obsidian from the official download page, launch it and choose **Open folder as vault**. Select a new dedicated directory you control, such as `Documents\Claude-Dev-Vault`.

The public repository provides empty templates only. **Do not automatically point it at your private vault or copy existing notes into a public repo.**

<br />

## ☑️ 2. Verify

```powershell
Get-Command obsidian -ErrorAction SilentlyContinue
Test-Path (Join-Path $HOME 'Documents\Claude-Dev-Vault')
```

<br />

## 📄 3. If something goes wrong

Obsidian does not necessarily add a CLI command; if `Get-Command` finds nothing, that is not proof the desktop app is absent. Confirm in the app. Vault persistence still needs a separate approved write-and-reload test.


[Obsidian installation help](https://obsidian.md/help/install) · [vault templates](../../vault/templates/)

<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
