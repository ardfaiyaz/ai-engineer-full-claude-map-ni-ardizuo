<p align="center">
  <img src="./banner.png" alt="AI Engineer Full Claude Map ni Ardizuo banner" width="100%" />
</p>

<h1 align="center">AI Engineer Full Claude Map ni Ardizuo</h1>

<p align="center"><strong>A modular, global Claude Code setup for AI and software engineers.</strong></p>

<p align="center">Windows-first &nbsp;·&nbsp; Local-first &nbsp;·&nbsp; Developer-focused &nbsp;·&nbsp; No hosted website</p>

<p align="center"><a href="#start-here">Get started</a> &nbsp;·&nbsp; <a href="./INSTALL_WITH_AI.md">Install with AI</a> &nbsp;·&nbsp; <a href="./docs/architecture.md">Architecture</a> &nbsp;·&nbsp; <a href="./docs/prerequisites.md">Requirements</a> &nbsp;·&nbsp; <a href="./docs/README.md">All guides</a></p>

<br />

> **Status: bootstrap preview — not a Full release.** The checked-in installer currently adds **one namespaced global rule**. Skills, agents, hooks, provider integrations and the custom dashboard are being reviewed and packaged. The Full profile is **not yet installable**.

<br />

<a id="start-here"></a>
## <img src="./docs/assets/icons/terminal.svg" width="21" height="21" alt="" /> Start here

Choose whichever approach fits you. Everything runs locally; you don't need a hosted website.

| Installation route | Recommended for | Guide |
| :--- | :--- | :--- |
| **AI-assisted** | Guided, approval-first setup | [INSTALL_WITH_AI.md](./INSTALL_WITH_AI.md) |
| **Manual** | Control over each component | [Prerequisites](./docs/prerequisites.md) · [Component catalog](./docs/components/README.md) |
| **PowerShell bootstrap** | Safe Windows starting point | [Local scripts](./scripts/) |

<br />

### Quick start · Windows PowerShell

```powershell
git clone https://github.com/ardfaiyaz/ai-engineer-full-claude-map-ni-ardizuo.git
cd ai-engineer-full-claude-map-ni-ardizuo

.\scripts\doctor.ps1
.\scripts\install.ps1 -Profile core         # Dry run only

# Review changes before choosing to apply:
.\scripts\install.ps1 -Profile core -Apply
```

The current Core bootstrap only adds `rules/ardizuo-development.md` inside the resolved global Claude config directory. It does **not** install or authenticate plugins and MCPs.

<br />

---

<br />

## <img src="./docs/assets/icons/workflow.svg" width="21" height="21" alt="" /> Developer workflow

```text
Triage  →  Contract  →  Dispatch  →  Review  →  Ship
```

Planned layers: specialist agents, skills, lifecycle hooks, global rules, optional Obsidian memory, MCP integrations, plugins and a localhost dashboard.

**Completion mandate:** `simplify` · `code-review` · `reuse-audit` · `dead-code-scan` · `vault-learning`.

Availability is not execution: the eventual checker distinguishes **installed**, **configured**, **authenticated**, and **tested**.

[Explore the architecture →](./docs/architecture.md)

<br />

## <img src="./docs/assets/icons/package.svg" width="21" height="21" alt="" /> What's ready?

| Included now | Planned / pending review |
| :--- | :--- |
| Core rule installer with safe dry run | Original agent, skill and hook packaging |
| Dependency and names-only inventory checks | Complete plugin and MCP installation workflows |
| Backup/restore utilities for supported files | Functional Full and specialist profiles |
| Manifests, six profile definitions, documentation | Attributed and tested dashboard distribution |
| AI prompt and Obsidian templates | Live orchestration, vault and Ship verification |

**Reference machine only:** the author's names-only inventory shows **21 global agents**, **62 global skill files**, **5 custom hooks**, **12 enabled plugins**, and **9 user-scoped MCP registrations**. Those components are **not yet bundled** in this repository. The inventory does not prove authentication or runtime use.

[Component catalog →](./docs/components/README.md)

<br />

---

<br />

## <img src="./docs/assets/icons/book.svg" width="21" height="21" alt="" /> Guides

| Guide | Contents |
| :--- | :--- |
| [Install with AI](./INSTALL_WITH_AI.md) | Portable setup prompt with explicit approvals |
| [Prerequisites](./docs/prerequisites.md) | Choose what to install; each dependency has its own guide |
| [Installation guides](./docs/installation/README.md) | Official sources, recommended PowerShell commands and verification |
| [API keys and PowerShell](./docs/security/api-keys-and-powershell.md) | OAuth, masked prompts, temporary variables, leaks and rotation |
| [Component catalog](./docs/components/README.md) | Agents, skills, hooks, rules, memory and dashboard |
| [Plugin references](./integrations/plugins/README.md) | Third-party plugin checklist |
| [MCP references](./integrations/mcp/README.md) | Transports and authentication requirements |
| [Release checklist](./docs/release-checklist.md) | Tests required before a full release |
| [All documentation](./docs/README.md) | Browse guides without reading everything at once |

<br />

## <img src="./docs/assets/icons/shield.svg" width="21" height="21" alt="" /> Security and licensing

- Never commit live `.claude.json`, tokens, private notes, session histories or plugin caches.
- Third-party tools are **referenced**, not redistributed, unless their licenses expressly permit it.
- Claude Map changes must retain upstream attribution and keep secret-bearing endpoints out of the dashboard.
- No social-media integrations, agents, or automation are included.

**License selection is pending.** Publicly visible source is not the same as a completed, licensed open-source release.

[Security](./SECURITY.md) &nbsp;·&nbsp; [API key safety](./docs/security/api-keys-and-powershell.md) &nbsp;·&nbsp; [Third-party notices](./THIRD_PARTY_NOTICES.md)

<br />

<p align="center"><sub>Portable development workflows · Ardizuo</sub></p>
