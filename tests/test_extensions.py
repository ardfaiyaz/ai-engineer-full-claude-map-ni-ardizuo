"""Offline checks for the opt-in extension catalog and installer."""
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


class ExtensionCatalogTests(unittest.TestCase):
    def test_catalog_rows_match_master_inventory(self):
        expected={'skills':range(63,83),'mcps':range(10,16),'guardrails':range(6,8),
                  'agentCollections':range(22,26),'extensionSystems':range(13,21),
                  'commands':range(32,46),'tools':range(1,21)}
        for key,rows in expected.items():
            self.assertEqual([r['row'] for r in CATALOG[key]],list(rows),key)
        self.assertEqual(sum(len(CATALOG[k]) for k in expected),74)

    def test_references_resolve_and_ids_are_unique(self):
        ids=[p['id'] for p in CATALOG['packages']]
        self.assertEqual(len(ids),len(set(ids)))
        for key in ('skills','mcps','guardrails','agentCollections','extensionSystems','commands','tools'):
            for row in CATALOG[key]:
                self.assertTrue(row['package'] is None or row['package'] in ids,(key,row))
        markets={m['id'] for m in CATALOG['marketplaces']}
        for p in CATALOG['packages']:
            if p['kind']=='plugin':
                self.assertIn(p['pluginId'].split('@',1)[1],markets,p['id'])
            if p['kind'] in ('guided','reference'):
                self.assertTrue(p['docs'].startswith('https://github.com/'),p['id'])

    def test_executable_commands_are_safe_argv(self):
        for p in CATALOG['packages']:
            if p['kind']!='mcp':continue
            self.assertEqual(p['argv'][:5],['claude','mcp','add','--scope','user'])
            for arg in p['argv']:
                self.assertIsInstance(arg,str)
                self.assertFalse(re.search(r'[;&|`$<>]',arg),arg)

    def test_no_secrets_personal_paths_or_social_tooling(self):
        text=(ROOT/'setup/extension-catalog.json').read_text(encoding='utf-8').lower()
        for forbidden in ('ghp_','bearer ','c:\\users\\melthon','vidiq','tiktok','instagram'):
            self.assertNotIn(forbidden,text)
        self.assertIsNone(re.search(r'\b(sk|fc)-[a-z0-9]{12,}',text),'API-key-shaped literal')
        installable=' '.join(p.get('pluginId','')+p.get('name','') for p in CATALOG['packages']).lower()
        for social in ('twitter','facebook','social','tweet'):
            self.assertNotIn(social,installable)

    def test_policy_keeps_extensions_out_of_all(self):
        self.assertFalse(CATALOG['policy']['defaultInstall'])
        self.assertFalse(CATALOG['policy']['includedInAllSwitch'])
        ps1=(ROOT/'scripts/install-all.ps1').read_text(encoding='utf-8')
        all_line=next(line for line in ps1.splitlines() if line.startswith('if ($All)'))
        self.assertNotIn('Extensions',all_line)


class ExtensionSelectionTests(unittest.TestCase):
    def test_priority_is_the_ten_item_shortlist(self):
        self.assertEqual([p['id'] for p in ext.resolve(CATALOG,'priority')],
            ['codex','claude-hud','tob-differential-review','ponytail','firecrawl',
             'probity','agentation','mcp-inspector','beads','mcp-use'])

    def test_all_excludes_alternatives(self):
        chosen=ext.resolve(CATALOG,'all')
        self.assertFalse(any(p.get('alternative') for p in chosen))
        self.assertEqual(len(chosen),sum(1 for p in CATALOG['packages'] if not p.get('alternative')))

    def test_exclusive_groups_and_unknown_ids_are_refused(self):
        with self.assertRaisesRegex(ValueError,'tdd-enforcement'):
            ext.resolve(CATALOG,'probity,tdd-guard')
        with self.assertRaisesRegex(ValueError,'orchestration'):
            ext.resolve(CATALOG,'gstack,compound-engineering')
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
            self.assertIn('not executed by this installer',r.stdout)
            self.assertEqual(list(Path(tmp).iterdir()),[])

    def test_status_reads_names_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)
            (cfg/'settings.json').write_text('{"enabledPlugins":{"codex@openai-codex":true,"claude-hud@claude-hud":false}}')
            home=cfg/'home.json'
            home.write_text('{"mcpServers":{"n8n-mcp":{"env":{"N8N_API_KEY":"DO_NOT_OUTPUT_SECRET"}}}}')
            r=self.run_script('--status','--json','--config-dir',str(cfg),'--home-config',str(home))
            self.assertEqual(r.returncode,0,r.stderr)
            data=json.loads(r.stdout)
            self.assertEqual(data['codex'],'enabled')
            self.assertEqual(data['claude-hud'],'not-enabled')
            self.assertEqual(data['n8n-mcp'],'registered')
            self.assertNotIn('DO_NOT_OUTPUT_SECRET',r.stdout)

    def test_already_enabled_plugin_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)
            (cfg/'settings.json').write_text('{"enabledPlugins":{"codex@openai-codex":true}}')
            r=self.run_script('--select','codex','--config-dir',str(cfg))
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('ALREADY ENABLED: codex@openai-codex',r.stdout)
            self.assertNotIn('MARKETPLACES',r.stdout)

    def test_install_all_requires_external_for_extensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=subprocess.run([sys.executable,str(ROOT/'scripts/install-all.py'),'--config-dir',str(Path(tmp)/'cfg'),'--extensions','priority'],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIn('--external is required',r.stdout)
            self.assertIn('SKIPPED; external installs not authorized',r.stdout)


if __name__=='__main__':unittest.main()
