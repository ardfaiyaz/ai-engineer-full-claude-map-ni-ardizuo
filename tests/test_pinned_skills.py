"""Proof that static publisher skill sourcing is pinned, dry-run first and safe."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ardizuo_skills', ROOT/'scripts/install-pinned-skills.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class PinnedSkillsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lock=json.loads((ROOT/'setup/source-provenance-lock.json').read_text('utf-8'))
        cls.candidates=json.loads((ROOT/'setup/skill-source-candidates.json').read_text('utf-8'))['entries']

    def test_counts_and_safe_candidates(self):
        rows=[x for x in self.lock['entries'] if x['target'].startswith('skills/')]
        self.assertEqual(len(rows),29)
        self.assertEqual(len(mod.selected_rows(self.lock)),20)
        self.assertEqual(len(mod.selected_rows(self.lock,True)),25)
        self.assertEqual(len(self.candidates),19)
        self.assertEqual(sum(bool(x['candidateRepository']) for x in self.candidates),15)
        self.assertTrue(all(x['approvedForInstall'] is False for x in self.candidates))
        self.assertEqual(sum(x.get('promotedToSourceLock',False) for x in self.candidates),15)
        self.assertTrue(all(x['installPolicy']=='manual-source-review' for x in rows if x['comparison']=='UNMAPPED'))
        self.assertEqual(sum(x['installPolicy']=='automatic-reviewed-upstream' for x in rows),20)
        self.assertEqual(sum(x['installPolicy']=='opt-in-upstream-variant' for x in rows),5)
        self.assertEqual(sum(x['installPolicy']=='manual-source-review' for x in rows),4)
        self.assertNotIn('SHA256',json.dumps(rows))

    def test_dry_run_without_network_or_writes(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'test'
            result=mod.install(target, mod.selected_rows(self.lock), fetch=lambda _ : (_ for _ in ()).throw(AssertionError('Dry-run must not fetch')))
            self.assertEqual(result['new'],20)
            self.assertFalse(target.exists())

    def test_simulated_source_install_then_repeat(self):
        body=b'---\nname: test-skill\n---\n'
        row=copy.deepcopy(mod.selected_rows(self.lock)[0][0]);row['gitBlobSHA1']=mod.blob_sha(body)
        rows=[(row,mod.safe_name(row['target']))]
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'test'
            self.assertEqual(mod.install(cfg,rows,True,fetch=lambda r:body)['new'],1)
            self.assertEqual(mod.install(cfg,rows,True,fetch=lambda r:(_ for _ in ()).throw(AssertionError('Should not download identical files')))['new'],0)
            self.assertEqual((cfg/row['target']).read_bytes(),body)

    def test_atomic_on_fetch_checksum_failure(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'test'
            with self.assertRaisesRegex(ValueError,'Checksum mismatch'):
                mod.install(cfg,mod.selected_rows(self.lock),True,fetch=lambda _ :b'not-the-upstream-source')
            self.assertFalse(cfg.exists())

    def test_conflicting_personal_skills_stop_before_download(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'test';path=cfg/'skills/find-skills/SKILL.md';path.parent.mkdir(parents=True)
            path.write_text('custom protected local definition',encoding='utf-8')
            with self.assertRaisesRegex(RuntimeError,'Existing skill conflicts'):
                mod.install(cfg,mod.selected_rows(self.lock),True,fetch=lambda _ : (_ for _ in ()).throw(AssertionError('Must not download')))
            self.assertEqual(path.read_text(),'custom protected local definition')

    def test_conflicting_symlink_refused(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'target';out=Path(d)/'other';out.mkdir()
            cfg.mkdir()
            try:(cfg/'skills').symlink_to(out,target_is_directory=True)
            except OSError:self.skipTest('Symlinks unavailable on this host')
            with self.assertRaisesRegex(ValueError,'symlink'):
                mod.install(cfg,mod.selected_rows(self.lock))

    def test_source_sanitizers(self):
        for name in ['../SKILL.md', 'skills/../SKILL.md','/skills/a/SKILL.md','skills\\a\\SKILL.md','skills/a/SKILL.txt','skills/a/.secret','skills/a/b/SKILL.md']:
            with self.assertRaises(ValueError,msg=name):mod.safe_name(name)
        lock=copy.deepcopy(self.lock)
        row=next(r for r in lock['entries'] if r['target']=='skills/find-skills/SKILL.md')
        row['upstreamRepository']='random/fake-repository'
        with self.assertRaisesRegex(ValueError,'publisher'):mod.selected_rows(lock)

    def test_combined_installer_supports_isolated_preview(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'sandbox'
            run=subprocess.run([sys.executable,str(ROOT/'scripts/install-all.py'),'--config-dir',str(cfg),'--pinned-superclaude','--pinned-skills'],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stdout+run.stderr)
            self.assertIn('Pinned SuperClaude',run.stdout)
            self.assertIn('Publisher-pinned skills',run.stdout)
            self.assertFalse(cfg.exists())

    def test_variants_need_explicit_opt_in(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/'config'
            run=subprocess.run([sys.executable,str(ROOT/'scripts/install-all.py'),'--config-dir',str(cfg),'--skill-upstream-variants'],capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0)
            self.assertIn('requires --pinned-skills',run.stderr)
            self.assertFalse(cfg.exists())

    def test_crlf_comparison_does_not_silently_accept_content_changes(self):
        self.assertEqual(mod.normalize_eol(b'a\r\nb\r\n'),mod.normalize_eol(b'a\nb\n'))
        self.assertNotEqual(mod.normalize_eol(b'a\r\nchanged'),mod.normalize_eol(b'a\ncorrect'))

if __name__=='__main__':unittest.main()
