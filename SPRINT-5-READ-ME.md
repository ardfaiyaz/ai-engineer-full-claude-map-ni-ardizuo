# <img src="docs/assets/lucide/rocket.svg" width="18" height="18" alt="" /> Sprint 5 — existing Claude Map capabilities and honest public release coverage

This update installs **no new third-party capability names** beyond the owner's observed Claude development environment. Added files are presentation assets, a portable global-context template (not a byte-exact private copy), read-only verification scripts, tests, and public documentation. All changed skill/agent/command Markdown headings now use locally available Lucide-style SVG icon assets.

## <img src="docs/assets/lucide/list-checks.svg" width="18" height="18" alt="" /> What is verified

- Public release contract: **21/21 agent names** by default; **36/62 direct skills** by default and **41/62** if five opt-in upstream variants are installed; **20/31 executable commands** by default, **31/31** with 11 upstream variants. Variant definitions may differ from reference-machine customizations.
- Installable local definitions: 28 reviewed files, one base rule, portable `CLAUDE.md` and local Lucide assets, with non-overwriting behavior.
- Documented but not fully reproducible: 17 externally sourced direct skills, four unidentified source skills, exact persona/global-context content, additional skill sidecars and seven locally modified Ardizuo source files.
- Documented and available for guided setup: 12 plugins, nine user MCPs, five hook scripts (four lifecycle events), eight optional Obsidian folders/four templates, and the five-stage Claude Map overlay.
- The **one optional Atlassian plugin MCP authentication** may remain deferred. No credentials, logs, plugin caches, private notes, or unknown-sourced skill definitions have been included.

## <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Update the GitHub checkout

Unzip this update into the **repository root** (not into `.claude`). Keep any existing uncommitted Sprint 3/4 changes; this ZIP supersedes the shared paths but does not rewrite your live Claude installation.

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
Expand-Archive -LiteralPath "$HOME\Downloads\Ardizuo-Existing-Setup-Release-Audit-Sprint-5.zip" -DestinationPath (Get-Location).Path -Force
python -m unittest discover -s tests -v
python .\scripts\release-audit.py
```

The automated tests passed in the builder environment. A real fresh-Windows test, plugin/MCP runtime, and real agent/skill execution remain separate release gates.

## <img src="docs/assets/lucide/terminal.svg" width="18" height="18" alt="" /> Check a fresh isolated config

```powershell
$test = "$HOME\Documents\Ardizuo-Sprint5-Sandbox"
if (Test-Path $test) { throw 'Choose a fresh, empty test folder' }
.\scripts\install-all.ps1 -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks
.\scripts\install-all.ps1 -Apply -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks
python .\scripts\verify-installed-layers.py --config-dir $test --require-hooks --strict-local
```

**Expected:** the installed-layer verifier reports all selected default package files present and five hook registrations. It will deliberately **not** claim that all 62 direct skills are installed. Optional upstream variants are tested only if you explicitly choose them. Do not run `-Apply -All` on your live machine just to test this release.

## <img src="docs/assets/lucide/monitor.svg" width="18" height="18" alt="" /> Follow-up docs

See [the exact by-name matrix](./docs/installation/reproducibility-matrix.md), [Development Hub surface](./docs/components/development-hub-surface.md), [read-only installed-layer audit](./docs/installation/installed-layer-audit.md), [scenario playbook](./docs/installation/scenario-playbook.md), and [license/asset notice](./THIRD_PARTY_NOTICES.md).
