# 🛠️ Troubleshooting


Start here if a command isn't found or a plugin/MCP shows missing.


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
<br />


## 🌿 Windows Git line-endings


Warnings such as `LF will be replaced by CRLF` are generally informational. Run `git diff --check`; review file changes and scripts before staging. Do not change global Git settings blindly.


<br />
<br />


## 🌿 A reliable Git sequence


These are **four separate lines**, not one combined command:

```powershell
git status
git add README.md docs/ integrations/ ardizuo-plugin/README.md dashboard/claude-map/README.md
git commit -m "docs: clarify setup and prerequisites"
git push origin main
```

Run `git diff --cached --check` after staging and before committing. If you added a banner, include `git add banner.png` as appropriate.


[Docs hub](./README.md) · [Security](../SECURITY.md)


<br />
<br />


## 🛠️ One-package troubleshooting


**If the local installer reports CONFLICT:** do not force overwrite. Use a sandbox `-ConfigDir` to compare the original asset with your version. **If plugin installation fails:** check the marketplace and version inside Claude Code `/plugin`. **If MCP is configured but disconnected:** authenticate using `/mcp`; do not paste tokens into logs. **If Claude Map patch is incompatible:** the patch restores backups; use upstream dashboard until the extension is updated. [Full guide](./installation/full-setup.md).


<br />
<br />


## 🧩 A required plugin is missing after the one-command installer


First run `claude plugin marketplace list`. Make sure the required marketplace exists; the Full installer now attempts to register four upstream sources before installing plugins. The two Anthropic marketplaces have different IDs: `claude-plugins-official` and `anthropic-agent-skills`. Ralph uses `ralph-marketplace`, while Morph uses `morph`. Review each [publisher's original source](../integrations/plugins/README.md). Run `claude plugin list` and inspect `/plugin` before rerunning installation. An API login may still be required after the plugin is present.


<br />
<br />


## 🤖 Agent/skill/command counts do not match the author's dashboard


Run `python scripts/coverage-doctor.py` from your cloned repository. A direct Markdown definition counts as file-present; plugin cached but disabled counts as **cached-unconfirmed**, not installed. Some commands are Claude built-ins and some SuperClaude releases may lay out their agent files differently. See [exact coverage](./components/exact-coverage.md) and [private source migration](./installation/private-source-migration.md) rather than generating placeholder files.


<br />
<br />


## 📝 My Obsidian templates already exist or have been customized


The installer refuses to overwrite different versions in `Templates`. Make a private backup, compare your template to the packaged file and resolve the difference yourself. If testing with `-ConfigDir`, always specify a separate `-VaultPath` to avoid inadvertently changing your personal vault.


<br />
<br />


## 🔌 GitHub MCP does not start


Verify Docker Desktop is installed and running, the official `ghcr.io/github/github-mcp-server` image can be downloaded, and localhost port 8085 is free. Sign in through the server's official OAuth browser flow when prompted; don't paste GitHub tokens into PowerShell history or public issue logs. Registration alone is not connection proof.
