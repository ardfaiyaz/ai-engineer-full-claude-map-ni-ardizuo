# Sprint 2 — source-pinned SuperClaude (public source, private-file safe)

This update is a **patch for the repo on main at `d3c792f`**, not a complete replacement.

## Implemented

- A source provenance lock for the 80 candidates: 42 byte-exact, 6 newline-normalized, 13 modified, 19 unmapped.
- A hash-verified installer for 20 upstream agents + 19 exact command definitions. Optional 11 upstream command variants for a clean machine.
- Support for `-PinnedSuperClaude` and `-UpstreamVariants` in the unified PowerShell launcher, separate from `-SuperClaude`.
- Create-only, preflight conflict checking, all-downloads-before-writes and rollback of new files upon failure.
- Explicit upstream MIT attribution, new setup documentation, regression tests.

## Run this on Windows — no live changes

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
Expand-Archive -LiteralPath "$HOME\Downloads\Ardizuo-Source-Pinned-SuperClaude-Sprint-2.zip" -DestinationPath (Get-Location).Path -Force
python -m unittest discover -s tests -v

$testConfig = "$HOME\Documents\Ardizuo-Pinned-SuperClaude-Sprint2-Test"
if (Test-Path $testConfig) { throw "Use a new empty test config folder" }
python .\scripts\install-pinned-superclaude.py --config-dir $testConfig
python .\scripts\install-pinned-superclaude.py --apply --config-dir $testConfig
python .\scripts\install-pinned-superclaude.py --apply --config-dir $testConfig
python .\scripts\install-pinned-superclaude.py --config-dir $testConfig --upstream-variants
python .\scripts\install-pinned-superclaude.py --apply --config-dir $testConfig --upstream-variants
```

Expected: 39 new files in the first install; 39 identical on repeat; 11 new upstream variants when explicitly included. Verify counts:

```powershell
(Get-ChildItem "$testConfig\agents" -Filter '*.md' -File).Count
(Get-ChildItem "$testConfig\commands\sc" -Filter '*.md' -File).Count
```

Expected: `20` and `30` after the opt-in variant run. The custom `diagram-architect.md` and Ardizuo command are delivered by the separate original asset installer.

**Never apply to your real `~/.claude` to resolve conflicts.** This checks no live dashboard files, plugin credentials or vault notes. Does not install skill dependencies or the upstream SuperClaude executable.

After reviewing the test logs and staged changes:

```powershell
git diff --check
git status
```

Stop and send the output before committing if anything fails.
