# 🛡️ Windows permissions and safe installation

**Default to normal user permissions.** You do not need Administrator PowerShell just to add user-scope Claude rules, plugins or many MCP entries.

<br />

## 🛡️ Safe defaults

- Use `$HOME` and respect `$env:CLAUDE_CONFIG_DIR`; don't hardcode `C:\Users\Someone`.
- Preview installer changes before using `-Apply`.
- Back up only files the installer is going to modify.
- Never disable antivirus, firewall, account protection or execution policy globally as a convenience.
- For MCPs, grant access only to the required repos, directories, projects or test data.
- For repository actions, keep review, push and deploy permissions separate from read-only checks.

<br />

## 📄 Preflight

```powershell
$PSVersionTable.PSVersion
$HOME
Get-Command claude,git,node,npm -ErrorAction SilentlyContinue | Select-Object Name,Source
.\scripts\doctor.ps1
.\scripts\install.ps1 -Profile core # dry run
```

Use `-Apply` only after reviewing the specific destination and source files. Unexpected file collisions should stop rather than overwrite.

<br />

[API key safety](./api-keys-and-powershell.md) · [Security policy](../../SECURITY.md) · [Docs hub](../README.md)
