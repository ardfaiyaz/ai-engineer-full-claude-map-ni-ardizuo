"""Offline regression checks for marketplace, vault template and exact-name audit."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(filename, alias):
    spec = importlib.util.spec_from_file_location(alias, ROOT/'scripts'/filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

installer = load('install-all.py','ar_install_completion')
coverage = load('coverage-doctor.py','ar_coverage_completion')

class CompletionSprintTests(unittest.TestCase):
    def test_sources_and_no_credentials_in_manifest(self):
        data=json.loads((ROOT/'setup/full-stack.json').read_text())
        markets={e['id']:e['source'] for e in data['marketplaces']}
        self.assertEqual(markets['anthropic-agent-skills'],'anthropics/skills')
        self.assertEqual(markets['ralph-marketplace'],'snarktank/ralph')
        self.assertEqual(markets['morph'],'morphllm/morph-claude-code-plugin')
        self.assertEqual(len(markets),4)
        github=next(x for x in data['mcp'] if x['name']=='github')
        self.assertEqual(github['automation'],'supported')
        self.assertIn('GITHUB_OAUTH_CALLBACK_PORT=8085',github['argv'])
        self.assertNotIn('PAT', ' '.join(github['argv']))
        self.assertNotIn('ghp_', ' '.join(github['argv']))

    def test_all_reference_counts_and_no_social_tooling(self):
        data=json.loads((ROOT/'setup/reference-inventory.json').read_text())
        self.assertEqual([len(data[k]) for k in ('agents','globalSkills','commands')],[21,62,32])
        self.assertEqual(len(data['plugins']),12)
        self.assertTrue(all(x not in str(data).lower() for x in ('vidiq','tiktok','instagram')))

    def test_coverage_never_equates_cache_with_installed(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)/'config'
            (cfg/'plugins/cache/foo/test-plugin/1.0/skills/owasp-security').mkdir(parents=True)
            (cfg/'plugins/cache/foo/test-plugin/1.0/skills/owasp-security/SKILL.md').write_text('test only')
            (cfg/'agents').mkdir(parents=True)
            (cfg/'agents/diagram-architect.md').write_text('test')
            (cfg/'skills/reuse-audit').mkdir(parents=True)
            (cfg/'skills/reuse-audit/SKILL.md').write_text('test')
            home=Path(tmp)/'.claude.json';home.write_text('{"mcpServers":{"serena":{"secret":"DO_NOT_OUTPUT_SECRET"}}}')
            info=coverage.inspect(cfg,home,Path(tmp)/'vault')
            self.assertEqual(info['agents']['diagram-architect'],'direct')
            self.assertEqual(info['skills']['reuse-audit'],'direct')
            self.assertEqual(info['skills']['owasp-security'],'cached-unconfirmed')
            self.assertEqual(info['mcps']['serena'],'registered-user-scope')
            self.assertNotIn('DO_NOT_OUTPUT_SECRET',json.dumps(info))
            (cfg/'settings.json').write_text('{"enabledPlugins":{"test-plugin@foo":true}}')
            info=coverage.inspect(cfg,home,Path(tmp)/'vault')
            self.assertEqual(info['skills']['owasp-security'],'enabled-plugin-cache')

    def test_coverage_json_and_strict_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg=Path(tmp)/'config'
            cmd=[sys.executable,str(ROOT/'scripts/coverage-doctor.py'),'--config-dir',str(cfg),'--home-config',str(Path(tmp)/'none.json'),'--vault-path',str(Path(tmp)/'empty')]
            a=subprocess.run(cmd+['--json'],capture_output=True,text=True)
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertEqual(len(json.loads(a.stdout)['agents']),21)
            b=subprocess.run(cmd+['--strict'],capture_output=True,text=True)
            self.assertEqual(b.returncode,2)

    def test_vault_templates_do_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            vault=Path(tmp)/'vault'
            installer.install_templates(ROOT/'vault/templates',vault,False)
            self.assertFalse(vault.exists())
            installer.install_templates(ROOT/'vault/templates',vault,True)
            self.assertTrue((vault/'Templates/ADR.md').exists())
            installer.install_templates(ROOT/'vault/templates',vault,True)
            (vault/'Templates/ADR.md').write_text('user-customized',encoding='utf8')
            with self.assertRaisesRegex(RuntimeError,'Conflicting'):
                installer.install_templates(ROOT/'vault/templates',vault,True)
            self.assertEqual((vault/'Templates/ADR.md').read_text(),'user-customized')

    def test_private_review_defaults_to_no_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            config=Path(tmp)/'config';(config/'agents').mkdir(parents=True)
            (config/'agents/system-architect.md').write_text('private example')
            target=Path(tmp)/'private-review'
            cmd=[sys.executable,str(ROOT/'scripts/prepare-private-review.py'),'--config-dir',str(config),'--output',str(target)]
            a=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertIn('system-architect.md',a.stdout)
            self.assertFalse(target.exists())
            b=subprocess.run(cmd+['--apply'],capture_output=True,text=True)
            self.assertEqual(b.returncode,0,b.stderr)
            self.assertEqual((target/'agents/system-architect.md').read_text(),'private example')
            c=subprocess.run(cmd+['--apply'],capture_output=True,text=True)
            self.assertNotEqual(c.returncode,0)

    def test_dry_run_marketplace_list_no_install(self):
        stack=json.loads((ROOT/'setup/full-stack.json').read_text())
        self.assertEqual(len(installer.known_marketplaces(stack,False)),4)

if __name__ == '__main__': unittest.main()
