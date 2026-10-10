# 🔎 Identify your exact installed skills without publishing private files


**Purpose:** close the gap between the 62 direct `SKILL.md` definitions on the reference machine and the smaller set a new user can obtain from the GitHub installer. This is **source verification**, not a new skill or plugin. Nothing gets installed or modified in Claude Code.


## 🗂️ What is already reproduced versus unresolved


| Category | Names | How it is handled |
| :-- | --: | :-- |
| Reviewed Ardizuo skills | 16 | Bundled, non-overwriting |
| Exact/text-equivalent third-party skills | 20 | Pinned public upstream installer |
| Different-from-local publisher versions | 5 | Explicit opt-in, **not** an exact clone |
| Other direct-source skills | 17 | Local provenance audit; installation **not** approved yet |
| Unknown-origin skills | 4 | Must be traced to original source before public installation |
| **Total** | **62** | Source availability does not imply sidecars or actual execution |

The **17 external/unverified** names and **four unknown-origin** names are already part of your reference machine. This script does not invent or install replacements. Plugin-cached skills are not counted as direct-scope definitions.


## 💻 Windows: preview before using the network


From the repository root:

```powershell
python .\scripts\review-exact-local-components.py
```

The preview reads the **62 direct skill entrypoints** in your existing `~/.claude/skills` directory. It reports only names, whether each `SKILL.md` exists, counts of additional files, counts of relative path references, and source candidates. It compares the seven previously customized Ardizuo files by status only; it does **not** print their contents, read `.claude.json`/`settings.json`, inspect transcripts, or walk plugin caches and vault notes. No report file or network request is made by default.

To check the six public publisher candidates on your own machine and save the **metadata-only** report privately:

```powershell
$report = "$HOME\Documents\Ardizuo-Exact-Local-Review-$(Get-Date -Format yyyyMMdd-HHmmss).json"

python .\scripts\review-exact-local-components.py `
  --compare-public `
  --output $report

# Inspect metadata and redact anything you'd rather not share before uploading.
code $report
```

The command makes **GET requests only for pinned public** `SKILL.md` files at `raw.githubusercontent.com`; it does **not send local file bytes**. Every downloaded public file must match its pinned Git blob checksum. A public mismatch or network problem is recorded as `DOWNLOAD_OR_CHECKSUM_FAILURE`, **not** as a match. The JSON file is created once in Documents and will not overwrite an existing file. Do not save the report inside the public repository.


## 📖 Six current publisher leads


These already exist as direct skill names in your Claude configuration, but their origin remains **unconfirmed until your local comparison is run**.

| Direct skill | Candidate publisher | Included supporting files? |
| :-- | :-- | :-- |
| `deep-research` | SuperClaude Framework | **Not yet verified** |
| `docx` | Anthropic official skill source | **Not yet verified** |
| `pdf` | Anthropic official skill source | **Not yet verified** |
| `pptx` | Anthropic official skill source | **Not yet verified** |
| `xlsx` | Anthropic official skill source | **Not yet verified** |
| `skill-creator` | Anthropic official skill source | **Not yet verified** |

All six are pinned to immutable upstream revisions in [`setup/direct-skill-origin-candidates.json`](../../setup/direct-skill-origin-candidates.json). Neither that manifest nor this checker installs or republishes them. Some official document skills include **numerous scripts, templates and/or other files**; matching the instruction file alone is not sufficient to declare them operational on a fresh Windows installation.

The other **11 external** skills remain unmapped to a reliable original source; the four unknown-source skills still remain unknown. Neither a matching name in a random GitHub repository nor a copied cached plugin definition constitutes proof of origin.


## 📄 Understand the report


| Status | Meaning | Next action |
| :-- | :-- | :-- |
| `EXACT_BYTE_MATCH` | Your local `SKILL.md` matches the publisher's pinned bytes | Investigate sidecars and license before an installer change |
| `TEXT_MATCH_LINE_ENDINGS_ONLY` | Difference is CRLF vs LF | Treat as source-identical text, but preserve file-format differences when needed |
| `DIFFERENT_CONTENT` | Your installed skill contains modifications or a different version | Keep it; review the difference privately, don't silently replace it |
| `MISSING_LOCAL` | The reference skill's `SKILL.md` is missing | Confirm your global config path; do not claim coverage |
| `NO_APPROVED_SOURCE_CANDIDATE` | No trusted publisher path known | Manual source investigation required |
| `DOWNLOAD_OR_CHECKSUM_FAILURE` | Source could not be validated | Retry network or examine upstream version; **never auto-trust** |

`supportingFileCount` counts non-entrypoint files inside that skill folder, skipping symlinks/junctions and large irrelevant cache folders. `relativeReferenceHints`, `referenceHintsWithFiles` and `unresolvedReferenceHints` are **heuristic** indicators from textual references such as `scripts/...` or `references/...`; these aren't guaranteed runtime dependencies. Counts above 2,000 are capped and marked accordingly. No supporting file content or filenames appear in the report.


## 🛡️ Publishing and exact reproduction


When the local results are available, promotion should happen in this order: confirm the true publisher/revision; inspect license and any special per-skill terms; compare your local bytes; audit required scripts/assets and prerequisites; add **only an allowed upstream installation method**; test in an empty Claude config; finally test one real task. Locally customized or original files need separate review and explicit approval, not forced overwrites.

The seven earlier differing Ardizuo sources are also reported under `customizedArdizuoFiles`. A status of `DIFFERENT_FROM_PACKAGE` only means the existing local file differs. It does not prove that the private version is safe, original, or better.

Do **not** commit your `~/.claude` contents, raw private source exports, plugin caches, private vault notes, credentials, tokens, provider configuration, or generated local reports. Atlassian plugin sign-in is optional and not a release blocker for these local-source checks.

[Public reproducibility matrix](./reproducibility-matrix.md) · [Private source review](./private-source-migration.md) · [Installed-layer audit](./installed-layer-audit.md) · [Security](../../SECURITY.md)
