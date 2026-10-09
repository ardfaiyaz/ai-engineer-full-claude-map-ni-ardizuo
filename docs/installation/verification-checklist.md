# 📥 Full setup verification checklist

**Run these checks on a clean Windows user or disposable test configuration before calling the installer complete.** A displayed skill or green dashboard badge is not proof of execution.

<br />

## 📄 1. Prepare the computer

- [ ] Check Windows version and PowerShell version.
- [ ] Install Claude Code, Git, Python and Node/npm from official sources.
- [ ] Install optional uvx, gh and Docker if those modules are selected.
- [ ] Run `scripts/doctor.ps1` and review all missing tools.

<br />

## 📥 2. Install original development assets

- [ ] Run `scripts/install-all.ps1 -All` as a dry run.
- [ ] Copy 28 custom files into a disposable `-ConfigDir` and verify identical checksums.
- [ ] Re-run the installer: identical files should be skipped.
- [ ] Introduce a different existing file: installer should refuse overwriting.

<br />

## 🧩 3. Framework and plugins

- [ ] Confirm SuperClaude agent/command framework is present.
- [ ] Verify all 21 global agent names from the reference inventory.
- [ ] Check `sc:research` and other required global command names.
- [ ] Verify 12 plugin IDs in `claude plugin list` (where marketplace registration permits).
- [ ] Confirm Ralph PRD and Superpowers skill discovery in `/skills`.
- [ ] Confirm optional Expo, Stripe, Sentry, Atlassian and Notion provider skills are enabled as intended.

<br />

## 🛡️ 4. MCP registrations and credentials

- [ ] Confirm Serena, Sequential Thinking and Chrome DevTools MCP registration.
- [ ] Confirm Supabase, Figma and Vercel MCP registration.
- [ ] Complete Tavily authentication and verify it works.
- [ ] Complete Morph authentication and verify it works.
- [ ] Complete GitHub MCP authentication with appropriately limited permissions.
- [ ] Inspect `/mcp` and document actual **Connected** statuses, not just registrations.

<br />

## 🔄 5. Hooks, configuration and memory

- [ ] Register all five hooks without removing existing entries.
- [ ] Confirm hook scripts resolve `hooks/lib/common.mjs`.
- [ ] Confirm `skill-gates.json` and workflow/mandate rule files are loaded.
- [ ] Create/open optional Obsidian vault folders and templates.
- [ ] Test one note save only after approval and reload that note in a new session.

<br />

## 🖥️ 6. Dashboard and end-to-end operation

- [ ] Install upstream Claude Map and verify the localhost dashboard.
- [ ] Apply the Ardizuo Development Hub overlay with backups and syntax checks.
- [ ] Test agent delegation, test/lint/build evidence, Ship preflight and honest negative statuses.
- [ ] Complete security, rollback, licensing and clean-Windows release checks.

**Not all 30 steps are fully automated**; account authentication and real development execution require user approval. See [Full guide](./full-setup.md) and [release gates](../release-checklist.md).


## 🧩 7. Exact-name and marketplace release gates

- [ ] All four declared plugin marketplace sources are reviewed and registered (Anthropic official, Anthropic skills, Ralph and Morph).
- [ ] `python scripts/coverage-doctor.py --strict` returns success on the **target installed user** only after the literal names are present.
- [ ] Cached-only skills are not counted as enabled; the operator has verified individual plugin enablement in Claude.
- [ ] GitHub MCP uses the approved Docker OAuth launch flow and the user has completed browser consent.
- [ ] Four Obsidian templates are present in the selected vault; a customized preexisting template is never overwritten.
- [ ] Every remaining locally customized third-party agent/skill/command has documented source and redistribution permission; otherwise install from official upstream.
- [ ] No `settings.json`, `.claude.json`, token, session log, plugin cache or private vault note is included in the release.

[See the offline exact-coverage audit](../components/exact-coverage.md). These tests intentionally do not claim that a real OAuth connection or delegated agent ran.


<br />

## 🖥️ Full Claude Map overlay rehearsal

The initial dashboard preview checks only scaffold anchors. Before using
`--apply`, rehearse **all five** overlay stages against an unmodified official
Claude Map archive as explained in [the dashboard setup](../../dashboard/claude-map/README.md).

```powershell
python .\scripts\install-dashboard.py --rehearse
```

The rehearsal redirects patch-created files into temporary private folders.
Record all failed stages and do not infer browser/runtime compatibility from
JavaScript syntax checks alone.


## 📄 Sprint 4 verification

Run `python -m unittest discover -s tests -v`, then test the **20 default publisher skills** in a disposable config via `python .\scripts\install-pinned-skills.py --apply --config-dir $testConfig`. Confirm `20` skill subdirectories. The five differing upstream variants are opt-in, and the four unknown-source skills must remain absent. Inspect each installed skill for references to sibling scripts/data; `SKILL.md` alone is not a complete skill package.


## 🔎 Verify the exact reference skills and support files

Run `python .\scripts\review-exact-local-components.py` from the repository root before declaring your 62 direct skill definitions reproducible. For six existing source candidates, use `--compare-public` and a private `--output` path as described in the [exact-source guide](./exact-local-origin-review.md). Inspect missing sidecars, source differences and unknown origins; do not treat the resulting counts as proof of skill execution or permission to redistribute private files.
