# 🌿 GitHub CLI (`gh`)


Optional: useful for your own GitHub login, PRs and repository maintenance; not required to clone a public repository.


<br />
<br />


## 📥 Windows PowerShell


```powershell
winget install --id GitHub.cli --exact --source winget
gh --version
gh auth login
```

Follow the browser-based sign-in. Never paste a token into this repository or a public issue.


<br />
<br />


## ⌨️ Bash alternative


macOS with Homebrew:

```bash
brew install gh
gh auth login
```


<br />
<br />


## ✅ Verify


```powershell
gh auth status
```

Do not share `gh auth token` output. [Official GitHub CLI instructions](https://cli.github.com/manual/gh_auth_login).

[Installation index](./README.md)
