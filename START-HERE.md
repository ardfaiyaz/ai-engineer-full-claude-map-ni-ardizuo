# 🚀 Install Ardizuo in five steps


**Windows 10/11, PowerShell, your own Claude Code account.** Most users need only this page.


<br />
<br />


## ✅ 1. Install the required tools


Skip any already installed; these are **PowerShell commands**, not Bash:

```powershell
winget install --id Git.Git --exact --source winget
winget install --id OpenJS.NodeJS.LTS --exact --source winget
winget install --id Python.Python.3.13 --exact --source winget
winget install --id Anthropic.ClaudeCode --exact --source winget
```

Restart PowerShell. Check:

```powershell
git --version
node --version
python --version
claude --version
```

The extended stack also uses [uv](./docs/installation/uv.md) (Serena, Snyk Agent Scan, Spec Kit) and Bun (gstack). Install them now to avoid `missing-dependency` lines later:

```powershell
winget install --id astral-sh.uv --exact --source winget
winget install --id Oven-sh.Bun --exact --source winget
```

GitHub's Docker MCP and ToolHive also need [Docker](./docs/installation/docker.md).


<br />
<br />


## 📥 2. Download and preview


```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo
.\scripts\install-all.ps1 -All
```

Preview reports intended changes. If the installer reports a conflicting file in your existing `.claude` folder, **stop and compare** rather than deleting it.


<br />
<br />


## 🚀 3. Install only after review


```powershell
.\scripts\install-all.ps1 -Apply -All
```

This installs the agents, skills (including the new `version-log` skill), commands, the 12 baseline plugins, supported MCP registrations, hooks, the empty vault **and the whole extended stack**: Codex, Claude HUD, Trail of Bits, Matt Pocock skills, Ponytail, Firecrawl, Exa, ECC, wshobson Agents, CLI tools and more. It does **not** copy private credentials, reproduce all 62 original skills, or automatically patch your dashboard. Expect it to take a while: it installs well over a hundred plugins.


<br />
<br />


## 🔑 4. Connect accounts and confirm installed plugins


```powershell
claude plugin list
claude mcp list
claude
```

Inside Claude Code, inspect `/plugin`, `/skills`, `/mcp` and `/hooks`. Sign in to each service you choose to use. Optional Atlassian authentication can be skipped if you do not use it.


<br />
<br />


## ☑️ 5. One final local check


```powershell
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
python .\scripts\install-extensions.py --status
```

A missing file is reported by name. If `rules/ardizuo-development.md` is missing on an existing setup:

```powershell
.\scripts\install.ps1 -Profile core          # Preview
.\scripts\install.ps1 -Profile core -Apply   # Install missing core rule
```

This verifier does **not** check provider login or execution. [Full setup and troubleshooting](./docs/installation/full-setup.md).


<br />
<br />


## 🖥️ Optional: Claude Map dashboard


```powershell
npm.cmd install --global claude-map@1.2.3
claude-map -p 8888
```

The original Claude Map is available at <http://localhost:8888>. To apply the **Ardizuo Development Hub overlay**, follow [the separate rehearsal and backup steps](./docs/installation/claude-map.md); don't apply patches blindly.


<br />
<br />


## 🧩 Finish the extended stack


The extended stack is already installed by step 3. A few tools need one action from you:

```powershell
codex login                                         # Codex plugin: ChatGPT or API key sign-in
python .\scripts\install-extensions.py --status     # what is enabled, registered or on PATH
```

Inside Claude Code run `/codex:setup`, `/claude-hud:setup` and, in each repository, `/setup-matt-pocock-skills`. Firecrawl, Exa and 21st Magic ask for their own sign-in. The installer prints the few steps it can't do for you (a Browserbase key and per-project setups).

[Extended stack guide](./docs/installation/extensions.md) · [Master catalog](./docs/components/extension-catalog.md)


<br />
<br />


## ⌨️ Bash commands (only on systems with Bash and the prerequisites installed)


You can use these to **clone** the repo and launch upstream Claude Map on macOS/Linux. Ardizuo's **installer is Windows PowerShell-first**:

```bash
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo
npm install --global claude-map@1.2.3
claude-map -p 8888
```

Do **not** run `.\scripts\install-all.ps1` directly inside a Bash shell.

[Full command index](./docs/prerequisites.md) · [MCPs](./integrations/mcp/README.md) · [Plugins](./integrations/plugins/README.md)
