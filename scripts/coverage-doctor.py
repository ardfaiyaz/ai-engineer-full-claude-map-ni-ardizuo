#!/usr/bin/env python3
"""Auditable, offline Development Hub capability inventory.

No subprocess, network access, source-content dumping or credential printing.
Direct definitions, enabled cached plugin definitions, and dormant caches are
reported separately. Configuration never counts as authenticated or executed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'setup/reference-inventory.json'
FULL = ROOT / 'setup/full-stack.json'
ASSETS = ROOT / 'setup/development-assets.json'
HOOKS = ('dead-code-check', 'log-to-vault', 'skill-gate-check', 'stop-vault-log', 'vault-session-init')


def read_json(path, default):
    try:
        value = json.loads(path.read_text(encoding='utf-8-sig'))
        return value if isinstance(value, dict) else default
    except (OSError, ValueError, UnicodeError):
        return default


def paths_for(config, kind):
    base = config / kind
    if not base.is_dir():
        return []
    pattern = 'SKILL.md' if kind == 'skills' else '*.md'
    return sorted(p for p in base.rglob(pattern) if p.is_file())


def plugin_cache_records(config, enabled, kind):
    """Index only expected cache layout: cache/<marketplace>/<plugin>/<version>/..."""
    cache = config / 'plugins/cache'
    if not cache.is_dir():
        return {}
    out = {}
    target = 'SKILL.md' if kind == 'skills' else '*.md'
    for candidate in cache.rglob(target):
        if not candidate.is_file():
            continue
        rel = candidate.relative_to(cache).parts
        if len(rel) < 6:
            continue
        marketplace, plugin = rel[0], rel[1]
        ident = f'{plugin}@{marketplace}'
        slug = candidate.parent.name if kind == 'skills' else candidate.stem
        state = 'enabled-plugin-cache' if enabled.get(ident) is True else 'cached-unconfirmed'
        existing = out.get(slug.casefold())
        if existing != 'enabled-plugin-cache':
            out[slug.casefold()] = state
    return out


def find_definitions(config, names, kind, enabled):
    direct = { (p.parent.name if kind == 'skills' else p.stem).casefold() for p in paths_for(config, kind)}
    plugin = plugin_cache_records(config, enabled, kind)
    records = {}
    for name in names:
        key = name.casefold()
        records[name] = 'direct' if key in direct else plugin.get(key, 'missing')
    return records


def sha(path):
    return hashlib.sha256(path.read_bytes()).digest()


def inspect(config, home_config=None, vault=None):
    ref = read_json(REF, {})
    stack = read_json(FULL, {})
    asset_paths = read_json(ASSETS, {}).get('filePaths', [])
    settings = read_json(config/'settings.json', {})
    enabled = settings.get('enabledPlugins', {})
    if not isinstance(enabled, dict): enabled = {}
    hook_settings = settings.get('hooks', {})
    if not isinstance(hook_settings, dict): hook_settings = {}

    home_record = read_json(home_config or Path.home()/'.claude.json', {})
    mcps = home_record.get('mcpServers', {})
    if not isinstance(mcps, dict): mcps = {}
    vault = vault or Path(os.environ.get('CLAUDE_DEV_VAULT') or Path.home()/'Documents/Claude-Dev-Vault')

    local = {'identical': 0, 'different': 0, 'missing': 0}
    for name in asset_paths:
        source = ROOT/'ardizuo-plugin'/name
        dest = config/name
        if not source.is_file() or not dest.is_file(): local['missing'] += 1
        elif sha(source) == sha(dest): local['identical'] += 1
        else: local['different'] += 1

    result = {
        'disclaimer': 'Local evidence only. Enabled/configured is not authenticated, connected or executed.',
        'originalAssets': local,
        'agents': find_definitions(config, ref.get('agents', []), 'agents', enabled),
        'skills': find_definitions(config, ref.get('globalSkills', []), 'skills', enabled),
        'commands': find_definitions(config, ref.get('commands', []), 'commands', enabled),
        'plugins': {p['id']: ('enabled-in-settings' if enabled.get(p['id']) is True else 'not-confirmed-enabled') for p in stack.get('plugins', [])},
        'mcps': {m['name']: ('registered-user-scope' if m['name'] in mcps else 'not-confirmed-user-scope') for m in stack.get('mcp', [])},
        'hooks': {name: ('file-present' if (config/'hooks'/f'{name}.mjs').is_file() else 'missing') for name in HOOKS},
        'hookEvents': {evt: len(items) if isinstance(items, list) else 0 for evt, items in hook_settings.items()},
        'vaultFolders': {folder: (vault/folder).is_dir() for folder in stack.get('memory',{}).get('folders', [])},
        'vaultTemplates': {path.name: (vault/'Templates'/path.name).is_file() for path in (ROOT/'vault/templates').glob('*.md')},
        'dashboard': 'not-verified-automatically',
    }
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config-dir', type=Path, default=Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude'))
    ap.add_argument('--home-config', type=Path, help='Optional .claude.json for user-scope MCP names (test isolation)')
    ap.add_argument('--vault-path', type=Path)
    ap.add_argument('--json', action='store_true', help='Print machine-readable names/status only; no secret values or absolute paths')
    ap.add_argument('--strict', action='store_true', help='Return 2 when any named agent, skill, command, plugin, or MCP is not confirmed installed/configured')
    args = ap.parse_args()
    report = inspect(args.config_dir.expanduser(), args.home_config, args.vault_path)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print('ARDIZUO DEVELOPMENT HUB — EXACT NAME COVERAGE (OFFLINE)')
        print(report['disclaimer'])
        print('Original assets:', report['originalAssets'])
        for category in ('agents', 'skills', 'commands', 'plugins', 'mcps'):
            entries = report[category]
            ready = {'direct', 'enabled-plugin-cache', 'enabled-in-settings', 'registered-user-scope'}
            count = sum(v in ready for v in entries.values())
            print(f'\n{category.upper()}: {count}/{len(entries)} matched (not runtime proof)')
            for name, status in entries.items():
                print(f'  {status:24} {name}')
        print('\nHOOK FILES:', ', '.join(f'{k}={v}' for k, v in report['hooks'].items()))
        print('HOOK EVENTS:', report['hookEvents'], '(presence only)')
        print('VAULT FOLDERS:', sum(report['vaultFolders'].values()), '/', len(report['vaultFolders']))
        print('VAULT TEMPLATES:', sum(report['vaultTemplates'].values()), '/', len(report['vaultTemplates']))
        print('DASHBOARD:', report['dashboard'])
        print('\nCached-only skills are NOT counted as enabled. Reconnect/enable provider plugins separately.')
        print('Do not interpret registered MCP names as connected or authenticated.')
    if args.strict:
        eligible = {'direct', 'enabled-plugin-cache', 'enabled-in-settings', 'registered-user-scope'}
        if any(state not in eligible for category in ('agents','skills','commands','plugins','mcps') for state in report[category].values()):
            return 2
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
