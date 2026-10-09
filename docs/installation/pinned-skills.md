# <img src="../assets/lucide/blocks.svg" width="18" height="18" alt="" /> Publisher-pinned skill prompts — Sprint 4

This is the **skill source** counterpart to the [pinned SuperClaude agent/command installer](./pinned-superclaude.md). Files are downloaded from **immutable upstream GitHub commits** and checked against upstream Git blob SHA-1. They are **not bundled** in this public repository. Publisher license and attribution remain with their owners.

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> Verified source coverage

The author compared all 29 third-party skill definitions against pinned publisher sources in two rounds. Together the reviews establish:

| Source comparison | Count | Public installer policy |
| --- | ---: | --- |
| Exact byte match | 5 | Safe default pinned file install |
| Same content, CRLF/LF line endings only | 15 | Safe default pinned file install; does not overwrite local CRLF copies |
| Different from publisher original | 5 | Opt-in *publisher* versions; **not** the author's customized copies |
| Still unmapped | 4 | Excluded until a trustworthy original source is identified |

By default, `install-pinned-skills.py` installs **20** source-matched `SKILL.md` definitions. This includes the 8 previously pinned skills and 12 newly matched skills, such as Animate, Animation Vocabulary, Apple Design, Emil Design Eng, CI/CD and Automation, and Vercel React Best Practices. The **five opt-in publisher variants** are Impeccable, Supabase, Accessibility Audit, Accessibility Fix, and Playwright Best Practices. Four skills remain excluded.

> **Skill functionality:** This installer currently downloads **SKILL.md only**, not sibling scripts, images, reference files, templates or CLIs. Some skill prompts reference these dependencies and may be unusable without following the publisher's full setup. A successful install verifies source text and file presence, **not operational completeness**. Check each skill's official README and do a real Claude Code invocation.

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Windows — isolated config first

```powershell
cd "$HOME\Documents\ai-engineer-full-claude-map-ni-ardizuo"
$testConfig = "$HOME\Documents\Ardizuo-Pinned-Skills-Sprint4-Test"
if (Test-Path $testConfig) { throw "Choose an unused isolated test folder" }

# Offline dry run (does not create folders or download files)
python .\scripts\install-pinned-skills.py --config-dir "$testConfig"

# Explicitly download pinned publisher files and create files only
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig"

# A second run verifies idempotence with no downloads when identical
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig"

# Optional: publisher versions of five author-modified definitions
python .\scripts\install-pinned-skills.py --config-dir "$testConfig" --upstream-variants
python .\scripts\install-pinned-skills.py --apply --config-dir "$testConfig" --upstream-variants
```

The five optional upstream versions **differ** from the author's original skill content. This difference is intentional. The program refuses to replace any existing conflicting files.

## <img src="../assets/lucide/plug.svg" width="18" height="18" alt="" /> Unified installer integration

Both the pinned SuperClaude and pinned skills installers can be called in a **single isolated** setup, along with Ardizuo-owned local assets:

```powershell
$allTest = "$HOME\Documents\Ardizuo-Pinned-Combined-Test"
if (Test-Path $allTest) { throw "Choose a fresh test folder" }

.\scripts\install-all.ps1 -ConfigDir $allTest -PinnedSuperClaude -PinnedSkills
.\scripts\install-all.ps1 -Apply -ConfigDir $allTest -PinnedSuperClaude -PinnedSkills
```

`-SkillUpstreamVariants` is optional and requires `-PinnedSkills`; `-UpstreamVariants` applies **only** to the 11 differing SuperClaude commands and requires `-PinnedSuperClaude`. In the public `-All` flow, the pinned definitions are selected by default instead of silently running a new, unpinned SuperClaude CLI installer. Other third-party installers, plugins and MCPs still require their own permissions and may need account sign-in; the same user cannot safely isolate all of them using `-ConfigDir -All -Apply`.

## <img src="../assets/lucide/blocks.svg" width="18" height="18" alt="" /> Compare 19 previously unverified private skills without uploading contents

A historical public-source lead list is stored at `setup/skill-source-candidates.json`: **All 15** public source paths have now been compared locally with the author’s private definitions: **12 matched content, 3 differed**. The 12 content matches are included in the default pinned installer, and the 3 differing publisher variants are explicitly opt-in. The **four unidentified skills remain excluded**. The lead manifest remains a historical review list; the source-provenance lock is the authoritative install policy.

```powershell
# Preview: no private reads, network, or output file
python .\scripts\verify-remaining-skill-sources.py

# Compare on your local PC, public sources only fetched via HTTPS.
# The report contains names and statuses, never private text or hashes.
python .\scripts\verify-remaining-skill-sources.py --compare `
  --private-root "$HOME\Documents\Ardizuo-Additional-Assets-PRIVATE" `
  --output "$HOME\Documents\Ardizuo-Remaining-Skill-Comparison.csv"
```

**Only upload the reviewed status CSV**, not the private skills folder. `EXACT_BYTE_MATCH` and `TEXT_MATCH_LINE_ENDINGS_ONLY` establish that the proposed public source matches the user's local text, but do not in themselves establish copyright ownership, redistribute rights or complete skill dependency installation. Any source promotion needs manual review, license attribution, manifest update, and tests.

## <img src="../assets/lucide/shield-check.svg" width="18" height="18" alt="" /> Security and compatibility

- All default planning commands are offline and read-only.
- `--apply` requests public downloads, verifies every downloaded Git blob checksum **before any files are written**, and aborts on conflicts. It never overwrites existing files.
- A local copy using different line endings is *not* overwritten or quietly accepted as source-identical; choose a fresh test directory.
- Git SHA-1 objects are version pins but not a full software supply-chain security attestation.
- Do not store personal `.claude.json`, `settings.json`, token values, vault notes, or private skill contents in your public Git repository.

[Exact reference coverage](../components/exact-coverage.md) · [Source migration](./private-source-migration.md) · [Third-party notices](../../THIRD_PARTY_NOTICES.md)
