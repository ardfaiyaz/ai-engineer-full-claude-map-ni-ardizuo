# 🧩 Optional extensions


These are the researched extensions from the [master extension catalog](../components/extension-catalog.md): Codex review, Claude HUD, Trail of Bits security skills, Matt Pocock skills, Ponytail, Firecrawl, Exa, 21st Magic, n8n MCP and more. They are **opt-in** and are **never** installed by `-All`.

The installer reads [`setup/extension-catalog.json`](../../setup/extension-catalog.json). It does a dry run by default and skips anything already enabled. It never reads, stores or prints credentials.


<br />
<br />


## 🚀 Recommended: preview, then install the priority set


From **Windows PowerShell** in the repository root:

```powershell
# See every package, its group and whether it is an alternative.
python .\scripts\install-extensions.py --list

# Preview the priority set (nothing changes).
.\scripts\install-all.ps1 -External -Extensions priority

# Install it after reviewing the preview.
.\scripts\install-all.ps1 -Apply -External -Extensions priority

# Check what is enabled or registered (names only).
python .\scripts\install-extensions.py --status
```

The **priority** set is Codex, Claude HUD, Trail of Bits `differential-review`, Ponytail and Firecrawl. It also prints guided steps for Probity, Agentation, MCP Inspector, Beads and mcp-use.


<br />
<br />


## 📋 Selections


Pass one or more IDs or groups, separated by commas, to `-Extensions` (or `--select` when you call `install-extensions.py` directly).

| Selection | Installs |
| --- | --- |
| `priority` | The top ten from the catalog shortlist |
| `security` | Six Trail of Bits plugins and Snyk Agent Scan guidance |
| `testing` | Property-based and mutation testing |
| `engineering` | Matt Pocock skills, Ponytail, Karpathy skills guidance |
| `frontend` | Daymade `frontend-visual-qa`, 21st Magic, Agentation guidance |
| `research` | Firecrawl and Exa |
| `automation` | n8n MCP |
| `mcp-dev` | MCP Inspector and mcp-use guidance |
| `all` | Every package **except** alternatives |
| `<id>` | One package, for example `codex,claude-hud` |

**Alternatives** must be named explicitly: `playwright-mcp`, `compound-engineering`, `claude-mem`, `tdd-guard`, `autoharness`, `i-have-adhd` and `gstack`. The installer refuses two packages from the same exclusive group, such as `probity,tdd-guard`.


<br />
<br />


## ⌨️ Manual commands


Run only what is missing. Each command comes from the publisher's own README or marketplace manifest.

```powershell
# Priority plugins
claude plugin marketplace add openai/codex-plugin-cc
claude plugin install codex@openai-codex
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud@claude-hud
claude plugin marketplace add trailofbits/skills
claude plugin install differential-review@trailofbits
claude plugin marketplace add DietrichGebert/ponytail
claude plugin install ponytail@ponytail
claude plugin install firecrawl@claude-plugins-official

# Other researched plugins
claude plugin install supply-chain-risk-auditor@trailofbits
claude plugin install property-based-testing@trailofbits
claude plugin install mutation-testing@trailofbits
claude plugin install spec-to-code-compliance@trailofbits
claude plugin install static-analysis@trailofbits
claude plugin marketplace add mattpocock/skills
claude plugin install mattpocock-skills@mattpocock
claude plugin marketplace add daymade/claude-code-skills
claude plugin install frontend-visual-qa@daymade-skills
claude plugin install exa@claude-plugins-official
claude plugin marketplace add 21st-dev/magic-mcp
claude plugin install 21st@21st-dev

# n8n MCP (documentation tools; no credentials)
claude mcp add --scope user n8n-mcp -e MCP_MODE=stdio -e LOG_LEVEL=error -e DISABLE_CONSOLE_OUTPUT=true -- npx -y n8n-mcp
```

Inside Claude Code, run `/reload-plugins` (if your version has it), then `/codex:setup` and `/claude-hud:setup`.


<br />
<br />


## 📁 Project-only and on-demand tools


These are printed, never executed. Run them inside the specific project after reviewing the publisher's documentation.

```powershell
npm install -D @nizos/probity                                # Probity: one test project first
npm install -D agentation                                    # Agentation: React/Next.js only
claude mcp add agentation -- npx -y agentation-mcp server    # Agentation MCP for that project
npx @modelcontextprotocol/inspector                          # MCP Inspector, on demand
npm install -g @beads/bd                                     # Beads CLI
npx -y create-mcp-use-app@latest                             # mcp-use starter
uvx snyk-agent-scan@latest                                   # Snyk Agent Scan, review privacy first
npx ccusage@latest                                           # Token usage report
uv tool install specify-cli                                  # GitHub Spec Kit
```


<br />
<br />


## 🛡️ Safety


- Provider sign-in (Codex, Firecrawl, Exa, 21st) happens in each publisher's own flow. Never paste API keys into commands, issues or commits.
- Ponytail and Probity add their own hooks. Check `/hooks` after installing and compare them with the five Ardizuo hooks.
- Agentation uses the PolyForm Shield license, which is not an open-source license. Read it before using it commercially.
- Trail of Bits content is CC-BY-SA-4.0. Install it from the publisher; don't copy it into this repository.
- An exit code of 0 means only that the CLI accepted the command. It doesn't prove the extension is enabled, signed in or working.

To remove an extension, use `claude plugin uninstall <id>` or `claude mcp remove <name>` for that one entry only.

[Master catalog](../components/extension-catalog.md) · [Plugins](../../integrations/plugins/README.md) · [MCPs](../../integrations/mcp/README.md) · [Installation index](./README.md)
