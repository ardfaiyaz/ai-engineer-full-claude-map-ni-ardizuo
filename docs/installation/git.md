# <img src="../assets/lucide/git-branch.svg" width="18" height="18" alt="" /> Git for Windows

**Why you might need it:** Clones repositories, tracks changes, enables worktrees and helps Claude inspect diffs.

<br />

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> 1. Get it from the official source

[Git for Windows — official installation page](https://git-scm.com/install/windows)

**Recommended:** download Git for Windows from the official site, accept the default options, then reopen PowerShell. If you prefer Windows Package Manager:

```powershell
winget install --id Git.Git -e --source winget
```

For your first commit only, configure your own identity:

```powershell
git config --global user.name "Your display name"
git config --global user.email "you@example.com"
```

Use your real preferred identity; these are examples.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 2. Verify

```powershell
git --version
git config --global --get user.name
```

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. If something goes wrong

If Git is not found after installation, close and reopen the terminal. If the repository is public, check changes with `git status` and `git diff` before committing.



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
