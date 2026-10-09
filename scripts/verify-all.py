#!/usr/bin/env python3
"""Local capability coverage (names/status only; no tokens, URLs, env, or CLI network calls)."""
import json,os,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
config=Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')
manifest=json.loads((ROOT/'setup/full-stack.json').read_text(encoding='utf8'))
files=json.loads((ROOT/'setup/development-assets.json').read_text(encoding='utf8'))['filePaths']
counts={'identical':0,'missing':0,'different':0}
print('ARDIZUO SETUP DOCTOR — LOCAL STATE ONLY\n')
print('Target Claude global config:',config)
for f in files:
    src=ROOT/'ardizuo-plugin'/f;dst=config/f
    state='missing' if not dst.is_file() else ('identical' if hashlib.sha256(src.read_bytes()).digest()==hashlib.sha256(dst.read_bytes()).digest() else 'different')
    counts[state]+=1
print('Original files: ',counts,'(28 reviewed files; not plugin caches)')
agentroot=config/'agents'
installed_agents={p.stem for p in agentroot.glob('*.md')} if agentroot.is_dir() else set()
reference=set(json.loads((ROOT/'setup/reference-inventory.json').read_text(encoding='utf8'))['agents'])
print(f'Global agents: {len(installed_agents & reference)}/{len(reference)} reference names found')
cmds=config/'commands/sc'
print('SuperClaude commands: ',len(list(cmds.glob('*.md'))) if cmds.exists() else 0,'global sc command files found')
settings={}
try:settings=json.loads((config/'settings.json').read_text(encoding='utf-8-sig'))
except (FileNotFoundError,ValueError):pass
plugins=settings.get('enabledPlugins',{}) if isinstance(settings,dict) else {}
installed={k for k,v in plugins.items() if v is True}
missing=[p['id'] for p in manifest['plugins'] if p['id'] not in installed]
print(f'Enabled plugins: {len(manifest["plugins"])-len(missing)}/{len(manifest["plugins"])} reference IDs confirmed in settings.json')
if missing:print('  Not confirmed:',', '.join(missing))
# user-scope MCP registrations may be elsewhere; this checks only home/.claude.json.
mcps={}
try:mcps=json.loads((Path.home()/'.claude.json').read_text(encoding='utf-8-sig')).get('mcpServers',{})
except (OSError,ValueError,TypeError):pass
found=[x['name'] for x in manifest['mcp'] if x['name'] in mcps]
print(f'MCP registration names: {len(found)}/9 found in home .claude.json; connection/auth NOT tested')
print('Hook files: ',sum((config/'hooks'/name).is_file() for name in ['skill-gate-check.mjs','vault-session-init.mjs','log-to-vault.mjs','stop-vault-log.mjs','dead-code-check.mjs']))
print('Hook registration events: ',len(settings.get('hooks',{})) if isinstance(settings,dict) else 0,'(presence not execution)')
vault=Path(os.environ.get('CLAUDE_DEV_VAULT') or Path.home()/'Documents/Claude-Dev-Vault')
print('Obsidian vault folders: ',sum((vault/name).is_dir() for name in manifest['memory']['folders']),'/8; notes not read')
print('Dashboard: check separately using docs/installation/claude-map.md')
print('\nIMPORTANT: Installed/configured != connected/authenticated != actually used.')
print('Check inside Claude Code: /skills, /mcp and /hooks.')
