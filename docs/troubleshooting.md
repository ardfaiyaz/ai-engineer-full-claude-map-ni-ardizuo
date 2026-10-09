# Troubleshooting

Start here if a command isn't found or a plugin/MCP shows missing.

<br />

| Symptom | Check first | Next step |
| :--- | :--- | :--- |
| `claude` not found | `Get-Command claude` | Reopen PowerShell, then see [Claude CLI](./installation/claude-code.md) |
| `git` not found | `git --version` | Install [Git for Windows](./installation/git.md) |
| `node` works but `npm.ps1` is blocked | `npm.cmd --version` | Follow [Node/npm guide](./installation/nodejs-npm.md); don't disable policy globally |
| `uvx` not found | `uv --version` | Reopen terminal or consult [uv installer guide](./installation/uv.md) |
| `gh` needs sign-in | `gh auth status` | `gh auth login` in [GitHub CLI guide](./installation/github-cli.md) |
| MCP says authentication required | `claude mcp list` / `/mcp` | Sign in through [provider guide](../integrations/mcp/README.md) |
| Dashboard does not list all skills | `claude` → `/skills` | Plugin/nested scans may differ; dashboard is not authoritative |
| Obsidian vault folder exists but no saved notes | Check note folder | A folder is not proof of a successful approved write |
| `git push` reports everything up to date | `git status` | You may not have staged/committed changes; see [Git commands](./installation/git.md) |

<br />

## Windows Git line-endings

Warnings such as `LF will be replaced by CRLF` are generally informational. Run `git diff --check`; review file changes and scripts before staging. Do not change global Git settings blindly.

<br />

## A reliable Git sequence

These are **four separate lines**, not one combined command:

```powershell
git status
git add README.md docs/ integrations/ ardizuo-plugin/README.md dashboard/claude-map/README.md
git commit -m "docs: clarify setup and prerequisites"
git push origin main
```

Run `git diff --cached --check` after staging and before committing. If you added a banner, include `git add banner.png` as appropriate.

<br />

[Docs hub](./README.md) · [Security](../SECURITY.md)
