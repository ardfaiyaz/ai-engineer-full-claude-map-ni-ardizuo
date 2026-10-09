<p align="center">
  <img src="./banner.png" width="100%" alt="AI Engineer Full Claude Map ni Ardizuo banner" />
</p>

<h1 align="center">🗂️ AI Engineer Full Claude Map ni Ardizuo</h1>

<p align="center"><strong>One public setup. One guided installer. Clear coverage and opt-in integrations.</strong></p>

<p align="center">Windows-first &nbsp;·&nbsp; Global configuration &nbsp;·&nbsp; Optional services &nbsp;·&nbsp; Local Claude Map dashboard</p>

<p align="center"><a href="#-installation"><strong>Install</strong></a> &nbsp;·&nbsp; <a href="./INSTALL_WITH_AI.md">Use an AI assistant</a> &nbsp;·&nbsp; <a href="./docs/README.md">All documentation</a> &nbsp;·&nbsp; <a href="./docs/architecture.md">Architecture</a></p>

<br />

> **Public assisted installer.** This repository packages the original Ardizuo development components and automates supported third-party installation steps. External accounts and several MCP servers still require manual consent/authentication. The existing 178 discovered skills are **not** all independently bundled: installed source packages, native commands, and plugin caches overlap. Do not confuse configured with connected or executed.

<br />

---

<br />

## 💻 Installation

Start here whether you are new to Claude Code or have an existing global setup.

### 📥 1. Check requirements

Follow the [Windows requirements guide](./docs/prerequisites.md). Install **Git**, **Python**, **Node.js/npm**, and **Claude Code**. Optional integrations use **uvx**, **GitHub CLI**, **Docker**, and **Obsidian**. The installer does not silently add system packages or modify system policy, and the dashboard overlay is explicitly guided to protect an existing customized Claude Map.

### 📥 2. Download and inspect

```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

# Inventory only — no network calls or model usage
.\scripts\doctor.ps1
python .\scripts\verify-all.py
```

### 📥 3. Preview the complete setup

```powershell
# Local files, upstream SuperClaude, 12 plugins, 9 MCP registrations,
# optional hooks, vault and Claude Map. DRY RUN only.
.\scripts\install-all.ps1 -All
```

### 📥 4. Install after review

```powershell
# Explicit approval: can download packages, register MCPs and edit settings.
.\scripts\install-all.ps1 -Apply -All
```

**Important:** This is one entrypoint, but not a no-consent background installer. Provider OAuth and API keys cannot be migrated from another user, and installation failures are reported rather than disguised as success. If the Claude Map overlay is incompatible with upstream, run the [dashboard compatibility guide](./dashboard/claude-map/README.md) instead.

[Detailed one-command walkthrough →](./docs/installation/full-setup.md)

<br />

### ☑️ Measure exact Development Hub coverage

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

### 📥 Other ways to install

| Route | When to choose it | Start |
| :--- | :--- | :--- |
| **AI-assisted** | You want another AI to guide each step and ask before changes | [INSTALL_WITH_AI.md](./INSTALL_WITH_AI.md) |
| **Local only** | You want the 28 original development assets plus base rule, portable context and emoji headings | [Development pack](./docs/installation/ardizuo-development-pack.md) |
| **Core** | You want one minimal global workflow rule | `scripts/install.ps1 -Profile core` |
| **Manual integration** | You want to pick third-party plugins and MCPs | [Components](./docs/components/README.md) |
| **Private migration** | You want exact other agent/skill/command files from your own machine reviewed before release | [Asset ownership and migration](./docs/installation/private-source-migration.md) |

<br />

---

<br />

## 🔄 How the setup works

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

## 📦 What's in the package?

| Layer | Coverage | How it is delivered |
| :--- | :--- | :--- |
| Workflow & configuration | Five stages, gates, portable `CLAUDE.md` and completion instructions | **Reviewed original files plus a clearly labeled portable global-context template** |
| Agent layer | 21 reference names | **1 bundled + 20 pinned and Windows-tested in isolation** |
| Direct skill layer | 62 reference files | **16 original bundled + 20 publisher-pinned by default; 5 publisher variants opt-in; 17 external-origin and 4 unknown-source definitions not automatically reproduced** |
| Superpowers, Ralph, Expo, etc. | 12 plugin IDs | **Marketplace preflight + CLI installs (provider login separate)** |
| SuperClaude commands | ~30 command files | **19 default SuperClaude commands + 11 optional publisher variants; 1 bundled Ardizuo command** |
| Hook layer | 5 event scripts + shared library | **Included source, opt-in activation** |
| MCP layer | 9 reference servers | **Nine documented MCPs; seven supported registration flows and two guided/manual credential flows** |
| Memory | Obsidian vault folder structure, session templates | **Optional 8 folders and 4 templates with emoji headings; approved notes only** |
| Dashboard | AI / Software Engineer Claude Setup | **Local Claude Map + version-sensitive overlay** |

**Reference inventory:** 21 global agents · 62 global skill files · 32 global commands · 12 enabled plugins · 9 user MCPs. These are the source computer's names-only observations, **not** a promise of live availability on a fresh device.

[Component-by-component reference →](./docs/components/README.md)

<br />

---

<br />

## 📖 Guides without the overload

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
| Verifying exact original skill sources and support files | [Read-only source and sidecar checker](./docs/installation/exact-local-origin-review.md) |

<br />

## ☑️ Five-minute setup checklist

**Install:** [Start here](./START-HERE.md) for a short Windows walkthrough. The only required repository entrypoint is `scripts/install-all.ps1` (preview with `-All`, then apply with `-Apply -All`).

**Verify:**

```powershell
python .\scripts\verify-installed-layers.py --strict-local --require-hooks
claude plugin list
claude mcp list
```

This checks package files, registered hooks, and CLI-level provider information. It does not assert that all 62 reference skills were reproduced or that every remote account is authenticated. See the [release checklist](./docs/release-checklist.md).

## 🧹 Documentation cleanup and maintenance

The documentation uses **emoji headings**. Skills, commands, rules, and Obsidian templates
need no additional presentation SVGs after installation. Keep the permanent install guides,
source definitions, and license/security notices; retire dated sprint and hotfix handoff notes.

From the repository root, use:

```powershell
python .\scripts\cleanup-markdown.py          # preview only
python .\scripts\cleanup-markdown.py --apply  # update docs; remove only known obsolete files
python .\scripts\cleanup-markdown.py --check  # verify complete
python -m unittest discover -s tests -v
```

The cleanup **never modifies your live Claude installation**, third-party plugin caches,
API credentials, or existing Obsidian notes. It preserves Markdown frontmatter, fenced code
examples, source definitions and the project banner. Check `git diff --stat` and
`git diff --check` before committing the result.

## 🛡️ Security and licensing

- Installation never copies existing account tokens, `.claude.json`, provider credentials, private projects, transcripts or vault notes into this repository.
- Original files do **not** overwrite different existing files; review conflicts in an isolated `CLAUDE_CONFIG_DIR` first.
- Hook activation, external installs, account sign-ins, vault creation and dashboard patches remain explicit actions.
- The dashboard must stay on **localhost**; MCP inventory views must never expose environment values, auth headers or private paths.
- Third-party tools belong to their original publishers. Their licenses, subscriptions and permissions still apply.
- There are no social-media workflows or integrations in the distributed manifest.

**License:** [MIT for the original Ardizuo project files](./LICENSE). Third-party programs and external packages retain their own licenses. This is an assisted installer with tested packaged components, not a byte-identical export of the author's device.

[Security policy](./SECURITY.md) &nbsp;·&nbsp; [Third-party notices](./THIRD_PARTY_NOTICES.md)

<br />

<p align="center"><sub>Created by Ardizuo · Developer setup distribution · Designed to be inspected and extended</sub></p>
