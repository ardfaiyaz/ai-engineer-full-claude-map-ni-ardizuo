#!/usr/bin/env python3
"""Safely preview or apply the Ardizuo Development Hub overlay to Claude Map.

Windows-compatible npm CLI resolution. Dry run checks the initial scaffold
anchors without writing any files. Subsequent overlay stages remain version-
sensitive; a successful preview is NOT a guarantee that --apply will succeed.
"""
import argparse
import datetime
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PATCH = ROOT / 'dashboard' / 'claude-map' / 'patches'


def find_cli(name, windows=None):
    """Resolve full CLI path: Windows npm lives at npm.cmd, not npm.exe."""
    if windows is None:
        windows = os.name == 'nt'
    suffixes = ('.cmd', '.exe', '') if windows else ('',)
    for suffix in suffixes:
        found = shutil.which(name + suffix)
        if found:
            return found
    raise RuntimeError(
        f'Cannot find {name} in PATH. In PowerShell run: Get-Command {name}. '
        'Or supply --map-root with the installed Claude Map folder.'
    )


def detect_map_root():
    npm = find_cli('npm')
    try:
        proc = subprocess.run([npm, 'root', '-g'], capture_output=True,
                              text=True, timeout=20, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError('Unable to run npm root -g. Provide --map-root explicitly.') from exc
    if proc.returncode or not proc.stdout.strip():
        raise RuntimeError('npm root -g failed. Run it in PowerShell and pass '
                           '--map-root to this script. No changes made.')
    return Path(proc.stdout.strip()) / 'claude-map'


def scaffold_preflight(app_file):
    """Validate initial version-sensitive anchors with no mutations."""
    spec = importlib.util.spec_from_file_location('ardizuo_devhub_scaffold',
                                                  PATCH / 'bootstrap_devhub.py')
    if spec is None or spec.loader is None:
        raise RuntimeError('Missing bundled bootstrap_devhub.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        _new_content, changed = module.patch(app_file.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise RuntimeError(
            'This Claude Map version does not match the initial Development Hub '
            f'anchors: {exc}. Nothing changed. Do not use --apply yet.'
        ) from exc
    return 'scaffold-present' if not changed else 'scaffold-compatible'



def rehearse_overlay(directory, node):
    """Run all five upstream patches against temporary copies only.

    Never run patch stages against live Claude Map and never let a patch use
    the real HOME/USERPROFILE or real Claude configuration while rehearsing.
    This validates patch anchors and JS syntax, not a live browser/UI session.
    """
    with tempfile.TemporaryDirectory(prefix='ardizuo-map-rehearsal-') as tmp:
        workspace = Path(tmp)
        clone = workspace / 'claude-map'
        (clone / 'public').mkdir(parents=True)
        for relative in ('server.js', 'public/app.js', 'package.json'):
            source = directory / relative
            if source.is_file():
                target = clone / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        fake_home = workspace / 'private-home'
        fake_home.mkdir()
        fake_claude = fake_home / '.claude'
        fake_claude.mkdir()
        sandbox_env = dict(os.environ)
        sandbox_env.update({
            'HOME': str(fake_home),
            'USERPROFILE': str(fake_home),
            'CLAUDE_CONFIG_DIR': str(fake_claude),
        })
        stages = [
            ('bootstrap_devhub.py', ['--map-root', str(clone), '--apply']),
            ('claude_map_video_dashboard_patch.py', ['--map-dir', str(clone)]),
            ('claude_map_minimal_complete.py', ['--map-dir', str(clone), '--claude-dir', str(fake_claude)]),
            ('claude_map_finalize_integrations.py', ['--map-root', str(clone), '--claude-dir', str(fake_claude), '--apply']),
            ('claude_map_status_theme.py', ['--map-root', str(clone), '--apply']),
        ]
        print('FULL REHEARSAL (temporary files ONLY)', flush=True)
        print('Live Claude Map and ~/.claude remain untouched.', flush=True)
        print('Testing:', directory, flush=True)
        for filename, parameters in stages:
            # For already-customized installations, applying the video overlay
            # a second time deliberately errors; report this accurately rather
            # than silently counting it as newly installed.
            print('Checking overlay:', filename, flush=True)
            cmd = [sys.executable, str(PATCH / filename), *parameters]
            try:
                result = subprocess.run(cmd, env=sandbox_env, text=True,
                                        capture_output=True, timeout=120, check=False)
            except (OSError, subprocess.TimeoutExpired) as exc:
                raise RuntimeError(f'REHEARSAL BLOCKED at {filename}: '
                                   f'{type(exc).__name__}. Live files unchanged.') from exc
            if result.stdout.strip():
                print(result.stdout.strip()[-4500:], flush=True)
            if result.returncode:
                if result.stderr.strip():
                    print(result.stderr.strip()[-4500:], file=sys.stderr, flush=True)
                raise RuntimeError(f'REHEARSAL BLOCKED at {filename} (exit {result.returncode}). '
                                   'No live files changed. Do NOT use --apply.')
        for relative in ('server.js', 'public/app.js'):
            result = subprocess.run([node, '--check', str(clone / relative)],
                                    text=True, capture_output=True, timeout=30, check=False)
            if result.returncode:
                raise RuntimeError(f'REHEARSAL BLOCKED at JS syntax check: {relative}: '
                                   f'{result.stderr[-700:]}. No live files changed.')
        print('FULL REHEARSAL PASSED: all five overlay stages and JS syntax checks.', flush=True)
        print('Live files were not modified. Browser/runtime checks are still required.', flush=True)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Back up and apply overlays (not recommended until full compatibility review)')
    parser.add_argument('--rehearse', action='store_true', help='Run all five overlay scripts in a disposable, isolated copy; never write to live source')
    parser.add_argument('--map-root', type=Path, help='Exact Claude Map package folder; bypass npm lookup')
    args = parser.parse_args(argv)
    if args.apply and args.rehearse:
        parser.error('Use --apply or --rehearse, not both.')

    directory = (args.map_root or detect_map_root()).expanduser().resolve()
    app = directory / 'public' / 'app.js'
    server = directory / 'server.js'
    if not app.is_file() or not server.is_file():
        raise RuntimeError(f'Claude Map source not found at: {directory}. '
                           'Expected public/app.js and server.js. No changes made.')

    print('Claude Map folder:', directory)
    version_file = directory / 'package.json'
    if version_file.is_file():
        import json
        try:
            print('Installed Claude Map version:', json.loads(version_file.read_text(encoding='utf-8')).get('version', 'unknown'))
        except (ValueError, OSError):
            print('Installed Claude Map version: unknown')

    result = scaffold_preflight(app)
    print('Initial Development Hub compatibility:', result)
    if args.rehearse:
        return rehearse_overlay(directory, find_cli('node'))

    stages = [
        ('bootstrap_devhub.py', ['--map-root', str(directory), '--apply']),
        ('claude_map_video_dashboard_patch.py', ['--map-dir', str(directory)]),
        ('claude_map_minimal_complete.py', ['--map-dir', str(directory)]),
        ('claude_map_finalize_integrations.py', ['--map-root', str(directory), '--apply']),
        ('claude_map_status_theme.py', ['--map-root', str(directory), '--apply']),
    ]
    if not args.apply:
        print('DRY RUN. Initial scaffold compatible or already present; no files changed.')
        print('The remaining four overlay stages require a separate compatibility check.')
        for filename, _ in stages:
            print('  ', filename)
        print('Do NOT assume full compatibility from this preview.')
        return 0

    node = find_cli('node')
    # Upstream Claude Map may change. Back up both patched sources before trying.
    backup = Path.home() / ('claude-map-complete-backup-' +
                            datetime.datetime.now().strftime('%Y%m%d-%H%M%S%f'))
    backup.mkdir(parents=True, exist_ok=False)
    for original in (server, app):
        shutil.copy2(original, backup / original.name)
    try:
        for filename, stage_args in stages:
            print('Installing overlay:', filename, flush=True)
            proc = subprocess.run([sys.executable, str(PATCH / filename), *stage_args], check=False)
            if proc.returncode:
                raise RuntimeError(f'Overlay {filename} failed with exit {proc.returncode}')
        for original in (server, app):
            result = subprocess.run([node, '--check', str(original)],
                                    capture_output=True, text=True, timeout=30)
            if result.returncode:
                raise RuntimeError(f'JavaScript check failed: {result.stderr}')
    except Exception:
        print('Overlay failed. Restoring original server.js and app.js from backup.')
        for original in (server, app):
            shutil.copy2(backup / original.name, original)
        raise
    print('Development Hub overlay applied. Backup:', backup)
    print('Restart claude-map -p 8888 and hard refresh. Live service connections are not implied.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print('ERROR:', exc, file=sys.stderr)
        sys.exit(1)
