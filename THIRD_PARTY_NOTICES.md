# <img src="docs/assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Third-party licenses and attribution

This repository includes original Ardizuo files and references tools maintained by other projects. **It does not claim ownership of external plugin, CLI, MCP or dashboard code.**

<br />

## <img src="docs/assets/lucide/folder-open.svg" width="18" height="18" alt="" /> Upstream sources

- [Claude Code — Anthropic](https://code.claude.com/docs/en/overview)
- [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- [Superpowers plugin and other Claude plugins](https://code.claude.com/docs/en/discover-plugins)
- [Claude Map dashboard — shamim0902](https://github.com/shamim0902/claude-map)
- MCP providers and original URLs under [integrations/mcp](./integrations/mcp/README.md)
- Provider plugins and official references under [integrations/plugins](./integrations/plugins/README.md)

<br />

## <img src="docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> Redistribution boundary

Only reviewed original local skills, agent, hooks and rules are included as sources. Third-party packages are installed using their own official installers, with each provider's licenses and terms. Ardizuo-owned source is offered under the project MIT license. Preserve every upstream license and notice in any derived work.

[Security guidance](./SECURITY.md) · [Release checklist](./docs/release-checklist.md)

## <img src="docs/assets/lucide/folder-open.svg" width="18" height="18" alt="" /> Pinned SuperClaude source definitions

The optional `scripts/install-pinned-superclaude.py` fetches public source files from [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework), commit `fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2`. Copyright **SuperClaude Framework Contributors**. **MIT License**: [upstream license text](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2/LICENSE). Installations must retain any upstream attribution and license obligations. Ardizuo publishes **a manifest and installer**, not copies of these third-party source files.


## <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Pinned third-party SKILL.md prompts (Sprint 3)

`scripts/install-pinned-skills.py` references immutable public commits from the following original publishers; the sources remain copyrighted and licensed by their authors. This repository only publishes pinned source pointers and a verifier, **not their contents**. Users retrieving publisher source should consult and retain the original repository licenses and notices, including transitive dependencies and sibling assets.

- [Bencium Marketplace](https://github.com/bencium/bencium-marketplace) — MIT license indicated by publisher metadata
- [UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — MIT
- [Vercel Labs Skills](https://github.com/vercel-labs/skills) — MIT
- [Supabase Agent Skills](https://github.com/supabase/agent-skills) — MIT
- [Vercel Labs Agent Skills](https://github.com/vercel-labs/agent-skills) — license for this repository was not confirmed; verify before redistribution
- [Impeccable](https://github.com/pbakaus/impeccable) — Apache-2.0, optional upstream variant

Additional **unapproved source candidates** are tracked in `setup/skill-source-candidates.json`; no rights to republish those materials are implied.


## <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Sprint 4 skill provenance additions

The public `setup/source-provenance-lock.json` now references content-matched **SKILL.md** files at immutable commits from original publishers: [Emil Kowalski Skills](https://github.com/emilkowalski/skills) (MIT), [Addy Osmani Agent Skills](https://github.com/addyosmani/agent-skills) (MIT), and [Vercel Labs Agent Skills](https://github.com/vercel-labs/agent-skills) (repository license not confirmed). Optional publisher variants also refer to [Better Frontend Skills](https://github.com/dominika-zajac/better-frontend-skills) (MIT) and [Playwright Labs](https://github.com/vitalics/playwright-labs) (MIT). These third-party materials are **not bundled**; installing downloads original publisher files with fixed commit and blob hashes. No Ardizuo ownership is claimed. Respect license and supporting-file requirements.


## <img src="docs/assets/lucide/file-text.svg" width="18" height="18" alt="" /> Lucide icon attribution

Documentation and installed Markdown use local, inline-compatible SVG icon assets based on the [Lucide icon collection](https://github.com/lucide-icons/lucide). Lucide is distributed under the **ISC License**; preserve the attribution and [publisher license](https://github.com/lucide-icons/lucide/blob/main/LICENSE) in redistributions of icon assets. The icons are presentation-only and **not additional Claude skills or tools**.
