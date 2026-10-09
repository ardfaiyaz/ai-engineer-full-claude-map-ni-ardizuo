# 🗂️ Windows Subsystem for Linux (WSL)

**Why you might need it:** Optional Linux environment for tools that do not support Windows directly.

<br />

## 📁 1. Get it from the official source

[Windows Subsystem for Linux (WSL) — official installation page](https://learn.microsoft.com/en-us/windows/wsl/install)

Only install WSL when a particular integration requires it. Microsoft's installer (may require elevated PowerShell and a reboot):

```powershell
wsl --install
```

Follow Microsoft's instructions for selecting a distribution and creating a Linux user. For this repository's **Windows-first bootstrap**, WSL is not required.

<br />

## ☑️ 2. Verify

```powershell
wsl --status
wsl --list --verbose
```

<br />

## 📄 3. If something goes wrong

If WSL doesn't start, check virtualization, Windows feature requirements and the official [WSL troubleshooting guide](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
