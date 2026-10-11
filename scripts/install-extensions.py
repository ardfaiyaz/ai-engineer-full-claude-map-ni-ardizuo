#!/usr/bin/env python3
"""Extended-stack installer for setup/extension-catalog.json. Dry run by default.

Part of the one-command full installation (install-all.ps1 -All). Installs publisher
plugins, MCP registrations, global CLI tools, commit-pinned skill files and the
gstack skill suite. Per-project steps, credential-gated registrations and references
are printed, never executed. Never reads, embeds or prints credentials; anything
already enabled, registered, on PATH or present on disk is skipped.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/'setup/extension-catalog.json'
EXECUTABLE=('plugin','mcp','cli','pinned-files','git-setup')


def _load(name, filename):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

base=_load('ardizuo_install_all','install-all.py')
pins=_load('ardizuo_install_pinned_skills','install-pinned-skills.py')


def load_catalog():
    return json.loads(CATALOG.read_text(encoding='utf-8'))


def resolve(catalog, selection):
    """Expand comma-separated ids/groups. 'all' = every package in the catalog."""
    packages={p['id']:p for p in catalog['packages']}
    chosen=[]
    for token in [t.strip() for t in selection.split(',') if t.strip()]:
        if token=='all':
            matches=list(catalog['packages'])
        elif token in packages:
            matches=[packages[token]]
        else:
            matches=[p for p in catalog['packages'] if token in p.get('groups',[])]
            if not matches:
                raise ValueError('Unknown extension id or group: '+token)
        chosen.extend(m for m in matches if m not in chosen)
    return chosen


def overlaps(chosen):
    """Groups where more than one selected package does the same job."""
    groups={}
    for p in chosen:
        if p.get('overlapGroup'):
            groups.setdefault(p['overlapGroup'],[]).append(p['id'])
    return {g:ids for g,ids in groups.items() if len(ids)>1}


def enabled_plugins(config):
    try:
        settings=json.loads((config/'settings.json').read_text(encoding='utf-8-sig'))
        return {k for k,v in settings.get('enabledPlugins',{}).items() if v is True}
    except (OSError,ValueError,TypeError,AttributeError):
        return set()


def pinned_targets(config, p):
    for item in p['files']:
        # 'path' is the upstream source; optional 'target' places it (e.g. a LICENSE per skill folder).
        parts=PurePosixPath(item.get('target',item['path'])).parts
        if parts[0]!='skills' or '..' in parts or len(parts)<3:
            raise ValueError('Unsafe pinned file path: '+item['path'])
        yield item, config.joinpath(*parts)


def status(catalog, config, home_config):
    plugins=enabled_plugins(config)
    mcps=base.registered_mcp_names(home_config)
    result={}
    for p in catalog['packages']:
        kind=p['kind']
        if kind=='plugin':
            on=sum(i in plugins for i in p['pluginIds'])
            result[p['id']]='enabled' if on==len(p['pluginIds']) else (f'partial {on}/{len(p["pluginIds"])}' if on else 'not-enabled')
        elif kind=='mcp':
            result[p['id']]='registered' if p['name'] in mcps else 'not-registered'
        elif kind=='cli':
            result[p['id']]='on-path' if shutil.which(p['checkCommand']) else 'not-on-path'
        elif kind=='pinned-files':
            result[p['id']]='present' if all(t.is_file() for _,t in pinned_targets(config,p)) else 'missing'
        elif kind=='git-setup':
            result[p['id']]='present' if (config/p['target']).is_dir() else 'missing'
        else:
            result[p['id']]=kind+'-not-tracked'
    return result


def run_cli(argv, label, dry_run):
    """Resolve npm/uv/winget shims (npm.cmd on Windows) before running without a shell."""
    exe=shutil.which(argv[0])
    return base.run_external([exe or argv[0]]+list(argv[1:]),label,dry_run)


def install_plugins(catalog, plugins, config, apply, actions):
    enabled=enabled_plugins(config)
    wanted=[(p,i) for p in plugins for i in p['pluginIds']]
    needed={i.split('@',1)[1] for _,i in wanted if i not in enabled}
    markets={}
    if needed:
        print('\nMARKETPLACES')
        markets=base.known_marketplaces({'marketplaces':[m for m in catalog['marketplaces'] if m['id'] in needed]},apply)
    if wanted: print('\nPLUGINS')
    for p,plugin_id in wanted:
        key='plugin:'+plugin_id
        if plugin_id in enabled:
            print('  ALREADY ENABLED:',plugin_id);actions[key]='already-enabled';continue
        if markets.get(plugin_id.split('@',1)[1]) not in ('already-configured','cli-success','planned'):
            print('  SKIPPED',plugin_id,'because marketplace setup was not confirmed.');actions[key]='marketplace-not-ready';continue
        actions[key]=base.run_external(['claude','plugin','install',plugin_id],'plugin '+plugin_id,not apply)
    for p in plugins:
        if p.get('credentials'):print('  Sign-in needed later for',p['id']+':',p['credentials'])


def install_mcps(mcps, apply, actions):
    names=base.registered_mcp_names()
    if mcps: print('\nMCP REGISTRATIONS')
    for p in mcps:
        key='mcp:'+p['name']
        if p['name'] in names:
            print('  '+p['name']+' — configured already (connectivity NOT verified)');actions[key]='already-configured';continue
        missing=[x for x in p.get('prerequisites',[]) if not shutil.which(x)]
        if missing:
            print('  '+p['name']+' — missing dependencies: '+', '.join(missing));actions[key]='missing-dependency';continue
        actions[key]=base.run_external(p['argv'],'register MCP '+p['name'],not apply)


def install_clis(clis, apply, actions):
    if clis: print('\nGLOBAL CLI TOOLS')
    for p in clis:
        key='cli:'+p['id']
        if shutil.which(p['checkCommand']):
            print('  '+p['id']+' — '+p['checkCommand']+' already on PATH');actions[key]='already-installed';continue
        missing=[x for x in p['prerequisites'] if not shutil.which(x)]
        if missing:
            print('  '+p['id']+' — missing dependencies: '+', '.join(missing));actions[key]='missing-dependency';continue
        for argv in p['commands']:
            actions[key]=run_cli(argv,p['id']+': '+' '.join(argv),not apply)
            if actions[key] not in ('cli-success','planned'):break


def install_pinned(pinned, config, apply, actions, fetch=None):
    fetch=fetch or pins.fetch_source
    if pinned: print('\nPINNED SKILL FILES')
    for p in pinned:
        key='files:'+p['id']
        plan=list(pinned_targets(config,p))
        absent=[(i,t) for i,t in plan if not t.exists()]
        if not absent:
            print('  '+p['id']+' — all',len(plan),'files present');actions[key]='already-installed';continue
        if not apply:
            for i,_ in absent:print('  WOULD DOWNLOAD',p['repository']+'@'+p['commit'][:12],i['path'])
            actions[key]='planned';continue
        try:
            # Download and verify every file before writing any, so a mismatch leaves nothing behind.
            bodies=[(t,fetch({'upstreamRepository':p['repository'],'revision':p['commit'],'sourceFilePath':i['path'],
                              'gitBlobSHA1':i['blobSha'],'target':i.get('target',i['path'])})) for i,t in absent]
            for target,body in bodies:
                target.parent.mkdir(parents=True,exist_ok=True)
                with target.open('xb') as fh:fh.write(body)
            print('  '+p['id']+' — installed',len(bodies),'verified files (create-only)');actions[key]='cli-success'
        except Exception as e:
            print('  '+p['id']+' — FAILED: '+str(e));actions[key]='failed'


def install_git_setup(suites, config, apply, actions):
    if suites: print('\nGIT SKILL SUITES')
    for p in suites:
        key='git:'+p['id']
        target=config/p['target']
        if target.exists():
            print('  '+p['id']+' — already present at '+str(target));actions[key]='already-installed';continue
        missing=[x for x in p['prerequisites'] if not shutil.which(x)]
        if missing:
            print('  '+p['id']+' — missing dependencies: '+', '.join(missing)+'. See docs/installation/extensions.md');actions[key]='missing-dependency';continue
        actions[key]=base.run_external(['git','clone','--single-branch','--depth','1',p['repository'],str(target)],p['id']+' clone',not apply)
        if actions[key]!='cli-success':continue
        print('  '+p['id']+' — RUNNING setup in '+str(target),flush=True)
        code=subprocess.run([shutil.which(p['setup'][0])]+p['setup'][1:],cwd=target,check=False).returncode
        actions[key]='cli-success' if code==0 else 'failed'
        if code:print('    setup FAILED (exit code '+str(code)+'); the clone was left in place for inspection.')


def print_manual(guided, actions):
    if guided: print('\nPER-PROJECT AND CREDENTIAL STEPS (printed, not executed)')
    for p in guided:
        print(f"  {p['id']} — {p['kind'].upper()} ({p['scope']})")
        for command in p.get('commands',[]):print('      '+command)
        print('      Docs: '+p['docs'])
        actions[p['kind']+':'+p['id']]='manual'


def install(catalog, chosen, config, apply):
    actions={}
    by_kind=lambda k:[p for p in chosen if p['kind']==k]
    install_plugins(catalog,by_kind('plugin'),config,apply,actions)
    install_mcps(by_kind('mcp'),apply,actions)
    install_clis(by_kind('cli'),apply,actions)
    install_pinned(by_kind('pinned-files'),config,apply,actions)
    install_git_setup(by_kind('git-setup'),config,apply,actions)
    print_manual([p for p in chosen if p['kind'] not in EXECUTABLE],actions)
    project=[(p['id'],s) for p in chosen for s in p.get('projectSteps',[])]
    for pid,step in project:print(f'  {pid} — per project: {step}')
    return actions


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--select',default='all',help="Comma-separated ids or groups (all, priority, security, testing, engineering, frontend, research, review, workflow, collections, ...). Default: all")
    ap.add_argument('--apply',action='store_true',help='Run the selected installs')
    ap.add_argument('--list',action='store_true',help='List catalog packages and exit')
    ap.add_argument('--status',action='store_true',help='Report enabled/registered/on-PATH state from local names only')
    ap.add_argument('--json',action='store_true',help='JSON output for --status')
    ap.add_argument('--config-dir',type=Path,help='Claude config directory (plugin detection, pinned skills, gstack)')
    ap.add_argument('--home-config',type=Path,help='Alternate ~/.claude.json for --status (tests)')
    args=ap.parse_args(argv)
    catalog=load_catalog()
    config=(args.config_dir or Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')).expanduser().resolve()
    if args.list:
        for p in catalog['packages']:
            ids=p.get('pluginIds') or [p.get('name') or p.get('checkCommand') or p.get('repository') or p.get('docs','')]
            target=ids[0]+(f' (+{len(ids)-1} more)' if len(ids)>1 else '')
            print(f"{p['id']:30} {p['kind']:12} {p['scope']:8} {','.join(p.get('groups',[])) or '-':26} {target}")
        return 0
    if args.status:
        result=status(catalog,config,args.home_config)
        if args.json:print(json.dumps(result,indent=2))
        else:
            for k,v in result.items():print(f'  {k:30} {v}')
            print('Enabled/registered/on-PATH is not authenticated or tested.')
        return 0
    chosen=resolve(catalog,args.select)
    print('\nARDIZUO EXTENDED STACK —','APPLY' if args.apply else 'DRY RUN')
    print('Selection:',args.select,'->',len(chosen),'packages')
    for group,ids in overlaps(chosen).items():
        print(f'  NOTE overlap [{group}]: {", ".join(ids)} are all installed; disable one if they conflict.')
    actions=install(catalog,chosen,config,args.apply)
    print('\nEXTENDED STACK STATUS')
    print('  Actions tracked:',len(actions),'(exit 0 is not provider authentication)')
    print('  Next: claude plugin list ; claude mcp list ; python scripts/install-extensions.py --status')
    if any(v in ('failed','missing-dependency','marketplace-not-ready') for v in actions.values()):
        print('  Some steps did not complete. See docs/installation/extensions.md.')
    return 0


if __name__=='__main__':
    try:sys.exit(main())
    except Exception as e:
        print('ERROR:',e,file=sys.stderr)
        sys.exit(1)
