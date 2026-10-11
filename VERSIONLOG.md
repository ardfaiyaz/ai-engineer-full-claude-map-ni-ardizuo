# 📄 Version log


All notable changes to this repository, newest first. Entries are written with the `version-log` skill: one entry per change set, taken from the real Git history, with the checks that actually ran. Earlier entries are never rewritten.


<br />
<br />


## 🚀 2026-10-11.2 — One full installation, version-log skill, docs refresh


### 🧩 Added

- `version-log` skill (`ardizuo-plugin/skills/version-log/SKILL.md`), the 29th reviewed Ardizuo file. Every installation now keeps a `VERSIONLOG.md` in each repository it changes.
- This `VERSIONLOG.md`.
- Extended-stack install types in `scripts/install-extensions.py`: global CLI tools (npm, uv, winget), commit-pinned skill files with Git-blob verification, and a Git skill suite (gstack).
- Previously "guided" entries now install for real: Probity (`probity@probity`), Beads (`beads@beads-marketplace` + `@beads/bd`), mcp-use (`all-skills@mcp-use`), Everything Claude Code (`ecc@ecc`), 92 wshobson Agents plugins, Agentation MCP, Codex CLI, MCP Inspector, Snyk Agent Scan, ccusage, Spec Kit, ToolHive and four Karpathy skills (with their MIT `LICENSE`).
- Docs: switch reference, scripts table, repository layout, per-package tables, first-run steps, overlap guidance, troubleshooting for the extended stack, and where each tool fits in the five stages.

### 🔄 Changed

- `install-all.ps1 -All` now installs the whole extended stack (`-Extensions all`). It is no longer a separate optional step.
- Overlapping tools (Probity + TDD Guard, Compound Engineering + gstack + ECC, Firecrawl + Exa, …) are installed together with a printed note instead of being refused.
- `release-audit.py` reports Ardizuo skills added after the reference snapshot (`version-log`) separately, so the 36/62 reference coverage figure stays accurate.

### 🛠️ Fixed

- `docs/installation/superclaude.md` claimed `-All` runs the upstream SuperClaude CLI; it installs the pinned files.
- `docs/installation/pinned-superclaude.md` still said 8 pinned skills and 19 excluded; it is 20 default, 5 opt-in variants and 4 excluded.
- `docs/architecture.md` status column described an early phase; it now shows current coverage.
- `docs/components/development-hub-surface.md` mentioned icon assets that were replaced by emoji.

### 🧹 Removed

- wshobson plugins `social-publishing` and `hermes-tweet` are excluded from the install, under the no-social-automation rule.

**Verification:** `python -m unittest discover -s tests` passed (94 tests); `release-audit.py` and `cleanup-markdown.py --check` clean; dry run of all 40 extended-stack packages; real hash-verified download of the 10 Karpathy files into a throwaway folder. Plugins, MCPs and CLI tools were not installed on a clean machine.


<br />
<br />


## 🚀 2026-10-11 — Researched extension catalog (`6b95291`)


### 🧩 Added

- `setup/extension-catalog.json`: 74 researched rows (20 skills, 6 MCPs, 2 guardrails, 4 agent collections, 8 extension systems, 14 commands, 20 tools) with verified repositories, licenses, commits and plugin IDs.
- `scripts/install-extensions.py` and `install-all -Extensions <selection>`.
- `docs/components/extension-catalog.md` and `docs/installation/extensions.md`; extension sections in the plugin, MCP, hook, agent, command and skill pages.
- `tests/test_extensions.py`.

### 📖 Docs

- Corrected the draft inventory: Beads, ccusage and ECC repositories moved; Firecrawl and Exa ship as official plugins; Agentation is PolyForm Shield; TDD Guard is Probity's predecessor.

**Verification:** 91 tests passed; CI green.


<br />
<br />


## 🚀 2026-10-10 — Public setup, installers and audits


### 🧩 Added

- Project banner and initial Claude setup docs (`f11949b`); installation, integration and security guides (`37d4358`).
- Unified installer `install-all` and Development Hub preview (`393a60d`).
- Marketplace registration, exact coverage audit and vault templates (`f37d4ff`).
- Five-stage Claude Map compatibility rehearsal (`d3c792f`).
- Pinned SuperClaude agent and command installer (`e1aa988`).
- Expanded pinned skills and full release coverage audit (`6e8b37c`).

### 🔄 Changed

- Repository docs cleaned and SVG icons replaced with emoji headings (`9324156`).
- Public installation and release guide finalized (`47b3a9f`); guides streamlined with copyable install commands (`e058eae`); Markdown section spacing improved (`dd0f5f3`).
