# 📖 Documentation


Welcome! You do **not** need to read every file. Most people can install the supported setup using [the quick start](../START-HERE.md).


<br />
<br />


## 🚀 Common tasks


| Task | Guide |
| --- | --- |
| Install the public Claude setup | [Start here](../START-HERE.md) |
| Copy commands for Git, Node, Python and Claude | [Prerequisites](./prerequisites.md) |
| Install or troubleshoot 12 plugins | [Plugin catalog](../integrations/plugins/README.md) |
| Set up nine MCP servers | [MCP catalog](../integrations/mcp/README.md) |
| Add Claude Map on localhost | [Dashboard](./installation/claude-map.md) |
| Understand the extended stack that `-All` installs | [Extended stack](./installation/extensions.md) |
| Understand every installer switch | [Full setup](./installation/full-setup.md) |
| See how the five stages and layers fit together | [Architecture](./architecture.md) |
| Fix common errors | [Troubleshooting](./troubleshooting.md) |


<br />
<br />


## 📋 Reference and maintainer material


[Architecture](./architecture.md) · [Master extension catalog](./components/extension-catalog.md) · [Skill catalog](./components/skills/README.md) · [Hook catalog](./components/hooks/README.md) · [Actual coverage](./installation/reproducibility-matrix.md) · [Security](../SECURITY.md) · [Source provenance](../THIRD_PARTY_NOTICES.md)

The reference machine has 21 agent files, 62 direct skill entries, 31 executable commands, 12 enabled plugins and nine registered target MCPs. Not all are reproducible by the **public** installer yet; do not claim otherwise.

On top of that baseline, the [master extension catalog](./components/extension-catalog.md) tracks **74 researched rows**, delivered by 40 packages: 24 plugin packages (115 plugin IDs), 3 MCP registrations, 7 global CLI tools, pinned Karpathy skills, gstack, one credential-gated MCP and 3 per-project setups. `-All` installs them in the same run; see [extended stack](./installation/extensions.md). The Ardizuo pack also gained a 17th skill, `version-log`.


<br />
<br />


## 🛠️ Scripts at a glance


Run every script from the repository root in Windows PowerShell. Installers preview by default and change nothing until you pass `-Apply` or `--apply`.

| Script | Purpose | Writes anything? |
| --- | --- | --- |
| `scripts/install-all.ps1` / `.py` | Main installer for every layer; see the [switch reference](./installation/full-setup.md) | Only with `-Apply` |
| `scripts/install-extensions.py` | Extended stack (called by `-All`): `--list`, `--status`, `--select <ids/groups>` | Only with `--apply` |
| `scripts/install.ps1` | Profile installer (`-Profile core` or `development`) | Only with `-Apply` |
| `scripts/install-development.ps1` | The 29 reviewed Ardizuo files on their own | Only with `-Apply` |
| `scripts/install-pinned-superclaude.py` | 20 agents + 19 commands from a pinned SuperClaude commit | Only with `--apply` |
| `scripts/install-pinned-skills.py` | 20 publisher-pinned skills (+5 opt-in variants) | Only with `--apply` |
| `scripts/install-dashboard.py` | Claude Map overlay check, `--rehearse`, then `--apply` | Only with `--apply` |
| `scripts/register-hooks.mjs` | Adds the five hooks to `settings.json` with a backup | Only with `--apply` |
| `scripts/doctor.ps1` / `doctor-development.ps1` | Local tool and file inventory | No |
| `scripts/verify-installed-layers.py` | Checks installed files, hooks and vault templates in one config | No |
| `scripts/coverage-doctor.py` / `verify-all.py` | Name-by-name coverage of the reference inventory | No |
| `scripts/release-audit.py` | What the public package can reproduce | No |
| `scripts/review-exact-local-components.py`, `verify-remaining-skill-sources.py`, `prepare-private-review.py` | Private source and provenance review | Only to a private folder you choose |
| `scripts/export-inventory.ps1` | Names-only inventory of your config | One local JSON file |
| `scripts/backup.ps1` / `restore.ps1` | Back up and restore the Ardizuo-managed files only | Only with `-Apply` |
| `scripts/cleanup-markdown.py` | Maintainer check that headings use emoji | Only with `--apply` |

Offline checks for all of this run in CI with `python -m unittest discover -s tests`.

[Back to project README](../README.md)
