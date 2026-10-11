# 🧩 Existing Claude Code plugins


The Ardizuo reference setup uses **12 plugins**, listed below. The full installation adds the extended-stack plugins described further down. The repository does not bundle plugin source code or another person's account sessions.


<br />
<br />


## 🚀 Recommended: install the existing plugin set


In **Windows PowerShell**, from the repository root:

```powershell
# Preview every external action first.
.\scripts\install-all.ps1 -External -Plugins

# Install the 12 declared plugins and register their marketplaces when needed.
.\scripts\install-all.ps1 -Apply -External -Plugins

# Show actual installed/enabled status.
claude plugin list
```

An installer attempt is **not** proof of successful installation, enablement or provider sign-in. Each user authorizes their own account.


<br />
<br />


## 📋 Included plugin IDs


| Plugin | Purpose |
| --- | --- |
| `playwright@claude-plugins-official` | Browser testing and automation; inspect browser access |
| `context7@claude-plugins-official` | Current library and framework documentation |
| `superpowers@claude-plugins-official` | Planning, debugging and implementation skills |
| `document-skills@anthropic-agent-skills` | Document creation and editing skills |
| `example-skills@anthropic-agent-skills` | Published example skills |
| `morph-compact@morph` | Morph integration; provider account may be required |
| `ralph-skills@ralph-marketplace` | Ralph planning and PRD workflows |
| `expo@claude-plugins-official` | React Native and Expo integration |
| `stripe@claude-plugins-official` | Stripe API and payment integration; requires authorization |
| `sentry@claude-plugins-official` | Error monitoring and issue triage; requires authorization |
| `atlassian@claude-plugins-official` | Atlassian tools; sign-in optional if unused |
| `notion@claude-plugins-official` | Notion workspace interaction; requires authorization |


<br />
<br />


## ⌨️ Manual commands (only if the guided installer did not finish)


Do **not** run every command again if plugins are already installed. Register only a missing marketplace, then install only the missing plugin IDs.

```powershell
# Add only marketplaces not already listed in Claude Code.
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add anthropics/skills
claude plugin marketplace add snarktank/ralph
claude plugin marketplace add morphllm/morph-claude-code-plugin

# Individual plugin installs; choose only missing items.
claude plugin install playwright@claude-plugins-official
claude plugin install context7@claude-plugins-official
claude plugin install superpowers@claude-plugins-official
claude plugin install document-skills@anthropic-agent-skills
claude plugin install example-skills@anthropic-agent-skills
claude plugin install morph-compact@morph
claude plugin install ralph-skills@ralph-marketplace
claude plugin install expo@claude-plugins-official
claude plugin install stripe@claude-plugins-official
claude plugin install sentry@claude-plugins-official
claude plugin install atlassian@claude-plugins-official
claude plugin install notion@claude-plugins-official
```

In Claude Code, check `/plugin` and `/skills`. If applicable, connect the plugin's service through `/mcp` (e.g. Notion, Sentry, Stripe, Atlassian). An Atlassian login can remain unconnected if you do not use it.


<br />
<br />


## 🧩 Extended-stack plugins (installed by -All, beyond the 12)


The full installation also installs **24 plugin packages (115 plugin IDs)** from the extended stack. They are listed here so you can recognise them in `claude plugin list`.

| Plugin | Purpose |
| --- | --- |
| `codex@openai-codex` | Cross-model review and delegation (`/codex:review`); needs `codex login` |
| `claude-hud@claude-hud` | Status line for context, tools, agents and todos |
| `differential-review`, `supply-chain-risk-auditor`, `property-based-testing`, `mutation-testing`, `spec-to-code-compliance`, `static-analysis` `@trailofbits` | Security and testing skills |
| `mattpocock-skills@mattpocock` | 27 engineering-practice skills |
| `frontend-visual-qa@daymade-skills` | Rendered UI visual QA |
| `ponytail@ponytail` | Simplest-solution coding mode (adds hooks) |
| `firecrawl@claude-plugins-official`, `exa@claude-plugins-official` | Web extraction and search (provider sign-in) |
| `21st@21st-dev` | 21st Magic UI components (`API_KEY_21ST`) |
| `compound-engineering@compound-engineering-plugin` | `/ce-*` brainstorm, plan, work, review, compound workflow |
| `claude-mem@thedotmack` | Automatic session memory |
| `probity@probity`, `tdd-guard@tdd-guard` | Test-first guardrails (overlap; disable one if they conflict) |
| `autoharness@autoharness`, `i-have-adhd@i-have-adhd` | Skill derivation from sessions; concise answer style |
| `beads@beads-marketplace`, `all-skills@mcp-use` | Beads task tracking; MCP server building skills |
| `ecc@ecc` | Everything Claude Code: 71 agents, 311 skills, hooks |
| 92 × `…@claude-code-workflows` | wshobson Agents collection (social-media plugins excluded) |

```powershell
.\scripts\install-all.ps1 -Apply -All                          # installs these with everything else
.\scripts\install-all.ps1 -Apply -External -Extensions all     # only the extended stack
python .\scripts\install-extensions.py --status                # enabled state per package
```

[Extended stack guide](../../docs/installation/extensions.md) · [Master extension catalog](../../docs/components/extension-catalog.md)


<br />
<br />


## 🛡️ Troubleshoot or remove


If an install fails, check whether the marketplace was successfully registered and the plugin ID still exists; then retry only that plugin. To remove a plugin, use Claude Code's plugin manager for its exact ID rather than deleting caches or another user's settings. Never share tokens, session data or `settings.json`.

[Full installation](../../docs/installation/full-setup.md) · [MCP catalog](../mcp/README.md) · [Security](../../SECURITY.md)
