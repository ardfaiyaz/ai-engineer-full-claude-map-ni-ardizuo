#!/usr/bin/env python3
"""Audit declared GitHub package installability; does not read user configs or call providers."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]

def audit():
    m=json.loads((ROOT/'setup/release-coverage.json').read_text(encoding='utf-8'))
    p=json.loads((ROOT/'setup/source-provenance-lock.json').read_text(encoding='utf-8'))
    local=json.loads((ROOT/'setup/development-assets.json').read_text(encoding='utf-8'))
    ref=json.loads((ROOT/'setup/reference-inventory.json').read_text(encoding='utf-8'))
    entries=p['entries']; owned=set(local['filePaths'])
    if len(owned)!=28: raise ValueError('Changed owned manifest: inspect before release')
    auto={e['target'] for e in entries if e['installPolicy']=='automatic-reviewed-upstream'}
    opt={e['target'] for e in entries if e['installPolicy']=='opt-in-upstream-variant'}
    def name(target):
        v=target.split('/')[-1]
        return v[:-3] if v.endswith('.md') else target.split('/')[1]
    agent_auto={name(x) for x in auto if x.startswith('agents/')}
    skill_auto={x.split('/')[1] for x in auto if x.startswith('skills/')}
    command_auto={name(x) for x in auto if x.startswith('commands/sc/')}
    local_agents={name(x) for x in owned if x.startswith('agents/')}
    local_skills={x.split('/')[1] for x in owned if x.startswith('skills/')}
    local_commands={name(x) for x in owned if x.startswith('commands/')}
    manual=m['notAutomaticallyReproduced']['directSkillsRequiringVerifiedOriginOrExternalSource']
    unknown=m['notAutomaticallyReproduced']['directSkillsWithUnknownSafeSource']
    skill_opt=m['optInUpstreamVersions']['skills']
    cmd_opt=m['optInUpstreamVersions']['commands']
    if (set(ref['agents'])!=agent_auto|local_agents or
        set(ref['globalSkills'])!=skill_auto|local_skills|set(manual)|set(unknown)|set(skill_opt) or
        set(ref['commands'])!=command_auto|local_commands|set(cmd_opt)|{'README'}):
        raise ValueError('Release coverage does not exactly partition the reference inventory')
    if (len(m['providerLayers']['plugins']),len(m['providerLayers']['targetMCPs']))!=(12,9):
        raise ValueError('Provider manifest count drift')
    required=[ROOT/'global-config/CLAUDE.md',ROOT/'docs/installation/reproducibility-matrix.md',ROOT/'docs/installation/full-setup.md']
    if any(not f.is_file() for f in required):raise ValueError('Missing portable context or release documentation')
    return {'agentNames':{'default':len(local_agents|agent_auto),'target':len(ref['agents'])},
            'directSkillNames':{'default':len(local_skills|skill_auto),'withUpstreamVariants':len(local_skills|skill_auto|set(skill_opt)),'target':len(ref['globalSkills']),'externalUnverified':len(manual),'unknownSource':len(unknown)},
            'executableCommandNames':{'default':len(local_commands|command_auto),'withUpstreamVariants':len(local_commands|command_auto|set(cmd_opt)),'target':len(ref['commands'])-1},
            'plugins':{'documented':12,'freshInstallationVerified':False},
            'targetMCPs':{'documented':9,'freshConnectionVerified':False},
            'hooks':{'sourceScriptsIncluded':5,'runtimeVerified':False},
            'dashboard':{'fiveStageRehearsalDocumented':True,'freshRuntimeVerified':False},
            'freshWindowsAllLayersVerified':False}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',action='store_true',help='Machine-readable static report')
    ap.add_argument('--strict',action='store_true',help='Exit code 2 until every direct reference and fresh-runtime gate is truly met')
    args=ap.parse_args()
    r=audit()
    if args.json:print(json.dumps(r,indent=2))
    else:
        print('ARDIZUO PUBLIC PACKAGE RELEASE AUDIT — STATIC, OFFLINE')
        for label,key in [('Agents','agentNames'),('Skills','directSkillNames'),('Executable commands','executableCommandNames')]:
            g=r[key]
            print(f"  {label:20} default {g['default']}/{g['target']}" + (f"; optional upstream {g['withUpstreamVariants']}/{g['target']}" if 'withUpstreamVariants' in g else ''))
        print('  Plugins: 12 documented / CLI install option; fresh connection not proven')
        print('  MCPs: 9 documented / supported registration & manual auth; fresh connection not proven')
        print('  Hooks: 5 included, opt-in settings registration; execution not proven')
        print('  Dashboard: five-stage sandbox rehearsal + reference browser check, not clean-device proof')
        print('  Blockers: 4 unknown skill origins, 17 external direct-skill sources, 5 modified skill variants, 11 modified commands, sidecars/runtime/rollback')
        print('  Credentials, sessions, and private vault data are deliberately not bundled.')
    complete=(r['agentNames']['default']==r['agentNames']['target'] and
        r['directSkillNames']['default']==r['directSkillNames']['target'] and
        r['executableCommandNames']['default']==r['executableCommandNames']['target'] and
        r['freshWindowsAllLayersVerified'])
    if args.strict and not complete:return 2
    return 0
if __name__=='__main__':
    try:sys.exit(main())
    except Exception as e:print('AUDIT ERROR:',str(e),file=sys.stderr);sys.exit(1)
