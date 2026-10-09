# <img src="../assets/lucide/circle-help.svg" width="18" height="18" alt="" /> Windows installation scenario playbook

Choose your situation first. All terminal examples are **PowerShell**, executed from the repository root. **Preview flags do not modify files** unless otherwise documented. Never publish `settings.json`, `.claude.json`, GitHub OAuth files, vault notes or raw MCP URLs with keys.

## <img src="../assets/lucide/download.svg" width="18" height="18" alt="" /> Fresh Windows user, no Claude Code yet

1. Install Git, Node.js/npm, Python, Claude Code and (as needed) uvx, Docker and GitHub CLI from the linked [prerequisites](../prerequisites.md).
2. Clone this repository; run `python .\scripts\release-audit.py` to see default and missing capabilities **before** making changes.
3. Run `./scripts/install-all.ps1 -All` to preview local files and external actions. Read every install step before approval.
4. Stage **local definitions only** in an isolated test configuration:

```powershell
$test = Join-Path $HOME 'Documents/Ardizuo-Install-Audit-Test'
if (Test-Path $test) { throw 'Choose a new, empty test folder.' }
.\scripts\install-all.ps1 -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks
.\scripts\install-all.ps1 -Apply -ConfigDir $test -PinnedSuperClaude -PinnedSkills -Hooks
python .\scripts\release-audit.py
python .\scripts\verify-installed-layers.py --config-dir $test --require-hooks --strict-local
```

5. Connect optional plugin/MCP providers on **your own Claude user account**, with the smallest permissions required. Do not copy someone else's authorization files. Test each service before marking it working.
6. Use the [dashboard rehearsal](../../dashboard/claude-map/README.md) and an empty vault folder if those layers are desired. A complete new-user validation should include a real code task, not just filenames.

## <img src="../assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Existing user with personal rules, customizations and secrets

Do **not** force-overwrite your `.claude` files or run `-Apply -All` merely to get a success badge. First, run the offline inventory, make a private backup, and preview in an isolated directory. New `CLAUDE.md`, rule, icon, hook or template files are **create-only**. If there is a conflict, stop and manually merge after reading a diff.

```powershell
.\scripts\doctor.ps1
python .\scripts\coverage-doctor.py --strict
python .\scripts\release-audit.py
.\scripts\install-all.ps1
```

Seven local Ardizuo definition files on the reference machine differ from the currently published source. Do not replace them without understanding their changes. See [private source review](./private-source-migration.md).

## <img src="../assets/lucide/plug.svg" width="18" height="18" alt="" /> Optional Atlassian sign-in or provider downtime

You can keep the Atlassian plugin enabled while deferring its remote MCP authentication. This doesn't prevent local agents, skills, hooks, or the nine separately registered target MCP servers from being installed. Note the limitation in a status report and verify any provider you **do** want to use from within Claude Code `/mcp`.

## <img src="../assets/lucide/wrench.svg" width="18" height="18" alt="" /> Hash mismatch, offline download, or conflicting skill

A hash mismatch stops the pinned installer **before writing its batch**. If offline, defer external steps: packaged original assets still install locally, but publisher-sourced files require a trusted download. For a conflicting skill, don't delete it; inspect the local file, the upstream source, and any required sidecars. Enable the upstream variant only if you want that **different** implementation.

## <img src="../assets/lucide/monitor.svg" width="18" height="18" alt="" /> Dashboard already customized or port 8888 in use

Do not reinstall the global npm `claude-map` package into a customized live installation without a backup. Use `python .\scripts\install-dashboard.py --rehearse` first; it copies files into temporary storage. An upstream compatibility pass does not verify the actual browser UI. If the port is busy, stop or reconfigure the existing process rather than binding to an untrusted network interface.

## <img src="../assets/lucide/notebook-pen.svg" width="18" height="18" alt="" /> Obsidian vault, note consent or template conflict

Supply your vault path explicitly on a new machine. Four templates and the local icon assets are installed create-only. A different existing template is treated as a conflict. The vault-learning skill proposes note content and **asks before writing**; no private notes are copied from the author's device.

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Reporting your result accurately

Record at least these columns: **asset installed**, **registration present**, **provider connected**, **task executed**, and **verified clean-device reproduction**. Use [the reproducibility matrix](./reproducibility-matrix.md) as the release contract; do not turn an offline inventory match into a claim of working authentication.


## <img src="../assets/lucide/search-check.svg" width="18" height="18" alt="" /> Validate exactly what the installed package supplied

After an isolated install, use `python .\scripts\verify-installed-layers.py --config-dir $test --json`. Its missing-file list includes only items selected in the **default** package, not unapproved or missing personal skills. Add `--upstream-variants` when you explicitly installed both sets of publisher versions. Use the [deployed-layer audit guide](./installed-layer-audit.md) before interpreting the results.
