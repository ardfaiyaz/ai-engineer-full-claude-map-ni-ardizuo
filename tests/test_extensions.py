"""Offline checks for the extended-stack catalog and installer."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
CATALOG=json.loads((ROOT/'setup/extension-catalog.json').read_text(encoding='utf-8'))
spec=importlib.util.spec_from_file_location('ar_install_extensions',ROOT/'scripts/install-extensions.py')
ext=importlib.util.module_from_spec(spec)
spec.loader.exec_module(ext)
PACKAGES={p['id']:p for p in CATALOG['packages']}


class ExtensionCatalogTests(unittest.TestCase):
    def test_catalog_rows_match_master_inventory(self):
        expected={'skills':range(63,83),'mcps':range(10,16),'guardrails':range(6,8),
                  'agentCollections':range(22,26),'extensionSystems':range(13,21),
                  'commands':range(32,46),'tools':range(1,21)}
        for key,rows in expected.items():
            self.assertEqual([r['row'] for r in CATALOG[key]],list(rows),key)
        self.assertEqual(sum(len(CATALOG[k]) for k in expected),74)

    def test_references_resolve_and_ids_are_unique(self):
        self.assertEqual(len(PACKAGES),len(CATALOG['packages']))
        for key in ('skills','mcps','guardrails','agentCollections','extensionSystems','commands','tools'):
            for row in CATALOG[key]:
                self.assertTrue(row['package'] is None or row['package'] in PACKAGES,(key,row))
        markets={m['id'] for m in CATALOG['marketplaces']}
        for p in CATALOG['packages']:
            if p['kind']=='plugin':
                for plugin_id in p['pluginIds']:
                    self.assertIn(plugin_id.split('@',1)[1],markets,plugin_id)
            if p['kind'] in ('manual','project'):
                self.assertTrue(p['docs'].startswith('https://github.com/'),p['id'])

    def test_every_catalog_entry_is_installed_or_explained(self):
        kinds={p['kind'] for p in CATALOG['packages']}
        self.assertLessEqual(kinds,{'plugin','mcp','cli','pinned-files','git-setup','manual','project'})
        unpackaged=[r['name'] for k in ('tools',) for r in CATALOG[k] if r['package'] is None]
        self.assertEqual(sorted(unpackaged),['Awesome Claude Code','Awesome MCP Servers','MCP Reference Servers','MCP TypeScript SDK'])

    def test_executable_commands_are_safe_argv(self):
        for p in CATALOG['packages']:
            argvs=[p['argv']] if p['kind']=='mcp' else p['commands'] if p['kind']=='cli' else []
            if p['kind']=='mcp':
                self.assertEqual(p['argv'][:5],['claude','mcp','add','--scope','user'])
            if p['kind']=='cli':
                self.assertIn(p['commands'][0][0],('npm','uv','winget'))
            for argv in argvs:
                for arg in argv:
                    self.assertIsInstance(arg,str)
                    self.assertFalse(re.search(r'[;&|`$<>]',arg),arg)

    def test_pinned_files_are_commit_and_hash_pinned(self):
        for p in CATALOG['packages']:
            if p['kind']!='pinned-files':continue
            self.assertRegex(p['commit'],r'^[0-9a-f]{40}$')
            for item in p['files']:
                self.assertRegex(item['blobSha'],r'^[0-9a-f]{40}$')
                target=item.get('target',item['path'])
                self.assertTrue(target.startswith('skills/'),target)
                self.assertNotIn('..',target)

    def test_no_secrets_personal_paths_or_social_tooling(self):
        text=(ROOT/'setup/extension-catalog.json').read_text(encoding='utf-8').lower()
        for forbidden in ('ghp_','c:\\users\\melthon','vidiq','tiktok','instagram'):
            self.assertNotIn(forbidden,text)
        self.assertIsNone(re.search(r'\b(sk|fc)-[a-z0-9]{12,}',text),'API-key-shaped literal')
        installable=' '.join(i for p in CATALOG['packages'] for i in p.get('pluginIds',[])+[p.get('name','')]).lower()
        for social in ('twitter','facebook','social','tweet'):
            self.assertNotIn(social,installable)
        self.assertEqual(len(PACKAGES['wshobson-agents']['pluginIds']),92)

    def test_extended_stack_is_part_of_all(self):
        self.assertTrue(CATALOG['policy']['defaultInstall'])
        self.assertTrue(CATALOG['policy']['includedInAllSwitch'])
        ps1=(ROOT/'scripts/install-all.ps1').read_text(encoding='utf-8')
        all_line=next(line for line in ps1.splitlines() if line.startswith('if ($All)'))
        self.assertIn("$Extensions = 'all'",all_line)


class ExtensionSelectionTests(unittest.TestCase):
    def test_priority_group(self):
        self.assertEqual([p['id'] for p in ext.resolve(CATALOG,'priority')],
            ['codex','codex-cli','claude-hud','tob-differential-review','ponytail','firecrawl','agentation',
             'probity','beads','beads-cli','mcp-use','mcp-inspector'])

    def test_all_includes_every_package(self):
        self.assertEqual(len(ext.resolve(CATALOG,'all')),len(CATALOG['packages']))

    def test_overlaps_are_reported_not_refused(self):
        chosen=ext.resolve(CATALOG,'probity,tdd-guard')
        self.assertEqual(ext.overlaps(chosen),{'tdd-enforcement':['probity','tdd-guard']})
        with self.assertRaisesRegex(ValueError,'Unknown'):
            ext.resolve(CATALOG,'not-a-real-extension')


class ExtensionInstallerTests(unittest.TestCase):
    def run_script(self,*args):
        return subprocess.run([sys.executable,str(ROOT/'scripts/install-extensions.py'),*args],capture_output=True,text=True)

    def test_dry_run_never_executes(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=self.run_script('--select','all','--config-dir',tmp)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('DRY RUN',r.stdout)
            self.assertIn('WOULD RUN',r.stdout)
            self.assertNotIn('RUNNING',r.stdout)
            self.assertIn('printed, not executed',r.stdout)
            self.assertEqual(list(Path(tmp).iterdir()),[])

    def test_status_reads_names_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)
            first=PACKAGES['wshobson-agents']['pluginIds'][0]
            (cfg/'settings.json').write_text(json.dumps({'enabledPlugins':{'claude-hud@claude-hud':True,'codex@openai-codex':False,first:True}}))
            home=cfg/'home.json'
            home.write_text('{"mcpServers":{"n8n-mcp":{"env":{"N8N_API_KEY":"DO_NOT_OUTPUT_SECRET"}}}}')
            r=self.run_script('--status','--json','--config-dir',str(cfg),'--home-config',str(home))
            self.assertEqual(r.returncode,0,r.stderr)
            data=json.loads(r.stdout)
            self.assertEqual(data['claude-hud'],'enabled')
            self.assertEqual(data['codex'],'not-enabled')
            self.assertEqual(data['wshobson-agents'],'partial 1/92')
            self.assertEqual(data['n8n-mcp'],'registered')
            self.assertEqual(data['karpathy-skills'],'missing')
            self.assertNotIn('DO_NOT_OUTPUT_SECRET',r.stdout)

    def test_already_enabled_plugin_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)
            (cfg/'settings.json').write_text('{"enabledPlugins":{"codex@openai-codex":true}}')
            r=self.run_script('--select','codex','--config-dir',str(cfg))
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('ALREADY ENABLED: codex@openai-codex',r.stdout)
            self.assertNotIn('MARKETPLACES',r.stdout)

    def test_pinned_files_verify_before_writing(self):
        package=PACKAGES['karpathy-skills']
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)
            def bad_fetch(row):
                if row['sourceFilePath'].endswith('karpathy-verification/SKILL.md'):
                    raise ValueError('Publisher checksum mismatch')
                return b'ok'
            actions={}
            ext.install_pinned([package],cfg,True,actions,fetch=bad_fetch)
            self.assertEqual(actions['files:karpathy-skills'],'failed')
            self.assertEqual(list(cfg.iterdir()),[],'nothing may be written when any file fails verification')
            ext.install_pinned([package],cfg,True,actions,fetch=lambda row:b'ok')
            self.assertEqual(actions['files:karpathy-skills'],'cli-success')
            self.assertEqual(len([x for x in cfg.rglob('*') if x.is_file()]),len(package['files']))
            ext.install_pinned([package],cfg,True,actions,fetch=lambda row:self.fail('no refetch'))
            self.assertEqual(actions['files:karpathy-skills'],'already-installed')

    def test_install_all_requires_external_for_extensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=subprocess.run([sys.executable,str(ROOT/'scripts/install-all.py'),'--config-dir',str(Path(tmp)/'cfg'),'--extensions','all'],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('--external is required',r.stdout)
            self.assertIn('SKIPPED; external installs not authorized',r.stdout)


if __name__=='__main__':unittest.main()
