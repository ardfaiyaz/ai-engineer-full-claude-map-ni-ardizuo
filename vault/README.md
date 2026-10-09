# Obsidian developer memory

**Optional local folder, no required cloud sync.** Only the empty folder structure and generic templates are public. Your private sessions and notes never ship with this package.

<br />

## Create the eight folders

```powershell
.\scripts\install-all.ps1 -Apply -Vault
```

Creates `Sessions`, `Learnings`, `ADRs`, `PRDs`, `Dispatch-Logs`, `Diagrams`, `Projects`, and `Templates` under your Documents vault by default. To choose a different directory, pass `-VaultPath "D:\MyVault"`.

<br />

## Open and use

Install [Obsidian](../docs/installation/obsidian.md), then select **Open folder as vault** and choose the directory. Use [the sample templates](./templates/) to create ADRs, PRDs and learning notes manually.

`/log-to-vault` is an original Claude command, but it must ask before writing a note. Never authorize automatic export of private conversations, credentials, or raw source files. Test note save and reload on a disposable project before enabling hooks globally.

[Full installer](../docs/installation/full-setup.md) · [Credential safety](../docs/security/api-keys-and-powershell.md)

<br />

## A custom vault path (optional)

The hook library reads `CLAUDE_DEV_VAULT` when set. If you choose a custom vault directory, set the variable for the current PowerShell session before starting Claude Code:

```powershell
$env:CLAUDE_DEV_VAULT = 'D:\MyVault'
claude
```

This is **a path, not an API secret**. To keep this setting for future sessions, you may explicitly set a user-level Windows environment variable; see the [PowerShell guide](../docs/security/api-keys-and-powershell.md). The installer never changes it silently.


## Templates are installed without replacement

The Full installer now copies the four repository templates (`ADR.md`, `Learning.md`, `PRD.md`, `Session.md`) into the chosen vault's `Templates` directory only when no file with that name exists. Identical templates are skipped, and a customized existing template causes the template step to stop rather than overwrite your work.

```powershell
# Test first with a throwaway vault. Use --vault-path to avoid touching a personal vault.
python .\scripts\install-all.py --config-dir "$HOME\Documents\Ardizuo-Test-Config" --vault --vault-path "$HOME\Documents\Ardizuo-Test-Vault"

# Apply only after reviewing the directory and the template contents.
python .\scripts\install-all.py --apply --config-dir "$HOME\Documents\Ardizuo-Test-Config" --vault --vault-path "$HOME\Documents\Ardizuo-Test-Vault"
```

A template file does not mean a private note was written or a Claude session was saved. Keep approval checks for note creation and do not commit the resulting vault.
