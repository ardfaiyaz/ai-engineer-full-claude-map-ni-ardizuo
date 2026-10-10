# 🌿 Git


Git is required to clone the repository and review changes.


## 📥 Windows PowerShell


```powershell
winget install --id Git.Git --exact --source winget
```

Reopen PowerShell and verify:

```powershell
git --version
```

Only if you plan to commit changes, set your **own** identity:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```


## ⌨️ Bash alternative


macOS with Homebrew:

```bash
brew install git
git --version
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y git
git --version
```


## 🛠️ Troubleshooting


Reopen your terminal if Git isn't on `PATH`. Before committing, use `git status` and `git diff --check`. Official source: [git-scm.com](https://git-scm.com/install/windows).

[Installation index](./README.md)
