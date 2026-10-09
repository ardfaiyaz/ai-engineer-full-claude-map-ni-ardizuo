"""Regression tests for network-free planning and hash-verified pinned sourcing."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ar_pinned',ROOT/'scripts/install-pinned-superclaude.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class PinnedSuperClaudeTests(unittest.TestCase):
    def setUp(self):
        self.lock=json.loads((ROOT/'setup/source-provenance-lock.json').read_text())

    def test_counts_and_no_private_hashes(self):
        rows=self.lock['entries']
        self.assertEqual(len(rows),80)
        self.assertEqual({s:sum(x['comparison']==s for x in rows) for s in ('EXACT_BYTE_MATCH','DIFFERENT_CONTENT','UNMAPPED','TEXT_MATCH_LINE_ENDINGS_ONLY')},{'EXACT_BYTE_MATCH':45,'DIFFERENT_CONTENT':16,'UNMAPPED':4,'TEXT_MATCH_LINE_ENDINGS_ONLY':15})
        selected=mod.allowed_rows(self.lock)
        self.assertEqual(len(selected),39)
        self.assertEqual(len([1 for row,_ in selected if row['target'].startswith('agents/')]),20)
        self.assertEqual(len(mod.allowed_rows(self.lock,True)),50)
        self.assertEqual(sum(row['installPolicy']=='opt-in-upstream-variant' and row['target'].startswith('commands/') for row in rows),11)
        self.assertEqual(sum(row['installPolicy']=='docs-only' for row in rows),1)
        self.assertNotIn('SHA256', str(rows))
        self.assertNotIn('Origin', str(rows))

    def test_local_dry_run_no_network_no_writes(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'empty'
            def fail(_):raise AssertionError('No download during dry run')
            status=mod.execute(cfg,mod.allowed_rows(self.lock),apply=False,fetch=fail)
            self.assertEqual(status['new'],39)
            self.assertFalse(cfg.exists())

    def test_conflicts_stop_before_download(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'config';(cfg/'agents').mkdir(parents=True)
            (cfg/'agents/backend-architect.md').write_text('personal version')
            def fail(_):raise AssertionError('Must stop before fetching')
            with self.assertRaisesRegex(RuntimeError,'Existing files differ'):
                mod.execute(cfg,mod.allowed_rows(self.lock),apply=True,fetch=fail)
            self.assertEqual((cfg/'agents/backend-architect.md').read_text(),'personal version')
            self.assertFalse((cfg/'agents/business-panel-experts.md').exists())

    def test_verify_digest_before_any_write(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'config'
            with self.assertRaisesRegex(ValueError,'Hash mismatch'):
                mod.execute(cfg,mod.allowed_rows(self.lock),apply=True,fetch=lambda row:b'wrong')
            self.assertFalse(cfg.exists())

    def test_one_file_write_and_idempotency(self):
        data=b'---\nname: test\n---\n'
        blob=mod.git_blob_sha1(data)
        row=copy.deepcopy(mod.allowed_rows(self.lock)[0][0]);row['gitBlobSHA1']=blob
        selected=[(row,mod.safe_relative(row['target']))]
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'config'
            self.assertEqual(mod.execute(cfg,selected,True,fetch=lambda row:data)['new'],1)
            self.assertEqual(mod.execute(cfg,selected,True,fetch=lambda row:(_ for _ in ()).throw(AssertionError('unexpected network')))['identical'],1)
            self.assertEqual((cfg/row['target']).read_bytes(),data)

    def test_manifest_guards(self):
        for bad in ['../.claude.json','C:/secret','/tmp/foo','agents/../evil.md','agents\\a.md','settings.json']:
            with self.assertRaises(ValueError,msg=bad):mod.safe_relative(bad)
        dirty=copy.deepcopy(self.lock)
        dirty['entries'][0]['sourceFilePath']='src/superclaude/agents/../sneaky.md'
        with self.assertRaises(ValueError):mod.allowed_rows(dirty)

    def test_download_not_used_for_dry_run_cli(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'config'
            run=subprocess.run([sys.executable,str(ROOT/'scripts/install-pinned-superclaude.py'),'--config-dir',str(cfg)],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertIn('DRY RUN:',run.stdout)
            self.assertFalse(cfg.exists())

if __name__=='__main__': unittest.main()
