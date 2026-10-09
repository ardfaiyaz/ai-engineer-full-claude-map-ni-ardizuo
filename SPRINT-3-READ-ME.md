# <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Completion Sprint 3 — pinned skill sources

**Apply to a copy of the repository from Sprint 2, not into your `.claude` directory.** The update changes Python/PowerShell installers, adds a public 29-skill source lock and 19 pending-source leads, and includes tests/docs. It does not contain your private exported skills, API keys or Obsidian data.

## <img src="docs/assets/lucide/download.svg" width="18" height="18" alt="" /> Install this UPDATE ZIP over the repository

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
Expand-Archive -LiteralPath "$HOME\Downloads\Ardizuo-Pinned-Skills-Sprint-3-UPDATE.zip" -DestinationPath (Get-Location).Path -Force
python -m unittest discover -s tests -v
```

Expected **52 passing unit tests** on the staged Sprint 3 package. These are structural/injected-fake-network tests, not proof of live publisher availability.

## <img src="docs/assets/lucide/blocks.svg" width="18" height="18" alt="" /> Dry-run, then install 8 source-matched SKILL.md files in a disposable config

```powershell
$testConfig="$HOME\Documents\Ardizuo-Pinned-Skills-Sprint3-Test"
if (Test-Path $testConfig) { throw 'Use a fresh test path' }
python .\scripts\install-pinned-skills.py --config-dir "$testConfig"
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig"
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig"
(Get-ChildItem "$testConfig\skills" -Directory).Count
```

Expected `8` directories (one SKILL.md per selected skill). Live HTTPS access and publisher content consistency are tested by this step. Existing live `.claude` files are untouched.

## <img src="docs/assets/lucide/folder-open.svg" width="18" height="18" alt="" /> Next: compare the other 19 sources privately

```powershell
python .\scripts\verify-remaining-skill-sources.py
python .\scripts\verify-remaining-skill-sources.py --compare `
  --private-root "$HOME\Documents\Ardizuo-Additional-Assets-PRIVATE" `
  --output "$HOME\Documents\Ardizuo-Remaining-Skill-Comparison.csv"
```

Share only the **reviewed CSV** to promote sources in a subsequent update. Four remain unknown. For full clean installs, skill sidecars, real execution, global configuration and workflows still need verification; don't label this a finished v1.0.

[Full instructions](docs/installation/pinned-skills.md)
