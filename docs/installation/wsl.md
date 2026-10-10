# 🐧 WSL (optional)


WSL provides a Linux shell on Windows. **The Ardizuo `.ps1` installer itself remains Windows PowerShell-first.** You do not need WSL for the main setup.


## 📥 Windows PowerShell (administrator only if required)


```powershell
wsl --install
```

You may need a reboot and to create a Linux user. Then verify:

```powershell
wsl --status
wsl --list --verbose
```


## ⌨️ After opening Ubuntu Bash in WSL


```bash
sudo apt update
sudo apt install -y git python3 python3-venv
```

Do not run the Windows-only `.\scripts\install-all.ps1` as a Bash command. See [Microsoft WSL guidance](https://learn.microsoft.com/en-us/windows/wsl/install).

[Installation index](./README.md)
