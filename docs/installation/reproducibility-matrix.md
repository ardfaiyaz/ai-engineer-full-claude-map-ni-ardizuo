# ☑️ Reproducibility matrix — GitHub package vs. live Claude Code


**Last checked:** 2026-10-10 · **Scope:** Public repository, Windows PowerShell install guide and portable output. This page does **not** contain your existing Claude credentials, private notes or plugin caches.

> **Release decision: not yet a complete clone.** Your live machine's coverage can be 100% while a new user's **package reproducibility** is still partial. A successfully installed `.md` file does not prove its tools ran. One optional Atlassian plugin MCP login is intentionally nonblocking.


<br />
<br />


## ☑️ At a glance


| Layer | Existing reference machine | Public package / guided installer | Still required on a fresh machine |
|---|---|---|---|
| **Agents** | 21 direct agents present | **21/21** definitions: one original + 20 pinned SuperClaude | Real delegation test |
| **Direct skills** | 62/62 files present | **36/62 default** (16 local + 20 pinned); **41/62** if five upstream variants are opted into | Four unknown sources, 17 external direct definitions, skill sidecar files, task invocations |
| **Executable commands** | **31** executable `.md` files plus one `README.md` | **20/31 default**, **31/31** using 11 opt-in *upstream* versions | Actual slash commands, decide whether upstream versions replace reference customizations |
| **Plugins** | 12/12 enabled | 12 exact plugin identifiers and four marketplaces in manifest/guides; optional external CLI installer | Fresh install/enabled checks; individual provider grants where desired |
| **Target MCPs** | Nine of nine connected on latest local check | Nine named registrations documented; supported CLI flows provided, credential-dependent steps remain guided | Actual OAuth/API key setup and one permitted tool call each |
| **Extra plugin MCPs** | Playwright, Context7, Expo, Stripe, Sentry, Notion connected; Atlassian needs auth | Installed through corresponding plugin, not counted among nine target servers | Atlassian sign-in **optional and deferred** |
| **Hooks** | Five scripts; expected four event groups | Five scripts + shared helper bundled; `-Hooks` registers their handlers | Actual lifecycle execution, approvals, safe vault behavior |
| **Global context** | Source rule not fully aligned; seven local asset variations | Portable `CLAUDE.md` and base/orchestration rules are included in this update | Existing user's `CLAUDE.md` preserved on conflict; verify real rule loading |
| **Workflow layers** | Dashboard shows five phases | Triage → Contract → Dispatch → Review → Ship documents/rules + custom dashboard overlay | Verify actual guided use and results in a non-sensitive task |
| **Obsidian** | Eight folders; four templates absent in prior live audit | Eight folders + four Markdown templates + emojis via opt-in `-Vault` | Chosen vault folder, approvals, note write/read test |
| **Claude Map** | Live customized 1.2.3 reported working | Installer, five-stage patch rehearsal, version-sensitive overlay | Clean machine browser check; do not overwrite working custom package blindly |
| **Recovery and security** | Existing personal configuration must be protected | Preview, conflict refusal, limited backups and tests | Full per-provider rollback / fresh-machine signoff still incomplete |


<br />
<br />


## 📥 How to install without replacing your working configuration


**Scenario A — You are new to Claude Code:** Clone this repository, read [full setup](./full-setup.md), run `python .\scripts\release-audit.py`, preview `./scripts/install-all.ps1 -All`, and test the static portion with `-ConfigDir` before consenting to real plugins, MCPs, hooks, vault, or dashboard writes. Commands in this guide are Windows PowerShell commands.

**Scenario B — You already have a customized Claude configuration:** Back up the original config privately and run a **preview first**. Existing files are never overwritten by the pinned installers. An existing global `CLAUDE.md` or an altered original definition creates a conflict that requires manual reconciliation, not a force install.

**Scenario C — You do not want Atlassian authentication:** Leave it disconnected. Claude CLI currently reports all nine target MCP servers connected and the other six plugin MCPs connected on the reference machine; optional Atlassian sign-in is **not** a release gate. No OAuth tokens are stored in this repo.

**Scenario D — You want exact byte-identical reference customizations:** Do not enable `-UpstreamVariants` or `-SkillUpstreamVariants` as a substitute for the author's modified files. Those flags install publicly available publisher versions; your actual personal variants require ownership, licensing and privacy review before any public redistribution.


<br />
<br />


## ☑️ All 62 direct skill names — installability


<details><summary><strong>Expand the complete skill-by-skill table</strong></summary>

| Skill | Public installation status |
|---|---|
| `Accessibility` | Documented; original direct-source reproduction unverified |
| `accessibility-audit` | Opt-in upstream variant (`-SkillUpstreamVariants`), not exact reference |
| `accessibility-diff` | Blocked: source / redistribution not established |
| `accessibility-fix` | Opt-in upstream variant (`-SkillUpstreamVariants`), not exact reference |
| `accessibility-inspect` | Blocked: source / redistribution not established |
| `accessibility-scan` | Blocked: source / redistribution not established |
| `animate` | Publisher pinned (`-PinnedSkills`) |
| `animation-vocabulary` | Publisher pinned (`-PinnedSkills`) |
| `apple-design` | Publisher pinned (`-PinnedSkills`) |
| `bencium-innovative-ux-designer` | Publisher pinned (`-PinnedSkills`) |
| `built-in-browser` | Documented; original direct-source reproduction unverified |
| `chrome-browser` | Documented; original direct-source reproduction unverified |
| `ci-cd-and-automation` | Publisher pinned (`-PinnedSkills`) |
| `claude-md-management` | Bundled original (`-Apply`) |
| `clean-code-typescript` | Bundled original (`-Apply`) |
| `code-splitting` | Bundled original (`-Apply`) |
| `computer-use` | Documented; original direct-source reproduction unverified |
| `dead-code-scan` | Bundled original (`-Apply`) |
| `deep-research` | Documented; original direct-source reproduction unverified |
| `design` | Publisher pinned (`-PinnedSkills`) |
| `design-system` | Publisher pinned (`-PinnedSkills`) |
| `docs` | Documented; original direct-source reproduction unverified |
| `docx` | Documented; original direct-source reproduction unverified |
| `emil-design-eng` | Publisher pinned (`-PinnedSkills`) |
| `Engineering` | Documented; original direct-source reproduction unverified |
| `find-animation-opportunities` | Publisher pinned (`-PinnedSkills`) |
| `find-skills` | Publisher pinned (`-PinnedSkills`) |
| `fix-build` | Bundled original (`-Apply`) |
| `gauge-improvements` | Bundled original (`-Apply`) |
| `google-workspace` | Documented; original direct-source reproduction unverified |
| `humanizer` | Bundled original (`-Apply`) |
| `impeccable` | Opt-in upstream variant (`-SkillUpstreamVariants`), not exact reference |
| `import-memory` | Documented; original direct-source reproduction unverified |
| `improve-animations` | Publisher pinned (`-PinnedSkills`) |
| `morning` | Documented; original direct-source reproduction unverified |
| `owasp-security` | Blocked: source / redistribution not established |
| `pdf` | Documented; original direct-source reproduction unverified |
| `pick-ui-library` | Publisher pinned (`-PinnedSkills`) |
| `playwright-best-practices` | Opt-in upstream variant (`-SkillUpstreamVariants`), not exact reference |
| `pptx` | Documented; original direct-source reproduction unverified |
| `pragmatic-code-guidelines` | Bundled original (`-Apply`) |
| `prototype` | Publisher pinned (`-PinnedSkills`) |
| `react-native-best-practices` | Bundled original (`-Apply`) |
| `reuse-audit` | Bundled original (`-Apply`) |
| `review-animations` | Publisher pinned (`-PinnedSkills`) |
| `root-cause-analysis` | Bundled original (`-Apply`) |
| `ship-learn-next` | Bundled original (`-Apply`) |
| `skill-creator` | Documented; original direct-source reproduction unverified |
| `supabase` | Opt-in upstream variant (`-SkillUpstreamVariants`), not exact reference |
| `supabase-postgres-best-practices` | Publisher pinned (`-PinnedSkills`) |
| `team-driven-development` | Bundled original (`-Apply`) |
| `technical-style-guide` | Bundled original (`-Apply`) |
| `test-fixing` | Bundled original (`-Apply`) |
| `UI` | Documented; original direct-source reproduction unverified |
| `ui-styling` | Publisher pinned (`-PinnedSkills`) |
| `ui-ux-pro-max` | Publisher pinned (`-PinnedSkills`) |
| `UX` | Documented; original direct-source reproduction unverified |
| `vault-learning` | Bundled original (`-Apply`) |
| `vercel-composition-patterns` | Publisher pinned (`-PinnedSkills`) |
| `vercel-react-best-practices` | Publisher pinned (`-PinnedSkills`) |
| `web-design-guidelines` | Publisher pinned (`-PinnedSkills`) |
| `xlsx` | Documented; original direct-source reproduction unverified |

</details>


<br />
<br />


## ☑️ All 32 command Markdown files — 31 executable


<details><summary><strong>Expand command-by-command installation status</strong></summary>

| File name | Public installation status |
|---|---|
| `agent` | Publisher pinned default |
| `analyze` | Publisher pinned default |
| `brainstorm` | Opt-in official publisher variant (not identical to reference) |
| `build` | Publisher pinned default |
| `business-panel` | Publisher pinned default |
| `cleanup` | Opt-in official publisher variant (not identical to reference) |
| `design` | Publisher pinned default |
| `document` | Publisher pinned default |
| `estimate` | Opt-in official publisher variant (not identical to reference) |
| `explain` | Opt-in official publisher variant (not identical to reference) |
| `git` | Publisher pinned default |
| `help` | Publisher pinned default |
| `implement` | Opt-in official publisher variant (not identical to reference) |
| `improve` | Opt-in official publisher variant (not identical to reference) |
| `index` | Opt-in official publisher variant (not identical to reference) |
| `index-repo` | Publisher pinned default |
| `load` | Publisher pinned default |
| `log-to-vault` | Bundled original |
| `pm` | Publisher pinned default |
| `README` | Documentation, **not a command** |
| `recommend` | Opt-in official publisher variant (not identical to reference) |
| `reflect` | Publisher pinned default |
| `research` | Publisher pinned default |
| `save` | Publisher pinned default |
| `sc` | Publisher pinned default |
| `select-tool` | Publisher pinned default |
| `spawn` | Publisher pinned default |
| `spec-panel` | Opt-in official publisher variant (not identical to reference) |
| `task` | Opt-in official publisher variant (not identical to reference) |
| `test` | Publisher pinned default |
| `troubleshoot` | Publisher pinned default |
| `workflow` | Opt-in official publisher variant (not identical to reference) |

</details>


<br />
<br />


## 🔌 All plugins and target MCP registrations


Each plugin has a dedicated [installation page](../../integrations/plugins/README.md) and each MCP has a dedicated [connection page](../../integrations/mcp/README.md). The names below come from the public manifests, **not copied credentials**.

<details><summary><strong>Expand 12 plugins</strong></summary>

| Plugin ID | Installation | Verification |
|---|---|---|
| `playwright@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `context7@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `superpowers@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `document-skills@anthropic-agent-skills` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `example-skills@anthropic-agent-skills` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `morph-compact@morph` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `ralph-skills@ralph-marketplace` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `expo@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `stripe@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `sentry@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `atlassian@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |
| `notion@claude-plugins-official` | Marketplace + opt-in external installer | `claude plugin list`; optional `/mcp` login |

</details>

<details><summary><strong>Expand nine target MCPs</strong></summary>

| MCP | Installation | Verification |
|---|---|---|
| `serena` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `sequential-thinking` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `chrome-devtools` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `tavily` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `morph-mcp` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `supabase` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `figma` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `vercel` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |
| `github` | See its provider guide and the optional `-Mcps -External` route | `claude mcp list`, `/mcp`, permitted tool call |

</details>


<br />
<br />


## 🔄 Hooks, workflow and memory layer


**Hooks:** `skill-gate-check.mjs` (UserPromptSubmit), `vault-session-init.mjs` (SessionStart), `log-to-vault.mjs` and `dead-code-check.mjs` (PostToolUse), `stop-vault-log.mjs` (Stop). The shared `hooks/lib/common.mjs` helper is bundled. Use **`-Hooks`** to register handlers after reviewing the plan and backup.

**Five workflow phases:** Triage → Contract → Dispatch → Review → Ship. The global `CLAUDE.md`, the original orchestration rules and the workflow Markdown define the intention, while tests and real session evidence determine whether a phase was actually carried out.

**Obsidian:** Eight folder names and four note templates are public; private notes are not. Use `-Vault -VaultPath <your-chosen-path>` in the real account, and confirm before any note write.


<br />
<br />


## 🔎 Audit original local skills before promoting them


The [exact-local source and sidecar checker](./exact-local-origin-review.md) provides six pinned **unapproved** public source leads for existing direct skills (`deep-research`, `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`). It verifies source hashes privately on the reference machine, inventories supporting-file counts for all 62 direct skills and checks the seven customized Ardizuo files without exporting their content. No release coverage number is increased until matching content, necessary sidecars, license compliance, a safe installer and real execution are confirmed.


<br />
<br />


## ⚠️ Remaining blockers before a complete public release


1. **Four unknown-origin skills:** `accessibility-diff`, `accessibility-inspect`, `accessibility-scan`, `owasp-security` cannot be redistributable source code without provenance verification.
2. **Seventeen direct skills:** The installed live files can be native/plugin-provided or copied from third-party sources. Their exact direct-source install routes and required dependencies need to be established; don't bundle caches or copyrighted copies by assumption.
3. **Variant differences:** Five skill and 11 command upstream variants do not duplicate local customizations. Seven existing Ardizuo assets also differ from public source.
4. **Sidecars and runtime:** Publishers may use scripts, references or tools beyond `SKILL.md`; actual agent, command, hook and provider task calls still need verification.
5. **Fresh Windows acceptance:** Test network downloads, provider auth, browser dashboard, backups, repeat installation and partial failures on a clean account before calling it a one-click replica.


<br />
<br />


## 🛡️ Safety and evidence definitions


A **source path** proves a definition is available; a **hash match** proves its file matches the pinned publisher version; **installed** means files were written without conflict; **configured** means a setting or registration is present; **connected** means the provider reports a successful connection; **executed** means a real task/tool/hook ran with evidence. These are different checkpoints.

Use the read-only command `python .\scripts\release-audit.py` to check what the **GitHub package** can reproduce. Use `python .\scripts\coverage-doctor.py --strict` to check what exists on your **current machine**. Both must remain clear about their distinct roles.

See [full setup](./full-setup.md) · [exact inventory](../components/exact-coverage.md) · [verification](./verification-checklist.md) · [security](../../SECURITY.md).
