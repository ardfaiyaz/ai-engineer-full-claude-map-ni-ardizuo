# <img src="../assets/lucide/git-branch.svg" width="18" height="18" alt="" /> GitHub CLI (gh)

**Why you might need it:** Offers an interactive and safer way to authenticate to GitHub for repository actions.

<br />

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> 1. Get it from the official source

[GitHub CLI (gh) — official installation page](https://cli.github.com/)

**Recommended on Windows:** official installer or Windows Package Manager:

```powershell
winget install --id GitHub.cli -e --source winget
```

Then authenticate interactively with a browser instead of pasting a personal access token into scripts:

```powershell
gh auth login
```

Choose GitHub.com and HTTPS if those match your use case.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 2. Verify

```powershell
gh --version
gh auth status
```

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. If something goes wrong

If you need to change accounts or permissions, use `gh auth login` / `gh auth refresh` and review scopes. Never print, paste, log or commit the output of `gh auth token`. See [the GitHub CLI manual](https://cli.github.com/manual/gh_auth_login).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
