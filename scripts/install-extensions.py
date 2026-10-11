#!/usr/bin/env python3
"""Opt-in extension installer for setup/extension-catalog.json. Dry run by default.

Installs only selected publisher plugins and MCP registrations through the Claude
CLI. Project-scoped tools and references are printed as guidance, never executed.
Never reads, embeds or prints credentials; already-enabled plugins and already
registered MCP names are skipped.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/'setup/extension-catalog.json'
EXECUTABLE=('plugin','mcp')

_spec=importlib.util.spec_from_file_location('ardizuo_install_all',ROOT/'scripts/install-all.py')
base=importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)


def load_catalog():
    return json.loads(CATALOG.read_text(encoding='utf-8'))


def resolve(catalog, selection):
    """Expand comma-separated ids/groups. 'all' = every non-alternative package."""
    packages={p['id']:p for p in catalog['packages']}
    chosen=[]
    for token in [t.strip() for t in selection.split(',') if t.strip()]:
        if token=='all':
            matches=[p for p in catalog['packages'] if not p.get('alternative')]
        elif token in packages:
            matches=[packages[token]]
        else:
            matches=[p for p in catalog['packages'] if token in p.get('groups',[])]
            if not matches:
                raise ValueError('Unknown extension id or group: '+token)
        chosen.extend(m for m in matches if m not in chosen)
    groups={}
    for p in chosen:
        if p.get('exclusiveGroup'):
            groups.setdefault(p['exclusiveGroup'],[]).append(p['id'])
    clashes={g:ids for g,ids in groups.items() if len(ids)>1}
    if clashes:
        raise ValueError('Choose one per exclusive group: '+'; '.join(f'{g}: {", ".join(ids)}' for g,ids in clashes.items()))
    return chosen


def enabled_plugins(config):
    try:
        settings=json.loads((config/'settings.json').read_text(encoding='utf-8-sig'))
        return {k for k,v in settings.get('enabledPlugins',{}).items() if v is True}
    except (OSError,ValueError,TypeError,AttributeError):
        return set()


def status(catalog, config, home_config):
    plugins=enabled_plugins(config)
    mcps=base.registered_mcp_names(home_config)
    result={}
    for p in catalog['packages']:
        if p['kind']=='plugin':
            result[p['id']]='enabled' if p['pluginId'] in plugins else 'not-enabled'
        elif p['kind']=='mcp':
            result[p['id']]='registered' if p['name'] in mcps else 'not-registered'
        else:
            result[p['id']]=p['kind']+'-not-tracked'
    return result


def print_guidance(p):
    print(f"  {p['id']} — {p['kind'].upper()} ({p['scope']}); not executed by this installer")
    for command in p.get('commands',[]):
        print('      '+command)
    print('      Docs: '+p['docs'])


def install(catalog, chosen, config, apply):
    actions={}
    plugin_ids=enabled_plugins(config)
    mcp_names=base.registered_mcp_names()
    plugins=[p for p in chosen if p['kind']=='plugin']
    needed={p['pluginId'].split('@',1)[1] for p in plugins if p['pluginId'] not in plugin_ids}
    markets={}
    if needed:
        print('\nMARKETPLACES')
        wanted={'marketplaces':[m for m in catalog['marketplaces'] if m['id'] in needed]}
        markets=base.known_marketplaces(wanted, apply)
    if plugins: print('\nPLUGINS')
    for p in plugins:
        key='plugin:'+p['pluginId']
        if p['pluginId'] in plugin_ids:
            print('  ALREADY ENABLED:',p['pluginId']);actions[key]='already-enabled';continue
        if markets.get(p['pluginId'].split('@',1)[1]) not in ('already-configured','cli-success','planned'):
            print('  SKIPPED',p['pluginId'],'because marketplace setup was not confirmed.');actions[key]='marketplace-not-ready';continue
        actions[key]=base.run_external(['claude','plugin','install',p['pluginId']],'plugin '+p['pluginId'],not apply)
        if p.get('credentials'):print('    Sign-in needed later:',p['credentials'])
    mcps=[p for p in chosen if p['kind']=='mcp']
    if mcps: print('\nMCP REGISTRATIONS')
    for p in mcps:
        key='mcp:'+p['name']
        if p['name'] in mcp_names:
            print('  '+p['name']+' — configured already (connectivity NOT verified)');actions[key]='already-configured';continue
        missing=[x for x in p.get('prerequisites',[]) if not base.shutil.which(x)]
        if missing:
            print('  '+p['name']+' — missing dependencies: '+', '.join(missing));actions[key]='missing-dependency';continue
        actions[key]=base.run_external(p['argv'],'register MCP '+p['name'],not apply)
    guided=[p for p in chosen if p['kind'] not in EXECUTABLE]
    if guided: print('\nGUIDED / PROJECT-ONLY / REFERENCE (manual, after review)')
    for p in guided:
        print_guidance(p);actions[p['kind']+':'+p['id']]='manual'
    return actions


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--select',default='priority',help="Comma-separated ids or groups (priority, security, testing, engineering, frontend, research, automation, mcp-dev, all). Default: priority")
    ap.add_argument('--apply',action='store_true',help='Run the selected Claude CLI plugin/MCP commands')
    ap.add_argument('--list',action='store_true',help='List catalog packages and exit')
    ap.add_argument('--status',action='store_true',help='Report enabled/registered state from local config names only')
    ap.add_argument('--json',action='store_true',help='JSON output for --status')
    ap.add_argument('--config-dir',type=Path,help='Claude config directory used for enabled-plugin detection')
    ap.add_argument('--home-config',type=Path,help='Alternate ~/.claude.json for --status (tests)')
    args=ap.parse_args(argv)
    catalog=load_catalog()
    config=(args.config_dir or Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')).expanduser().resolve()
    if args.list:
        for p in catalog['packages']:
            tag=' [alternative]' if p.get('alternative') else ''
            target=p.get('pluginId') or p.get('name') or p.get('docs','')
            print(f"{p['id']:30} {p['kind']:9} {p['scope']:10} {','.join(p.get('groups',[])) or '-':28} {target}{tag}")
        return 0
    if args.status:
        result=status(catalog,config,args.home_config)
        if args.json:print(json.dumps(result,indent=2))
        else:
            for k,v in result.items():print(f'  {k:30} {v}')
            print('Enabled/registered is not authenticated or tested.')
        return 0
    chosen=resolve(catalog,args.select)
    print('\nARDIZUO OPTIONAL EXTENSIONS —','APPLY' if args.apply else 'DRY RUN')
    print('Selection:',args.select,'->',', '.join(p['id'] for p in chosen))
    skipped=[p['id'] for p in catalog['packages'] if p.get('alternative') and p not in chosen]
    if 'all' in args.select.split(',') and skipped:
        print('Alternatives not selected by "all" (name them explicitly):',', '.join(skipped))
    actions=install(catalog,chosen,config,args.apply)
    print('\nEXTENSION STATUS')
    print('  Actions tracked:',len(actions),'(exit 0 is not provider authentication)')
    print('  Next: claude plugin list ; claude mcp list ; in Claude Code /plugin, /skills, /mcp, /hooks')
    if any(v in ('failed','missing-dependency','marketplace-not-ready') for v in actions.values()):
        print('  Some optional steps did not complete. See docs/installation/extensions.md.')
    return 0


if __name__=='__main__':
    try:sys.exit(main())
    except Exception as e:
        print('ERROR:',e,file=sys.stderr)
        sys.exit(1)
