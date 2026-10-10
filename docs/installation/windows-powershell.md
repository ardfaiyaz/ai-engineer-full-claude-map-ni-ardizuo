# 💻 Windows PowerShell


Windows 10/11 with Windows PowerShell 5.1 is the supported installation target. You **do not need an administrator terminal** for Ardizuo's user-scoped files.


## ✅ Check your shell


```powershell
$PSVersionTable.PSVersion
winget --version
```

PowerShell 7 is optional. To install it with Windows Package Manager:

```powershell
winget install --id Microsoft.PowerShell --exact --source winget
```

Do not change the system-wide execution policy to `Unrestricted`. If scripts are blocked, review them first and follow your organization's policy.


## 🛠️ If script execution is restricted


For a single *reviewed* script, a new **process-scoped** PowerShell can be used if your organization permits it:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-all.ps1 -All
```

This is a **preview** only because `-Apply` is omitted. Avoid permanent policy changes.

[Quick start](../../START-HERE.md)
