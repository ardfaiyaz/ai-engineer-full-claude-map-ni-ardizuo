# Claude Code plugin catalog

**Install only what you need.** This page lists the **12 enabled plugins on the author's reference machine**; Core doesn't install these plugins. The **All Layers** installer has an explicit opt-in for marketplace registration and supported third-party installation.

<br />

## Reference plugins

| Plugin guide | Identifier on reference machine | Core install status |
| :--- | :--- | :--- |
| [Playwright](./playwright.md) | `playwright@claude-plugins-official` | Reference — not installed by Core |
| [Context7](./context7.md) | `context7@claude-plugins-official` | Reference — not installed by Core |
| [Superpowers](./superpowers.md) | `superpowers@claude-plugins-official` | Reference — not installed by Core |
| [Document skills](./document-skills.md) | `document-skills@anthropic-agent-skills` | Reference — not installed by Core |
| [Example skills](./example-skills.md) | `example-skills@anthropic-agent-skills` | Reference — not installed by Core |
| [Morph Compact](./morph-compact.md) | `morph-compact@morph` | Reference — not installed by Core |
| [Ralph skills](./ralph-skills.md) | `ralph-skills@ralph-marketplace` | Reference — not installed by Core |
| [Expo](./expo.md) | `expo@claude-plugins-official` | Reference — not installed by Core |
| [Stripe](./stripe.md) | `stripe@claude-plugins-official` | Reference — not installed by Core |
| [Sentry](./sentry.md) | `sentry@claude-plugins-official` | Reference — not installed by Core |
| [Atlassian](./atlassian.md) | `atlassian@claude-plugins-official` | Reference — not installed by Core |
| [Notion](./notion.md) | `notion@claude-plugins-official` | Reference — not installed by Core |

<br />

## Before installing

1. Read [Claude Code plugin docs](https://code.claude.com/docs/en/discover-plugins) and verify the marketplace source.
2. Check the individual guide's runtime and account requirements.
3. Install with user approval; providers can require additional login or paid usage.
4. Verify with `claude plugin list` and, inside Claude Code, `/skills` and `/mcp`.

Third-party source is not redistributed here. **Enabled ≠ authenticated ≠ invoked.**

<br />

[API keys and PowerShell](../../docs/security/api-keys-and-powershell.md) · [Component catalog](../../docs/components/README.md) · [Docs hub](../../docs/README.md)


## Marketplace setup before installing plugins

Marketplace IDs come from the marketplaces' own catalog, not from their GitHub repository names. Register these first (after inspecting their repositories):

```powershell
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add anthropics/skills
claude plugin marketplace add snarktank/ralph
claude plugin marketplace add morphllm/morph-claude-code-plugin
```

The first marketplace is ordinarily already available in Claude Code. If so, do **not** remove or overwrite it. The updated Ardizuo `-All` installer detects known marketplaces where the CLI supports listing them and attempts registration before the 12 plugin installations. It skips plugins whose marketplace registration failed.

**Plugin install examples:**

```powershell
claude plugin install document-skills@anthropic-agent-skills
claude plugin install ralph-skills@ralph-marketplace
claude plugin install morph-compact@morph
```

**Source documentation:** [Anthropic official catalog](https://github.com/anthropics/claude-plugins-official), [Anthropic skills](https://github.com/anthropics/skills), [Ralph](https://github.com/snarktank/ralph), and [Morph](https://github.com/morphllm/morph-claude-code-plugin).

Plugin installation may execute third-party code. Review source and permissions before consenting, and sign in separately to provider accounts. `claude plugin list` is not evidence of a successful provider connection.
