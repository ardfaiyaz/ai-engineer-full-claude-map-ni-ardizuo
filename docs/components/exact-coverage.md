# ☑️ Exact Development Hub coverage — the auditable definition of complete


🌐 **Name-for-name verification, with explicit evidence tiers.**

This page explains what a complete reproduction actually means, how the offline checker works, and what remains outside a package author's control. The reference numbers come from the author's exported **names-only** inventory. No credential values, plugin cache source code or private vault notes are included in this repository.


## 📁 Run the inventory from your cloned project


```powershell
# Shows all 21 agents, 62 global skills, 32 commands, 12 plugins and 9 MCP names.
python .\scripts\coverage-doctor.py

# Export a machine-readable report; do not put your actual settings files in an issue.
python .\scripts\coverage-doctor.py --json > "$HOME\Documents\Ardizuo-Coverage-Local.json"

# Return exit code 2 if any referenced name is unconfirmed; useful for release gates.
python .\scripts\coverage-doctor.py --strict
```

The checker reads metadata and searches for recognized definitions. It performs **no network calls**, opens no session transcripts or Obsidian notes, does not invoke models, and never outputs API key values or raw MCP configurations. It is a **local inventory**, not a penetration test or authentication probe.


## ☑️ Interpreting statuses correctly


| Status | Meaning | Counted toward presence? |
| :--- | :--- | :--- |
| `direct` | Matching original Markdown definition in user Claude config under the expected agent/skill/command folder | Yes, file only |
| `enabled-plugin-cache` | Matching skill/command/agent definition in a plugin cache whose exact `plugin@marketplace` setting is enabled | Yes, with caveats |
| `cached-unconfirmed` | Matching cached plugin file but no matching enabled plugin setting | **No** |
| `missing` | No recognized source file | **No** |
| `enabled-in-settings` | Plugin enabled in `settings.json` | Yes, configuration only |
| `registered-user-scope` | MCP name present in user `.claude.json` | Yes, registration only |
| `not-confirmed-*` | Plugin/MCP not confirmed by the checker | **No** |

The checker treats plugin caches as **untrusted inventories**, never as redistributable source. It may not discover newer plugin layouts or runtime-native capabilities. Some commands are built into Claude Code and have no Markdown file to locate. A plugin may be enabled but its server inaccessible. These subtleties are why a strict zero-missing report is necessary but **not sufficient** for release.


## 📄 Completion matrix


| Layer | Name-for-name target | Source of truth | Remaining proof |
| :--- | ---: | :--- | :--- |
| Agents | 21 | Original `agents/*.md` and upstream SuperClaude | Verify each name, then actually delegate a task to a specialist |
| Global skills | 62 | Direct `skills/*/SKILL.md` or installed third-party packages | Source/permissions review, invocation in Claude Code |
| Commands | 32 | Direct `commands` subtree or upstream SuperClaude | Slash menu and smoke test; do not invent fake equivalents |
| Custom hooks | Five scripts, four event types | Included `.mjs` files and `settings.json` entries | Trigger with safe test requests and confirm event output |
| Plugins | 12 exact IDs | Four marketplace sources and `claude plugin list` | Installation, enabled status and provider account sign-in |
| MCPs | Nine names | `claude mcp list` and user registration | Actual connection in `/mcp`, permitted read-only tool call |
| Memory | Eight folders and four templates | Vault path chosen by installer user | Explicit approval, a safe test note, reread evidence |
| Claude Map | Development Hub overlay | Claude Map upstream + custom patches | Same UI at localhost, no exposed secrets; check upstream version |
| Workflow | Five stages and completion mandate | Global Ardizuo rules and files | A sample coding task with observed review/test evidence |


### 🚀 Why 178 is not the release target


`178 discovered entries` combined plugin cache versions and other related capabilities. It is **not** a list of 178 independent skills. An uninstalled, disabled or stale cached entry must not be presented as a working skill. Built-in commands and MCP capabilities aren't separate redistributable `SKILL.md` files.


## 🛡️ How to address a missing source safely


1. Inspect the missing name in this report and compare it to the author's local `~/.claude` installation.
2. If maintained upstream, install its **official source** and verify its actual capabilities. [SuperClaude](../installation/superclaude.md), [plugins](../../integrations/plugins/README.md) and [MCPs](../../integrations/mcp/README.md) are starting points.
3. If it is a locally customized definition, create a **private candidate export** with [source-migration instructions](../installation/private-source-migration.md); review ownership, licensing, secrets, user paths and safe behavior.
4. Only after a reviewed source is added to the distributor manifest should the one-command installer treat the item as installable. Use a clean Windows test before declaring completion.

**Never** fill a gap by making a placeholder agent/skill and calling it the user's original. That would turn a reference inventory into a misleading clone.


## ☑️ CLI tests that need a real Claude Code session


```powershell
claude plugin list
claude mcp list
```

Inside Claude Code: check `/skills`, `/mcp` and `/hooks`; run a small **real** specialist delegation, a test run, and an explicitly approved sample vault note. Recorded hook/script status should distinguish configured from executed. Avoid passing tokens into logs or screenshots.

[All components](./README.md) · [Full installer](../installation/full-setup.md) · [Verification checklist](../installation/verification-checklist.md)


## 📁 Sprint 2: published source provenance lock


`setup/source-provenance-lock.json` is generated from a **local read-only comparison** of the 80-file private review export. It discloses only public filenames, source file paths, pinned publisher commits and classification; no private file contents, tokens or local modified-file SHA256 hashes are published.

At the pinned commits: **42 exact byte matches, 6 text matches after newline normalization, 13 different files and 19 unmapped skills**. Of the exact matches, the SuperClaude command README is documentation. See the [pinned SuperClaude installer](../installation/pinned-superclaude.md) for a create-only installation route for 20 agents and 19 command definitions, with 11 publisher-original command variants available through explicit opt-in.

These counts are reference-machine file comparisons, *not* a claim that every skill dependency, slash command or agent can run on a newly installed machine.


## 🧩 Sprint 3 skill-source progress


Eight of the 29 additional skill files are now reproducible as publisher-pinned, checksum-verified **SKILL.md instruction files** (2 byte-exact, 6 with only line-ending differences). Two further publisher originals differ from the author reference and require explicit opt-in. The 19 unreviewed skills remain excluded; `setup/skill-source-candidates.json` provides 15 unverified publisher path candidates and 4 unknown sources. Use [the pinned skill guide](../installation/pinned-skills.md) to perform a safe local comparison. Source-file reproducibility does **not** imply required sidecars or runtime behavior are present.


## 🚀 Current release-audit status (after Sprint 4)


The historical **Sprint 2** and **Sprint 3** numbers above describe their individual checkpoints, not today's source lock. The current installer offers **20 default pinned skill files and five explicit upstream variants**, with **four unknown skill origins** and **17 other direct-skill sources** unresolved. Use the [latest matrix](../installation/reproducibility-matrix.md) and `python scripts/release-audit.py` for the authoritative current breakdown. Do not equate 178 dashboard-discovered skill entries with 178 standalone redistributable skill packages.
