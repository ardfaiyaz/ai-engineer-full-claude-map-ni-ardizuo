# 📄 Reproducible, pinned SuperClaude definitions (Sprint 2)

This installer lets a Windows user install **20 upstream agents and 19 upstream commands** matched byte-for-byte against the author's reference files. It is separate from `pipx install superclaude` and does not claim to install the SuperClaude executable, modes or MCP integrations. The author also has **11 locally different SuperClaude commands**; a clean machine can opt into their *publisher originals*, but these will not reproduce the author's modified text.

> Source: [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) under MIT. Pinned commit: `fe68862c8ed9e2afb8120c2d9e27d0c3a7ce73a2`. The JSON file `setup/source-provenance-lock.json` records each source file and its Git blob checksum. It includes no author-private files, hashes of private modified files, keys or vault notes.

## ⚙️ Windows — start in a disposable configuration

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
$testConfig = "$HOME\Documents\Ardizuo-Pinned-SuperClaude-Test"
if (Test-Path $testConfig) { throw "Use a fresh test config path" }

# No downloads and no writes in preview.
python .\scripts\install-pinned-superclaude.py --config-dir "$testConfig"

# Explicit consent: fetch pinned public sources, checksum-check, create-only.
python .\scripts\install-pinned-superclaude.py --apply --config-dir "$testConfig"

# Rerunning makes no network requests when files are identical.
python .\scripts\install-pinned-superclaude.py --apply --config-dir "$testConfig"
```

To include **all 30 upstream commands** (11 were different on the author's machine), first preview, then opt into a *different upstream version* of those eleven files:

```powershell
python .\scripts\install-pinned-superclaude.py --config-dir "$testConfig" --upstream-variants
python .\scripts\install-pinned-superclaude.py --apply --config-dir "$testConfig" --upstream-variants
```

This yields 20 agents plus 30 upstream commands on a clean target. The Ardizuo-owned diagram agent and log-to-vault command are installed separately with `install-all.ps1`.

**Do not point this at your real `.claude` directory to resolve conflicts.** Any existing file that differs triggers a stop *before downloads or writes*; it is never overwritten, deleted, or merged.

You can also invoke this mode through the main installer:

```powershell
.\scripts\install-all.ps1 -ConfigDir "$testConfig" -PinnedSuperClaude
.\scripts\install-all.ps1 -Apply -ConfigDir "$testConfig" -PinnedSuperClaude
# Optional: -UpstreamVariants
```

Don't combine `-PinnedSuperClaude` and `-SuperClaude` in one call. `-All` now prefers pinned SuperClaude **file definitions** and eight publisher-pinned skill prompts; the upstream SuperClaude CLI is an explicit alternative via `-SuperClaude`. The pin is for static files, not full SuperClaude CLI functionality.

## 📖 What is and is not proven

- `EXACT_BYTE_MATCH`: 20 agent files and 19 actual command definitions in the default pinned installer. The upstream command directory's `README.md` is documentation, not a command.
- `DIFFERENT_CONTENT`: 11 additional SuperClaude command files. They are installed only with `--upstream-variants`, and the public upstream versions may not behave identically to the author's local changes.
- 29 skill candidates are tracked in the source lock. The separate [pinned skills installer](./pinned-skills.md) now installs 8 matched publisher SKILL.md files; 2 modified source variants are opt-in and 19 remain excluded pending private source comparison. Sidecar scripts/data require separate verification.
- An installed definition is **not** an executed agent, and this installer does not attest to Claude Code recognizing every slash command. Verify `claude --version`, `/agents`, `/skills`, and actual delegated tasks in Claude Code.
- Downloads use HTTPS from the upstream publisher at a full commit ID and are checked against recorded Git blob object SHA-1 values. This relies on Git's SHA-1 object scheme, and is not a complete supply-chain audit. **No third-party source is copied into Ardizuo's public repository.**

[Exact coverage](../components/exact-coverage.md) · [SuperClaude upstream setup](./superclaude.md) · [Third-party notices](../../THIRD_PARTY_NOTICES.md)
