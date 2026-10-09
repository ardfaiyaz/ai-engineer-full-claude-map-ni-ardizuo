# Third-party attribution and licenses

**This project is a configuration and installation effort, not a repackaged distribution of other developers' work.** Third-party licenses and ownership remain with their respective authors.

<br />

## Reference projects

| Project | Official source | How we use it |
| :--- | :--- | :--- |
| Claude Code | [Anthropic docs](https://code.claude.com/docs/en/setup) | Install the runtime using official distribution |
| Claude Map | [Upstream source](https://github.com/shamim0902/claude-map) | Optional *planned* attributed fork or patch; not bundled yet |
| Superpowers | [Upstream source](https://github.com/obra/superpowers) | Plugin reference; not redistributed |
| Ralph | [Upstream source](https://github.com/snarktank/ralph) | PRD/plugin reference; not redistributed |
| Claude Code plugins | [Plugin documentation](https://code.claude.com/docs/en/discover-plugins) | Installed from upstream marketplaces with consent |
| MCP implementations | [Official MCP documentation](https://code.claude.com/docs/en/mcp) | Registered from official providers, not copied from another user |

<br />

## Before a full release

1. Select and add a license covering **only original Ardizuo-authored code**.
2. Identify ownership/license of every bundled agent, hook, skill and generated script.
3. Preserve any upstream license, author attribution and modification notices required by redistribution.
4. Prefer pinned upstream dependencies and separate install instructions over shipping third-party caches.
5. Audit the dashboard patch for upstream version compatibility and security.

**No blanket license grant for third-party content is implied by this repository.** License selection for the original work remains pending.

[Security](./SECURITY.md) · [Release checklist](./docs/release-checklist.md) · [README](./README.md)
