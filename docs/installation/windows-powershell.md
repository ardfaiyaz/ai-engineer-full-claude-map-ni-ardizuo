# <img src="../assets/lucide/terminal.svg" width="18" height="18" alt="" /> Windows & PowerShell

**Why you might need it:** Windows PowerShell 5.1 is sufficient for the bootstrap scripts. Windows 10/11 is the supported v1 target.

<br />

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> 1. Get it from the official source

[Windows & PowerShell — official installation page](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows)

Use the built-in **Windows PowerShell** or Windows Terminal. No administrator terminal is needed for a user-scoped installation.

```powershell
$PSVersionTable.PSVersion
$HOME
Get-Command winget -ErrorAction SilentlyContinue
```

If you want current PowerShell 7, follow Microsoft's official installer, but **do not replace** Windows PowerShell 5.1 or change execution policy system-wide for this repo.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 2. Verify

```powershell
$PSVersionTable.PSVersion
[Environment]::OSVersion.VersionString
```

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. If something goes wrong

Scripts blocked? Review the script first and run it with a **process-only** policy if your environment permits it. Do not set permanent unrestricted policy. [Microsoft execution policy reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
