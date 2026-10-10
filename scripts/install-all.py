#!/usr/bin/env python3
"""Windows-first, user-scoped setup orchestrator. Dry run by default.

This tool NEVER reads or prints secrets, never assumes MCP authentication,
and never copies third-party caches. External installation is explicit opt-in.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'setup/full-stack.json'
LOCAL=ROOT/'setup/development-assets.json'


def hash_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def relpath(s):
    parts=Path(s.replace('\\','/')).parts
    if not parts or any(p in ('','..','.') for p in parts) or s.startswith(('/', '\\')) or ':' in s:
        raise ValueError('Untrusted relative path in manifest')
    if parts[0] not in ('agents','commands','hooks','rules','skills','workflows','assets'):
        raise ValueError('Unapproved destination category')
    return Path(*parts)


def local_plan(config, include_rule=True):
    srcs=json.loads(LOCAL.read_text(encoding='utf-8'))['filePaths']
    assert len(srcs)==28, 'Development asset inventory count changed: review manifest'
    plans=[]
    for entry in srcs:
        rel=relpath(entry)
        source=ROOT/'ardizuo-plugin'/rel
        dest=config/rel
        if not source.is_file():raise FileNotFoundError(f'Missing packaged source: {entry}')
        state='new' if not dest.exists() else ('identical' if dest.is_file() and hash_file(source)==hash_file(dest) else 'CONFLICT')
        plans.append((str(rel),source,dest,state))
    source=ROOT/'global-config/CLAUDE.md'
    dest=config/'CLAUDE.md'
    state='new' if not dest.exists() else ('identical' if dest.is_file() and hash_file(source)==hash_file(dest) else 'CONFLICT')
    plans.append(('CLAUDE.md',source,dest,state))
    if include_rule:
        source=ROOT/'global-config/rules/ardizuo-development.md'
        dest=config/'rules/ardizuo-development.md'
        state='new' if not dest.exists() else ('identical' if dest.is_file() and hash_file(source)==hash_file(dest) else 'CONFLICT')
        plans.append(('rules/ardizuo-development.md',source,dest,state))
    return plans


def execute_plan(plan, apply):
    for label,src,dst,state in plan:
        print(f'  {state:10} {label}')
    errors=[label for label,_,_,status in plan if status=='CONFLICT']
    if errors:
        print('\nSTOPPED: different files already exist. NO local changes made. Resolve in a test configuration first.')
        raise RuntimeError('File conflicts: '+', '.join(errors))
    if not apply:
        print('\nDRY RUN. No files copied. Add -Apply to the PowerShell wrapper.');return
    created=[]
    try:
        for label,src,dst,state in plan:
            if state=='identical': continue
            dst.parent.mkdir(parents=True,exist_ok=True)
            # Exclusive creation: never overwrite pre-existing data, even in races.
            with dst.open('xb') as fh: fh.write(src.read_bytes())
            created.append(dst)
            if hash_file(src)!=hash_file(dst):raise RuntimeError(f'Hash mismatch: {label}')
    except BaseException:
        for p in reversed(created):p.unlink(missing_ok=True)
        raise
    print(f'Installed {len(created)} new local files, skipped {len(plan)-len(created)} identical. No overwrites.')


def run_external(argv, label, dry_run=False):
    print('  '+label+' — '+ ('WOULD RUN' if dry_run else 'RUNNING'))
    if dry_run: return 'planned'
    if not shutil.which(argv[0]):
        print('    SKIPPED: prerequisite CLI not found: '+argv[0]);return 'missing-dependency'
    try:
        # No captured stdout; external installer prints only to user's terminal.
        code=subprocess.run(argv,check=False).returncode
        if code:
            print('    FAILED (exit code '+str(code)+'). See official linked guide.');return 'failed'
        print('    CLI returned exit=0. Authentication/availability NOT verified.');return 'cli-success'
    except Exception as e:
        print('    FAILED: '+type(e).__name__);return 'failed'


def known_marketplaces(manifest, apply):
    """Register official upstream marketplaces first, never interpolate shell commands.

    Claude CLI marketplace output may vary between versions. We never print it or
    treat this step as evidence that individual plugins are enabled.
    """
    market = manifest.get('marketplaces', [])
    if not apply:
        for entry in market:
            print('  WOULD CHECK/REGISTER:', entry['id'], 'from', entry['source'])
        return {entry['id']: 'planned' for entry in market}
    known = set()
    if shutil.which('claude'):
        try:
            p = subprocess.run(['claude','plugin','marketplace','list'], capture_output=True, text=True, timeout=30)
            if p.returncode == 0:
                for entry in market:
                    if entry['id'].casefold() in p.stdout.casefold():
                        known.add(entry['id'])
        except (OSError, subprocess.TimeoutExpired):
            pass
    result = {}
    for entry in market:
        name = entry['id']
        if name in known:
            print('  MARKETPLACE ALREADY REGISTERED:', name)
            result[name]='already-configured'
            continue
        result[name]=run_external(['claude','plugin','marketplace','add',entry['source']],
                                  'marketplace '+name,False)
    return result


def install_templates(source_folder, vault, apply):
    """Never overwrite personal Obsidian templates; all-or-nothing on conflicts."""
    templates = sorted(source_folder.glob('*.md'))
    if not templates: raise RuntimeError('No shipped vault templates found')
    dest = vault/'Templates'
    for src in templates:
        target = dest/src.name
        if target.exists() and (not target.is_file() or hash_file(target)!=hash_file(src)):
            raise RuntimeError('Conflicting vault template; will not overwrite: '+src.name)
    if not apply:
        for src in templates: print('  WOULD COPY template:',src.name,'(unless identical)')
        return
    dest.mkdir(parents=True,exist_ok=True)
    copied = 0
    for src in templates:
        target = dest/src.name
        if target.exists(): continue
        try:
            with target.open('xb') as output: output.write(src.read_bytes())
        except FileExistsError:
            raise RuntimeError('Vault template appeared during installation; inspect '+src.name)
        copied += 1
    print('  Vault templates: installed',copied,'new; identical:',len(templates)-copied,'; no overwrites.')


def main():
    ap=argparse.ArgumentParser(description='Ardizuo global development setup (dry run by default)')
    ap.add_argument('--apply',action='store_true',help='Copy reviewed local files into Claude user config')
    ap.add_argument('--external',action='store_true',help='Opt-in to third-party installers; may download and prompt')
    ap.add_argument('--hooks',action='store_true',help='Opt-in to registering five hooks in settings.json')
    ap.add_argument('--vault',action='store_true',help='Opt-in to creating an empty Obsidian vault folder structure')
    ap.add_argument('--vault-path',type=Path,help='Alternative vault destination')
    ap.add_argument('--dashboard',action='store_true',help='Opt-in to npm install -g claude-map; dashboard patch is separate')
    ap.add_argument('--superclaude',action='store_true',help='Allow upstream SuperClaude pipx install and install command')
    ap.add_argument('--pinned-superclaude',action='store_true',help='Install commit-pinned, hash-verified SuperClaude files (optional network with --apply)')
    ap.add_argument('--pinned-skills',action='store_true',help='Install 20 pinned third-party skill prompts (network only with --apply)')
    ap.add_argument('--skill-upstream-variants',action='store_true',help='Opt in to 5 upstream skill prompts different from author references')
    ap.add_argument('--upstream-variants',action='store_true',help='Opt in to 11 upstream commands different from author references')
    ap.add_argument('--plugins',action='store_true',help='Allow third-party plugin install commands')
    ap.add_argument('--mcps',action='store_true',help='Allow supported third-party MCP registration commands')
    ap.add_argument('--config-dir',type=Path,help='Use isolated Claude config for local files (test first)')
    args=ap.parse_args()
    mf=json.loads(MANIFEST.read_text(encoding='utf8'))
    if args.superclaude and args.pinned_superclaude:
        raise ValueError('Choose --superclaude (upstream CLI) OR --pinned-superclaude (static pinned definitions), not both.')
    if args.upstream_variants and not args.pinned_superclaude:
        raise ValueError('--upstream-variants requires --pinned-superclaude.')
    if args.skill_upstream_variants and not args.pinned_skills:
        raise ValueError('--skill-upstream-variants requires --pinned-skills.')
    if args.config_dir and args.vault and not args.vault_path and args.apply:
        raise ValueError('Isolated --config-dir with --vault requires an explicit --vault-path. No real default vault changed.')
    if args.config_dir and args.external and args.apply:
        raise ValueError('Cannot isolate external Claude/plugin/MCP CLI installs with --config-dir. Test local files first; do external installs separately on the intended user account.')
    config=args.config_dir or Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude')
    config=config.expanduser().resolve()
    print('\nAI ENGINEER FULL CLAUDE MAP NI ARDIZUO — ASSISTED SETUP\n')
    print('Claude global config:',config)
    print('Mode:', 'APPLY' if args.apply else 'DRY RUN')
    print('Local definitions: 28 reviewed files + base rule + portable CLAUDE.md; Markdown headings use native emoji')
    print('Third-party clients need internet and may require provider sign-in.')
    # Fail on a conflicting personal vault template BEFORE modifying local Claude files.
    # Dry-run previews the same conflict checks, but never creates folders or notes.
    if args.vault:
        vault_check=(args.vault_path or Path.home()/'Documents/Claude-Dev-Vault').expanduser().resolve()
        install_templates(ROOT/'vault/templates', vault_check, False)
    print('\nLOCAL FILES')
    plan=local_plan(config)
    execute_plan(plan,args.apply)
    actions={}
    external_enabled=args.external
    if any([args.plugins,args.mcps,args.dashboard,args.superclaude]) and not external_enabled:
        print('\nNote: --external is required before any provider installation.')
    if args.pinned_superclaude:
        print('\nPINNED SUPERCLAUDE SOURCE DEFINITIONS (SAFE, NON-OVERWRITING)')
        command=[sys.executable,str(ROOT/'scripts/install-pinned-superclaude.py'),'--config-dir',str(config)]
        if args.upstream_variants:command.append('--upstream-variants')
        if args.apply:command.append('--apply')
        actions['pinned-superclaude']=run_external(command,'pinned 20 agents + 19 matching commands (11 variants opt-in)',False)
        if actions['pinned-superclaude']!='cli-success':
            raise RuntimeError('Pinned SuperClaude installation failed; review output and retry in a fresh test config.')
    if args.pinned_skills:
        print('\nPINNED THIRD-PARTY SKILL PROMPTS (SAFE, NON-OVERWRITING)')
        command=[sys.executable,str(ROOT/'scripts/install-pinned-skills.py'),'--config-dir',str(config)]
        if args.skill_upstream_variants:command.append('--upstream-variants')
        if args.apply:command.append('--apply')
        actions['pinned-skills']=run_external(command,'20 source-matched skill prompts; 5 upstream variants opt-in',False)
        if actions['pinned-skills']!='cli-success':
            raise RuntimeError('Pinned skill installation failed; review output and retry in a fresh test config.')
    if args.superclaude:
        print('\nSUPERCLAUDE — upstream installer (20 agent definitions and sc commands)')
        if not external_enabled: print('  SKIPPED; external installs not authorized')
        elif (config/'commands/sc/research.md').exists():print('  Already appears installed; skipped to avoid upstream overwrites.')
        else:
            if not shutil.which('pipx'): print('  pipx missing. Follow docs/installation/superclaude.md')
            else:
                actions['pipx-superclaude']=run_external(['pipx','install','superclaude'],'pipx install superclaude',not args.apply)
                if actions['pipx-superclaude'] in ('cli-success','planned'):
                    # SuperClaude installer manages its own files. Ask user to review its prompts.
                    actions['superclaude-config']=run_external(['superclaude','install'],'superclaude install (UPSTREAM MAY WRITE ~/.claude)',not args.apply)
    if args.plugins:
        print('\n12 OFFICIAL/THIRD-PARTY PLUGINS (WITH MARKETPLACE PREFLIGHT)')
        if not external_enabled:print('  SKIPPED; external installs not authorized')
        else:
            markets=known_marketplaces(mf, args.apply)
            actions.update({'marketplace:'+k:v for k,v in markets.items()})
            for entry in mf['plugins']:
                label=entry['id']
                market=label.split('@',1)[1]
                if markets.get(market) not in ('already-configured','cli-success','planned'):
                    print('  SKIPPED plugin',label,'because marketplace setup was not confirmed.')
                    actions['plugin:'+label]='marketplace-not-ready'
                    continue
                actions['plugin:'+label]=run_external(entry['install'],'plugin '+label,not args.apply)
    if args.mcps:
        print('\nNINE MCP SERVERS (AVAILABLE AUTOMATION PLUS MANUAL AUTH)')
        if not external_enabled:print('  SKIPPED; external installs not authorized')
        else:
            # Avoid printing or exporting any sensitive content from existing ~/.claude.json.
            existing=set()
            try:
                cfg=json.loads((Path.home()/'.claude.json').read_text(encoding='utf-8-sig'))
                existing=set(cfg.get('mcpServers',{}))
            except (OSError,ValueError,TypeError): pass
            for entry in mf['mcp']:
                name=entry['name']; k='mcp:'+name
                if name in existing:
                    print('  '+name+' — configured already (connectivity NOT verified)'); actions[k]='already-configured';continue
                if entry['automation']!='supported':
                    print('  '+name+' — requires manual credential/provider flow: integrations/mcp/README.md (server: '+name+')')
                    actions[k]='manual';continue
                missing=[p for p in entry.get('prerequisites',[]) if not shutil.which(p)]
                if missing:
                    print('  '+name+' — missing dependencies: '+', '.join(missing));actions[k]='missing-dependency';continue
                actions[k]=run_external(entry['argv'],'register MCP '+name,not args.apply)
    if args.hooks:
        print('\nHOOK REGISTRATION (five lifecycle hooks)')
        if not args.apply: print('  DRY RUN: node scripts/register-hooks.mjs --config-dir ...')
        elif shutil.which('node'):
            # This helper backs up settings.json and preserves existing entries.
            argv=['node',str(ROOT/'scripts/register-hooks.mjs'),'--config-dir',str(config),'--apply']
            actions['hook-registration']=run_external(argv,'register hooks',False)
        else: print('  Missing Node.js: no hook changes made.')
    if args.vault:
        print('\nOPTIONAL OBSIDIAN FOLDERS')
        vault=(args.vault_path or Path.home()/'Documents/Claude-Dev-Vault').expanduser().resolve()
        print('  Vault:',vault)
        if args.apply:
            # Validate existing templates BEFORE creating anything.
            install_templates(ROOT/'vault/templates', vault, False)
            for name in mf['memory']['folders']: (vault/name).mkdir(parents=True,exist_ok=True)
            install_templates(ROOT/'vault/templates', vault, True)
            print('  Vault folders/templates created or verified. No personal notes read or written.')
            print('  If this is not your default vault path, set CLAUDE_DEV_VAULT to this directory for future Claude sessions.')
        else:
            print('  DRY RUN: no directories created.')
            install_templates(ROOT/'vault/templates',vault,False)
    if args.dashboard:
        print('\nOPTIONAL CLAUDE MAP LOCAL DASHBOARD')
        print('  GUIDED ONLY: never overwrite or upgrade an existing global Claude Map installation automatically.')
        print('  npm claude-map@1.2.3 and the existing five-stage overlay require a separate compatibility rehearsal.')
        print('  See dashboard/claude-map/README.md. First run python scripts/install-dashboard.py --rehearse')
        print('  Then review backups and compatibility before any explicit live --apply.')
        actions['dashboard']='manual-rehearsal-required'
    print('\nFINAL STATUS')
    print('  Local files:', 'installed or identical' if args.apply else 'planned only')
    print('  Third-party actions:', len(actions),'tracked (0 exit is not provider authentication)')
    print('  Still pending: 4 unknown skill sources; 17 external direct-skill origins; 5 optional skill versions; 11 optional command versions; sidecars and runtime checks.')
    print('  Next: python scripts/coverage-doctor.py ; claude plugin list ; claude mcp list ; in Claude Code /mcp, /skills and /hooks.')
    print('  This setup never copies your personal auth secrets or private vault notes.')
    if any(v in ('failed','missing-dependency','marketplace-not-ready') for v in actions.values()):
        print('  Some optional external steps failed. Check provider guides; local install may still be valid.')

if __name__=='__main__':
    try:main()
    except Exception as e:
        print('ERROR:',e,file=sys.stderr)
        sys.exit(1)
