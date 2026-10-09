<p align="center">
  <img src="./banner.png" width="100%" alt="AI Engineer Full Claude Map ni Ardizuo banner" />
</p>

<h1 align="center"><img src="./docs/assets/lucide/layers.svg" width="24" height="24" alt="" /> AI Engineer Full Claude Map ni Ardizuo</h1>

<p align="center"><strong>One repository. One guided installer. A guided Claude Code development stack.</strong></p>

<p align="center">Windows-first &nbsp;·&nbsp; Global configuration &nbsp;·&nbsp; Optional services &nbsp;·&nbsp; Local Claude Map dashboard</p>

<p align="center"><a href="#-installation"><strong>Install</strong></a> &nbsp;·&nbsp; <a href="./INSTALL_WITH_AI.md">Use an AI assistant</a> &nbsp;·&nbsp; <a href="./docs/README.md">All documentation</a> &nbsp;·&nbsp; <a href="./docs/architecture.md">Architecture</a></p>

<br />

> **Assisted Full Installer Preview.** This repository packages the original Ardizuo development components and automates supported third-party installation steps. External accounts and several MCP servers still require manual consent/authentication. The existing 178 discovered skills are **not** all independently bundled: installed source packages, native commands, and plugin caches overlap. Do not confuse configured with connected or executed.

<br />

---

<br />

## <img src="./docs/assets/icons/terminal.svg" width="19" height="19" alt="" /> Installation

Start here whether you are new to Claude Code or have an existing global setup.

### <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 1. Check requirements

Follow the [Windows requirements guide](./docs/prerequisites.md). Install **Git**, **Python**, **Node.js/npm**, and **Claude Code**. Optional integrations use **uvx**, **GitHub CLI**, **Docker**, and **Obsidian**. The installer does not silently add system packages or modify system policy, and the dashboard overlay is explicitly guided to protect an existing customized Claude Map.

### <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 2. Download and inspect

```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

# Inventory only — no network calls or model usage
.\scripts\doctor.ps1
python .\scripts\verify-all.py
```

### <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 3. Preview the complete setup

```powershell
# Local files, upstream SuperClaude, 12 plugins, 9 MCP registrations,
# optional hooks, vault and Claude Map. DRY RUN only.
.\scripts\install-all.ps1 -All
```

### <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> 4. Install after review

```powershell
# Explicit approval: can download packages, register MCPs and edit settings.
.\scripts\install-all.ps1 -Apply -All
```

**Important:** This is one entrypoint, but not a no-consent background installer. Provider OAuth and API keys cannot be migrated from another user, and installation failures are reported rather than disguised as success. If the Claude Map overlay is incompatible with upstream, run the [dashboard compatibility guide](./dashboard/claude-map/README.md) instead.

[Detailed one-command walkthrough →](./docs/installation/full-setup.md)

<br />

### <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Measure exact Development Hub coverage

```powershell
# Detailed offline report for EVERY reference agent, skill, command, plugin and MCP.
# "missing" and "cached-unconfirmed" are NOT installed.
python .\scripts\coverage-doctor.py

# Machine-readable names and statuses; does not print paths, keys or server configuration.
python .\scripts\coverage-doctor.py --json

# Audit the public repository installability separately from the current user environment.
python .\scripts\release-audit.py
```

The reference list contains **21 agents, 62 direct global skills, 31 executable commands plus one README, 12 enabled plugins and nine MCP server names**. This is not a promise that current upstream SuperClaude/plugin versions reproduce every name. [Read the exact-coverage guide](./docs/components/exact-coverage.md).

<br />

### <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Other ways to install

| Route | When to choose it | Start |
| :--- | :--- | :--- |
| **AI-assisted** | You want another AI to guide each step and ask before changes | [INSTALL_WITH_AI.md](./INSTALL_WITH_AI.md) |
| **Local only** | You want the 28 original development assets plus base rule, portable context and local icons | [Development pack](./docs/installation/ardizuo-development-pack.md) |
| **Core** | You want one minimal global workflow rule | `scripts/install.ps1 -Profile core` |
| **Manual integration** | You want to pick third-party plugins and MCPs | [Components](./docs/components/README.md) |
| **Private migration** | You want exact other agent/skill/command files from your own machine reviewed before release | [Asset ownership and migration](./docs/installation/private-source-migration.md) |

<br />

---

<br />

## <img src="./docs/assets/icons/workflow.svg" width="19" height="19" alt="" /> How the setup works

```text
Triage  ───→ Contract ───→ Dispatch ───→ Review ───→ Ship
                      │
           Agents · Skills · Rules
                      │
        Hooks · Memory · MCP · Plugins
```

**Completion mandate:** `simplify` · `code-review` · `reuse-audit` · `dead-code-scan` · `vault-learning`

Native Claude Code features stay native; the installer adds original skills, upstream SuperClaude and approved plugin integrations instead of making fake copies of built-in features.

[Detailed system architecture →](./docs/architecture.md) · [Actual Development Hub layers](./docs/components/development-hub-surface.md)

<br />

## <img src="./docs/assets/icons/package.svg" width="19" height="19" alt="" /> What's in the package?

| Layer | Coverage | How it is delivered |
| :--- | :--- | :--- |
| Workflow & configuration | Five stages, gates, portable `CLAUDE.md` and completion instructions | **Reviewed original files plus a clearly labeled portable global-context template** |
| Agent layer | 21 reference names | **1 bundled + 20 pinned and Windows-tested in isolation** |
| Direct skill layer | 62 reference files | **16 original bundled + 20 publisher-pinned by default; 5 publisher variants opt-in; 17 external-origin and 4 unknown-source definitions not automatically reproduced** |
| Superpowers, Ralph, Expo, etc. | 12 plugin IDs | **Marketplace preflight + CLI installs (provider login separate)** |
| SuperClaude commands | ~30 command files | **19 default SuperClaude commands + 11 optional publisher variants; 1 bundled Ardizuo command** |
| Hook layer | 5 event scripts + shared library | **Included source, opt-in activation** |
| MCP layer | 9 reference servers | **Nine documented MCPs; seven supported registration flows and two guided/manual credential flows** |
| Memory | Obsidian vault folder structure, session templates | **Optional 8 folders and 4 templates plus local Lucide icon assets; approved notes only** |
| Dashboard | AI / Software Engineer Claude Setup | **Local Claude Map + version-sensitive overlay** |

**Reference inventory:** 21 global agents · 62 global skill files · 32 global commands · 12 enabled plugins · 9 user MCPs. These are the source computer's names-only observations, **not** a promise of live availability on a fresh device.

[Component-by-component reference →](./docs/components/README.md)

<br />

---

<br />

## <img src="./docs/assets/icons/book.svg" width="19" height="19" alt="" /> Guides without the overload

| Need help with… | Open this |
| :--- | :--- |
| Installing required tools | [Prerequisites and individual installers](./docs/prerequisites.md) |
| Setting up plugins | [12 plugin-specific guides](./integrations/plugins/README.md) |
| Configuring MCP servers | [9 MCP-specific guides](./integrations/mcp/README.md) |
| Getting API keys or OAuth | [Credentials and PowerShell security](./docs/security/api-keys-and-powershell.md) |
| Global setup, hooks and conflicts | [Full installer walkthrough](./docs/installation/full-setup.md) |
| Claude Map local dashboard | [Dashboard setup](./dashboard/claude-map/README.md) |
| Obsidian memory | [Vault guide](./vault/README.md) |
| Fixing common issues | [Troubleshooting](./docs/troubleshooting.md) |
| Testing before publishing | [Release checklist](./docs/release-checklist.md) |
| Exact inventory and missing capabilities | [Coverage doctor](./docs/components/exact-coverage.md) |
| Privately reviewing missing original files | [Private migration instructions](./docs/installation/private-source-migration.md) |

<br />

## <img src="./docs/assets/icons/shield.svg" width="19" height="19" alt="" /> Security and licensing

- Installation never copies existing account tokens, `.claude.json`, provider credentials, private projects, transcripts or vault notes into this repository.
- Original files do **not** overwrite different existing files; review conflicts in an isolated `CLAUDE_CONFIG_DIR` first.
- Hook activation, external installs, account sign-ins, vault creation and dashboard patches remain explicit actions.
- The dashboard must stay on **localhost**; MCP inventory views must never expose environment values, auth headers or private paths.
- Third-party tools belong to their original publishers. Their licenses, subscriptions and permissions still apply.
- There are no social-media workflows or integrations in the distributed manifest.

**License:** [MIT for the original Ardizuo project files](./LICENSE). Third-party programs and external packages retain their own licenses. This is an installer preview, not a tested v1.0 release.

[Security policy](./SECURITY.md) &nbsp;·&nbsp; [Third-party notices](./THIRD_PARTY_NOTICES.md)

<br />

<p align="center"><sub>Created by Ardizuo · Developer setup distribution · Designed to be inspected and extended</sub></p>


### <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Sprint 3 pinned skills

The new [publisher-pinned skill installer](docs/installation/pinned-skills.md) verifies public source checksums and installs 8 compared SKILL.md files without overwriting personal definitions. Two publisher variants are opt-in and 19 unresolved skills are explicitly excluded pending author-side comparison. Use `scripts/verify-remaining-skill-sources.py` to compare the next 15 public source candidates privately. The complete five-stage Claude Map rehearsal and Sprint 2 SuperClaude sourcing remain included.


### <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Sprint 4: extended source-matched skills

The pinned-source setup now supports **20 default third-party SKILL.md prompts**, with five optional upstream variants and four unresolved names. Use [`docs/installation/pinned-skills.md`](docs/installation/pinned-skills.md) for a disposable Windows installation test. A sourced prompt is not necessarily an operational skill without its publisher sidecar files.


## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> What the public installer really reproduces

The reference machine has **21 agent files, 62 direct skill definitions, 31 executable command files plus one `README.md`, 12 enabled plugins and nine target user MCP servers**. The public installer does **not yet** exactly reproduce all of those on a fresh account. See the [release coverage matrix](docs/installation/reproducibility-matrix.md) for default, optional, provider-authenticated, and blocked items. Never publish personal provider configuration or private vault content.


## <img src="docs/assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Verified files are not identical to a personal machine in every case

The source lock never republishes private local modifications, credentials, cached plugins or licensed third-party files. The public **default** package can reproduce all 21 named agent definitions, 36 of 62 direct skill definitions, and 20 of 31 executable commands; selected upstream versions raise those to 41 and 31 respectively, **but some differ from the original device**. See the [complete by-name reproducibility matrix](./docs/installation/reproducibility-matrix.md) and the [installed-layers audit](./docs/installation/installed-layer-audit.md) for honest verification.
