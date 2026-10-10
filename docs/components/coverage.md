# ☑️ Reference inventory coverage


**This is the author's named source-machine inventory, not a list of packages silently copied into the installer.** The dashboard counted about 178 discovered entries across local, nested and plugin inventories; those categories overlap.


<br />
<br />


## 🤖 21 global agent definitions


20 are normally installed by the [SuperClaude framework](../installation/superclaude.md); `diagram-architect` is included here as reviewed Ardizuo source.

| Agent | Install path |
| :--- | :--- |
| `backend-architect` | Install via upstream SuperClaude |
| `business-panel-experts` | Install via upstream SuperClaude |
| `deep-research` | Install via upstream SuperClaude |
| `deep-research-agent` | Install via upstream SuperClaude |
| `devops-architect` | Install via upstream SuperClaude |
| `diagram-architect` | Included original definition |
| `frontend-architect` | Install via upstream SuperClaude |
| `learning-guide` | Install via upstream SuperClaude |
| `performance-engineer` | Install via upstream SuperClaude |
| `pm-agent` | Install via upstream SuperClaude |
| `python-expert` | Install via upstream SuperClaude |
| `quality-engineer` | Install via upstream SuperClaude |
| `refactoring-expert` | Install via upstream SuperClaude |
| `repo-index` | Install via upstream SuperClaude |
| `requirements-analyst` | Install via upstream SuperClaude |
| `root-cause-analyst` | Install via upstream SuperClaude |
| `security-engineer` | Install via upstream SuperClaude |
| `self-review` | Install via upstream SuperClaude |
| `socratic-mentor` | Install via upstream SuperClaude |
| `system-architect` | Install via upstream SuperClaude |
| `technical-writer` | Install via upstream SuperClaude |


<br />
<br />


## 🧩 62 global skill names


Only 16 are in the original Ardizuo development pack. Others must be obtained from their source under their own license, or added to a future optional manifest after confirming origin. **Do not mistake a same-name custom replacement for an official upstream package.**

| Skill name | Source status |
| :--- | :--- |
| `Accessibility` | Origin requires review |
| `accessibility-audit` | Third-party or locally sourced; verify origin/terms |
| `accessibility-diff` | Third-party or locally sourced; verify origin/terms |
| `accessibility-fix` | Third-party or locally sourced; verify origin/terms |
| `accessibility-inspect` | Third-party or locally sourced; verify origin/terms |
| `accessibility-scan` | Third-party or locally sourced; verify origin/terms |
| `animate` | Third-party or locally sourced; verify origin/terms |
| `animation-vocabulary` | Third-party or locally sourced; verify origin/terms |
| `apple-design` | Third-party or locally sourced; verify origin/terms |
| `bencium-innovative-ux-designer` | Third-party or locally sourced; verify origin/terms |
| `built-in-browser` | Third-party or locally sourced; verify origin/terms |
| `chrome-browser` | Third-party or locally sourced; verify origin/terms |
| `ci-cd-and-automation` | Third-party or locally sourced; verify origin/terms |
| `claude-md-management` | Included original skill |
| `clean-code-typescript` | Included original skill |
| `code-splitting` | Included original skill |
| `computer-use` | Third-party or locally sourced; verify origin/terms |
| `dead-code-scan` | Included original skill |
| `deep-research` | Third-party or locally sourced; verify origin/terms |
| `design` | Third-party or locally sourced; verify origin/terms |
| `design-system` | Third-party or locally sourced; verify origin/terms |
| `docs` | Third-party or locally sourced; verify origin/terms |
| `docx` | Third-party or locally sourced; verify origin/terms |
| `emil-design-eng` | Third-party or locally sourced; verify origin/terms |
| `Engineering` | Origin requires review |
| `find-animation-opportunities` | Third-party or locally sourced; verify origin/terms |
| `find-skills` | Origin requires review |
| `fix-build` | Included original skill |
| `gauge-improvements` | Included original skill |
| `google-workspace` | Third-party or locally sourced; verify origin/terms |
| `humanizer` | Included original skill |
| `impeccable` | Third-party or locally sourced; verify origin/terms |
| `import-memory` | Third-party or locally sourced; verify origin/terms |
| `improve-animations` | Third-party or locally sourced; verify origin/terms |
| `morning` | Third-party or locally sourced; verify origin/terms |
| `owasp-security` | Third-party or locally sourced; verify origin/terms |
| `pdf` | Third-party or locally sourced; verify origin/terms |
| `pick-ui-library` | Third-party or locally sourced; verify origin/terms |
| `playwright-best-practices` | Third-party or locally sourced; verify origin/terms |
| `pptx` | Third-party or locally sourced; verify origin/terms |
| `pragmatic-code-guidelines` | Included original skill |
| `prototype` | Third-party or locally sourced; verify origin/terms |
| `react-native-best-practices` | Included original skill |
| `reuse-audit` | Included original skill |
| `review-animations` | Third-party or locally sourced; verify origin/terms |
| `root-cause-analysis` | Included original skill |
| `ship-learn-next` | Included original skill |
| `skill-creator` | Origin requires review |
| `supabase` | Third-party or locally sourced; verify origin/terms |
| `supabase-postgres-best-practices` | Third-party or locally sourced; verify origin/terms |
| `team-driven-development` | Included original skill |
| `technical-style-guide` | Included original skill |
| `test-fixing` | Included original skill |
| `UI` | Origin requires review |
| `ui-styling` | Third-party or locally sourced; verify origin/terms |
| `ui-ux-pro-max` | Third-party or locally sourced; verify origin/terms |
| `UX` | Origin requires review |
| `vault-learning` | Included original skill |
| `vercel-composition-patterns` | Third-party or locally sourced; verify origin/terms |
| `vercel-react-best-practices` | Third-party or locally sourced; verify origin/terms |
| `web-design-guidelines` | Third-party or locally sourced; verify origin/terms |
| `xlsx` | Third-party or locally sourced; verify origin/terms |


<br />
<br />


## 🧩 Commands and plugins


The source machine reported **32 global command filenames**. Most `sc:*` capabilities are supplied by the upstream SuperClaude installation; `log-to-vault` is included in the Ardizuo pack. The [12 plugin](../../integrations/plugins/README.md) and [nine MCP](../../integrations/mcp/README.md) entries are listed separately.


<br />
<br />


## ☑️ Verify on a new computer


```powershell
python .\scripts\verify-all.py
claude plugin list
claude mcp list
```

In Claude Code, verify `/skills`, `/mcp` and `/hooks`. The presence of a file doesn't prove a task or agent was run.

[Full installer](../installation/full-setup.md) · [Component catalog](./README.md)


<br />
<br />


## 🚀 Exact-name release verification


This reference list is now machine-auditable. Run `python scripts/coverage-doctor.py` to obtain an offline, literal-name status report across agents, 62 skills, 32 commands, plugins and MCP servers. The report distinguishes direct sources, enabled plugin caches, unconfirmed caches, and missing entries.

See [the explanation of evidence and limitations](./exact-coverage.md) and [the private source migration procedure](../installation/private-source-migration.md). Do not claim all capability names are installed simply because the corresponding package download completed.
