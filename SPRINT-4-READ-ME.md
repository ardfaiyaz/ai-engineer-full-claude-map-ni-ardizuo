# <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Ardizuo Completion Sprint 4 — extended pinned skills

This ZIP updates the Sprint 3 repository. It contains **no private skill contents**, secrets, cached plugins or vault data. The user’s reviewed CSV established 3 exact matches, 9 line-ending-only matches, 3 changed variants, and 4 unknown sources.

## <img src="docs/assets/lucide/terminal.svg" width="18" height="18" alt="" /> Run on Windows (PowerShell)

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
Expand-Archive -LiteralPath "$HOME\Downloads\Ardizuo-Extended-Pinned-Skills-Sprint-4-UPDATE.zip" -DestinationPath (Get-Location).Path -Force
python -m unittest discover -s tests -v
$testConfig="$HOME\Documents\Ardizuo-Pinned-Skills-Sprint4-Test"
if (Test-Path $testConfig) { throw 'Choose a fresh directory for the test' }
python .\scripts\install-pinned-skills.py --config-dir "$testConfig"
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig"
(Get-ChildItem "$testConfig\skills" -Directory).Count # expected 20
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig" --upstream-variants
(Get-ChildItem "$testConfig\skills" -Directory).Count # expected 25
```

Do not install against real `~/.claude` yet. For combined isolated validation use `-PinnedSuperClaude -PinnedSkills`, and observe that all stages remain non-overwriting. Four unidentified skills and sidecars still require work before a v1.0 release.
