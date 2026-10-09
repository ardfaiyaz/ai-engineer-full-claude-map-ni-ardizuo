# Claude Map Windows preview compatibility fix

Fixes `python scripts/install-dashboard.py` failing on Windows with `[WinError 2]` when trying to run `npm` instead of `npm.cmd`.

Includes a safe read-only initial scaffold-compatibility preflight. That check does **not** verify the remaining overlay stages. It does not authorize blindly applying patches to an existing customized installation.

## Apply to the existing main checkout (only on a clean working tree)

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
git status
Expand-Archive -LiteralPath "$HOME\Downloads\Ardizuo-Claude-Map-Windows-Preview-Fix.zip" -DestinationPath (Get-Location).Path -Force
python -m unittest discover -s tests -v
python .\scripts\install-dashboard.py
```

Expected in our test suite: **28 tests / OK**. The real preview on your PC should find your global `claude-map` path automatically. If not, run the explicit override:

```powershell
$mapRoot = Join-Path ((npm root -g).Trim()) 'claude-map'
python .\scripts\install-dashboard.py --map-root "$mapRoot"
```

Do not use `--apply` before reviewing compatibility of all five stages with the actual installed source. When this is confirmed, stage and review changes and commit to main.

### Safety and provenance

This ZIP includes 3 edited/added project files plus this README. It does not include provider credentials, private notes, installed third-party code or cached plugins. On a fresh Windows machine, npm installation may still require admin rights or permissions depending on user setup. Later patch stages may create a missing diagram agent, so dashboard-only users should not run the complete patch without inspecting side effects.
