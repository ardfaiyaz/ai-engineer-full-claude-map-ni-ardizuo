# ☑️ Installed-layer verification — files vs. actual capabilities

**Purpose:** Confirm the contents of your installed configuration without assuming that every listed skill, plugin or MCP works. Use this after the unified installer and before claiming that the setup reproduces the full reference environment.

## 🔎 Three different evidence checks

| Check | Reads | What success actually proves |
|---|---|---|
| `python .\scripts\release-audit.py` | Public source manifests | The **package** covers the declared names; reports blockers even when the original machine has all components |
| `python .\scripts\verify-installed-layers.py --config-dir $test` | The selected target configuration, names only | File locations, hooked handler registrations and optional vault templates exist; **not runtime execution** |
| `python .\scripts\coverage-doctor.py --strict` | Live Claude user-scope inventory | Reference names exist and plugin/MCP identifiers are configured locally; **not provider authentication** |

All three scripts are read-only. None downloads skills, edits your configuration, runs a hook or connects an MCP. For active connections, inspect `claude mcp list` and then test only services you have authorized.

## 📥 Fresh, isolated Windows test

Open **PowerShell** from the repository root. Choose an empty folder so an existing Claude configuration cannot be overwritten.

```powershell
$test = "$HOME\Documents\Ardizuo-Final-Audit-Sandbox"
if (Test-Path $test) { throw "Choose a new, empty folder" }

# Read-only preview. Only previously installed source definitions are selected.
.\scripts\install-all.ps1 -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks

# Explicit test-only installation: no plugins, MCP auth, or live global Claude files.
.\scripts\install-all.ps1 -Apply -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks

# Verify the selected default package files and hook registration.
python .\scripts\verify-installed-layers.py --config-dir $test --require-hooks --strict-local
```

The verifier intentionally expects **36 direct skill files and 20 executable command files** in the default target, alongside all **21 agents**, the reviewed hooks/rules/workflows, portable `CLAUDE.md`, and emoji headings. It does not claim to find the remaining personal skill files which the public package cannot yet reproduce.

## 🧩 When you choose the additional upstream versions

If you personally decide to install the official-publisher versions of the **five modified skills** and **11 modified commands**, add both variant flags at install time:

```powershell
$variantTest = "$HOME\Documents\Ardizuo-Variant-Audit-Sandbox"
if (Test-Path $variantTest) { throw "Choose another empty folder" }
.\scripts\install-all.ps1 -Apply -ConfigDir $variantTest -PinnedSuperClaude -PinnedSkills -UpstreamVariants -SkillUpstreamVariants -Hooks
python .\scripts\verify-installed-layers.py --config-dir $variantTest --upstream-variants --require-hooks --strict-local
```

The resulting 41 skills and 31 executable commands are **not identical to every customized file on the author's computer**. The unverified 17 other direct skills and four unknown-source skills remain excluded. Never claim full 62-skill package coverage from these counts.

## 📝 Optional Obsidian template audit

If you opted into a fresh Obsidian vault, supply its location explicitly:

```powershell
python .\scripts\verify-installed-layers.py --config-dir $test --vault-path "$HOME\Documents\Claude-Dev-Vault"
```

The output counts eight expected folders and four template Markdown files; it does **not** read personal vault notes, write learnings, or verify that Claude successfully created a note. Test note creation only with explicit user approval.

## 🔌 Plugins and MCPs require a separate, live check

```powershell
claude plugin list
claude mcp list
```

In Claude Code, inspect `/skills`, `/mcp` and `/hooks`. The last known reference-machine inventory had **12 enabled plugins**, **nine connected target MCP servers**, and one **optional Atlassian plugin MCP** requiring authentication. The Atlassian login can remain deferred, but it must not be misreported as connected. Other Claude.ai account-level MCPs are connected account integrations, not nine extra global MCPs installed by this package.

## 🛠️ Failure scenarios

- **`MISSING` definitions:** Check that you selected the pinned flags and used the same `--config-dir` during install and verification. Re-running without applying modifications is safe.
- **`CONFLICT` in the installer:** The destination already differs. Stop, privately review your existing file and its source, and merge deliberately. Never add `--force` or publish your settings.
- **Hook script present but registration missing:** Re-run the isolated installer with `-Hooks` and check `settings.json` using the verifier. Script presence doesn't prove event execution.
- **Skill visible but tool call fails:** Check the original publisher's supporting scripts, software dependencies and permissions. A single `SKILL.md` is not always a functional complete skill.
- **Provider says needs authentication:** Follow the vendor's OAuth/API key flow; installation and enabled status do not authorize access.
- **Strict release audit exits nonzero:** This is intentional while the public package remains below the exact reference inventory and fresh-device runtime tests are unfinished.

## 🛡️ Publication and privacy boundary

Share the **plain summary** of verification, not raw `.claude.json`, `settings.json`, provider tokens, personal vault notes, private skill contents, or diagnostic files containing credentials. Review any report before publishing even if it only contains paths or names. Use the [reproducibility matrix](./reproducibility-matrix.md) for the by-name list and the [source migration guide](./private-source-migration.md) when a skill still needs approved provenance.
