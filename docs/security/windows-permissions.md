# 🛡️ Windows permissions and safe installation


**Default to normal user permissions.** You do not need Administrator PowerShell just to add user-scope Claude rules, plugins or many MCP entries.


<br />
<br />


## 🛡️ Safe defaults


- Use `$HOME` and respect `$env:CLAUDE_CONFIG_DIR`; don't hardcode `C:\Users\Someone`.
- Preview installer changes before using `-Apply`.
- Back up only files the installer is going to modify.
- Never disable antivirus, firewall, account protection or execution policy globally as a convenience.
- For MCPs, grant access only to the required repos, directories, projects or test data.
- For repository actions, keep review, push and deploy permissions separate from read-only checks.


<br />
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

The extended stack needs no administrator rights either. `claude plugin install` and `claude mcp add --scope user` write only to your own user profile. Global npm tools (`npm.cmd install -g`) install under your user's npm prefix by default; if npm asks for elevation, fix the npm prefix rather than running PowerShell as Administrator. Preview first:

```powershell
python .\scripts\install-extensions.py --select all   # dry run, no changes
```

`winget install stacklok.thv` (ToolHive) may show a Windows elevation prompt if the package installs per machine. Declining it skips only ToolHive.


[API key safety](./api-keys-and-powershell.md) · [Security policy](../../SECURITY.md) · [Docs hub](../README.md)
