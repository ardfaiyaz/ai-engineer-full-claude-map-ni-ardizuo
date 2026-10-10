# 📝 Obsidian (optional)


Use Obsidian to view the **empty local vault templates** created by this repository. Personal vault notes are never included.


## 📥 Windows PowerShell


```powershell
winget install --id Obsidian.Obsidian --exact --source winget
```

Then launch Obsidian and choose **Open folder as vault**, selecting `Documents\Claude-Dev-Vault` (or the separate vault path you approved).


## ⌨️ Bash alternative


On macOS with Homebrew:

```bash
brew install --cask obsidian
```


## ✅ Verify the template directory


From your cloned Ardizuo repository:

```powershell
Test-Path (Join-Path $HOME 'Documents\Claude-Dev-Vault')
```

Obsidian may not expose a CLI command on `PATH`; check the graphical application. Do not point a public demo at a private vault.

[Vault guide](../../vault/README.md) · [Full installer](./full-setup.md)
