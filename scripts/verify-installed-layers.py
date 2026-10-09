#!/usr/bin/env python3
"""Read-only audit of Ardizuo-defined files in one Claude configuration.

Checks only names, paths, and hook command basenames. Does not read MCP tokens,
open a browser, invoke Claude, execute hooks, or claim provider authentication.
"""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
HOOKS = {
    'UserPromptSubmit': 'skill-gate-check.mjs',
    'SessionStart': 'vault-session-init.mjs',
    'PostToolUse': ('log-to-vault.mjs','dead-code-check.mjs'),
    'Stop': 'stop-vault-log.mjs',
}

def _read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def expected(variants=False):
    owned = _read_json(ROOT/'setup/development-assets.json')['filePaths']
    entries = _read_json(ROOT/'setup/source-provenance-lock.json')['entries']
    files = {p.replace('\\', '/') for p in owned}
    for e in entries:
        p = e['target']
        if e['installPolicy']=='automatic-reviewed-upstream' or (variants and e['installPolicy']=='opt-in-upstream-variant'):
            if p.startswith(('agents/','skills/','commands/sc/')) and not p.endswith('/README.md'):
                files.add(p)
    files.update(['rules/ardizuo-development.md','CLAUDE.md'])
    files.update('assets/lucide/'+p.name for p in (ROOT/'ardizuo-plugin/assets/lucide').glob('*.svg'))
    return sorted(files)

def audit(config, variants=False, vault=None):
    files = expected(variants)
    found = sorted(p for p in files if (config/p).is_file() and not (config/p).is_symlink())
    missing = sorted(set(files)-set(found))
    by_layer={}
    for bucket in ('agents/','skills/','commands/','hooks/','rules/','workflows/','assets/'):
        name=bucket[:-1]
        f=[p for p in files if p.startswith(bucket)]
        by_layer[name]={'present':sum(p in found for p in f),'expected':len(f)}
    by_layer['global-context']={'present':int('CLAUDE.md' in found),'expected':1}
    hooked={}
    cfg_file=config/'settings.json'
    err=None
    if cfg_file.is_file():
        try:
            settings=_read_json(cfg_file)
            event_dict=settings.get('hooks',{}) if isinstance(settings,dict) else {}
            if not isinstance(event_dict,dict): raise ValueError('Invalid hooks configuration')
            for event,filespec in HOOKS.items():
                records=event_dict.get(event,[])
                if not isinstance(records,list):raise ValueError('Invalid event hooks configuration')
                commands=[str(cmd.get('command','')).replace('\\','/').casefold() for block in records if isinstance(block,dict) for cmd in block.get('hooks',[]) if isinstance(cmd,dict)]
                for basename in ((filespec,) if isinstance(filespec,str) else filespec):
                    hooked[basename]=any('/'+basename.casefold() in c or c.endswith(basename.casefold()) for c in commands)
        except (OSError,UnicodeError,ValueError,TypeError) as exc:
            err=f'Hook settings could not be interpreted ({type(exc).__name__}); no secret values printed'
    else:
        for v in HOOKS.values():
            for basename in ((v,) if isinstance(v,str) else v):hooked[basename]=False
    vault_result=None
    if vault is not None:
        # Check only published folder/template names, never list personal note files.
        dirs=['Sessions','Learnings','ADRs','Dispatch-Logs','PRDs','Diagrams','Projects','Templates']
        templates=sorted(p.name for p in (ROOT/'vault/templates').glob('*.md'))
        vault_result={'foldersFound':sum((vault/d).is_dir() for d in dirs),'foldersExpected':len(dirs),
                      'templatesFound':sum((vault/'Templates'/n).is_file() for n in templates),'templatesExpected':len(templates),
                      'lucideIconsFound':sum((vault/'.ardizuo-icons'/p.name).is_file() for p in (ROOT/'vault/.ardizuo-icons').glob('*.svg'))}
    return {'configDir':str(config),'expectedLocalFiles':len(files),'presentLocalFiles':len(found),
            'missing':missing,'byLayer':by_layer,'hooksRegistered':hooked,'hookSettingsError':err,
            'vault':vault_result,'providers':'NOT TESTED: plugin and MCP connections require Claude CLI and interactive authentication',
            'runtime':'NOT TESTED: static presence and registration do not prove skill execution'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--config-dir',type=Path,default=Path(os.environ.get('CLAUDE_CONFIG_DIR') or Path.home()/'.claude'))
    p.add_argument('--upstream-variants',action='store_true',help='Expect 11 command and 5 skill opt-in upstream versions')
    p.add_argument('--vault-path',type=Path,help='Read-only check of your approved vault folders/templates (not note content)')
    p.add_argument('--json',action='store_true')
    p.add_argument('--strict-local',action='store_true',help='Nonzero exit only if expected installed files are missing; does not assert all 62 direct skills')
    p.add_argument('--require-hooks',action='store_true',help='When strict, require five configured lifecycle handlers')
    args=p.parse_args()
    report=audit(args.config_dir.expanduser().resolve(), args.upstream_variants, args.vault_path.expanduser().resolve() if args.vault_path else None)
    if args.json:print(json.dumps(report,indent=2))
    else:
        print('ARDIZUO INSTALLED LAYERS — READ ONLY (not provider connectivity or runtime proof)')
        print('Claude config:',report['configDir'])
        for n,x in report['byLayer'].items():print(f'  {n:17} {x["present"]}/{x["expected"]} expected package files')
        print(f'  Hook definitions registered: {sum(report["hooksRegistered"].values())}/{len(report["hooksRegistered"])}')
        if report['hookSettingsError']:print('  ',report['hookSettingsError'])
        if report['vault']:print('  Vault folders/templates:',report['vault']['foldersFound'],'/',report['vault']['foldersExpected'],';',report['vault']['templatesFound'],'/',report['vault']['templatesExpected'])
        for file in report['missing']:print('  MISSING:',file)
        print(report['providers']);print(report['runtime'])
        print('See scripts/release-audit.py for the 62-skill/31-command reference completeness gate.')
    if args.strict_local and (report['missing'] or (args.require_hooks and (not all(report['hooksRegistered'].values()) or report['hookSettingsError']))):return 2
    return 0

if __name__=='__main__':sys.exit(main())
