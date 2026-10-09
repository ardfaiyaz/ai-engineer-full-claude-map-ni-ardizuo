# 🛠️ fix-build

**Purpose:** Diagnose actual build failures and verify fixes.

**Source:** Original Ardizuo local skill, included in `ardizuo-plugin/skills/fix-build/SKILL.md`. This is not claimed to be the identically named skill from another author.

<br />

## 📥 Install

From the cloned repository, preview or apply the entire reviewed development pack:

```powershell
.\scripts\install-all.ps1  # Preview
.\scripts\install-all.ps1 -Apply  # After review
```

The skill is installed globally under the current user's Claude configuration directory (respects `CLAUDE_CONFIG_DIR`). If a different file already exists, installation stops without overwriting it.

<br />

## ☑️ Verify and use

Inside Claude Code, check `/skills` and invoke the available skill manually when appropriate. Read the source `SKILL.md` for exact instructions; manual-only skills are not automatically run by merely installing them.

**Prerequisites:** Claude Code and its existing project tooling. No additional API key is required for this local file.

<br />

## 🛠️ Troubleshooting and removal

If missing, check `<ClaudeConfig>/skills/fix-build/SKILL.md`, restart Claude Code and run `python scripts/verify-all.py`. For removal, back up and remove only the specific installed skill folder; do not delete other users' skills or plugin caches.

[All components](../README.md) · [Full installer](../../installation/full-setup.md)
