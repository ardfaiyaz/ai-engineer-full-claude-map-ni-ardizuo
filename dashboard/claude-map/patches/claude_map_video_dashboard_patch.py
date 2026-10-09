#!/usr/bin/env python3
"""Read-only creator-style development architecture view for Claude Map.

Patches only Claude Map's server.js and public/app.js; never touches ~/.claude.
Usage: python claude_map_video_dashboard_patch.py [--map-dir PATH]
"""
from __future__ import annotations
import argparse
import datetime
import pathlib
import re
import shutil
import subprocess
import sys

BACKEND = r'''
// BEGIN VIDEO DEVELOPMENT ARCHITECTURE INVENTORY (READ ONLY)
app.get('/api/development-architecture', (req, res) => {
  // Return names and booleans only. Do not send raw settings, args, env, headers,
  // credentials, note contents or absolute paths to the browser.
  const home = process.env.USERPROFILE || process.env.HOME;
  if (!home) return res.status(500).json({ error: 'Home directory unavailable' });
  const root = path.join(home, '.claude');
  const vault = path.join(home, 'Documents', 'Claude-Dev-Vault');
  const sensitiveOrNonDev = /(^|[-_: ])(social|youtube|tiktok|instagram|facebook|influencer|marketing|remotion|video|media)([-_: ]|$)/i;
  const entries = { skills: new Map(), commands: new Map() };
  const allowed = value => typeof value === 'string' && value.length > 0
     && value.length <= 120 && !sensitiveOrNonDev.test(value);

  function add(kind, name, source) {
    if (allowed(name)) entries[kind].set(name, { name, source });
  }
  // Bounded, symlink-free walk; reads file names, not file contents.
  function walk(dir, depth, visit, remaining) {
    if (depth > 9 || remaining.n <= 0 || !fs.existsSync(dir)) return;
    let items;
    try { items = fs.readdirSync(dir, { withFileTypes: true }); }
    catch { return; }
    for (const item of items) {
      if (--remaining.n < 0) break;
      if (item.isSymbolicLink()) continue;
      if (item.isDirectory()) {
        if (/^(node_modules|\.git|\.next|dist|build|tmp)$/i.test(item.name)) continue;
        walk(path.join(dir, item.name), depth + 1, visit, remaining);
      } else if (item.isFile()) visit(dir, item.name);
    }
  }
  const primarySkills = path.join(root, 'skills');
  walk(primarySkills, 0, (dir, name) => {
    if (name.toLowerCase() === 'skill.md') add('skills', path.basename(dir), 'user');
  }, { n: 4500 });
  const commandsDir = path.join(root, 'commands');
  walk(commandsDir, 0, (dir, name) => {
    if (!name.toLowerCase().endsWith('.md')) return;
    const base = name.slice(0, -3);
    const rel = path.relative(commandsDir, dir).split(path.sep).filter(Boolean);
    add('commands', rel.length ? rel.join(':') + ':' + base : base, 'user');
  }, { n: 3500 });
  // Installed plugin skills/commands are in the plugin cache, not ~/.claude/skills.
  const cache = path.join(root, 'plugins', 'cache');
  walk(cache, 0, (dir, name) => {
    const segments = dir.split(path.sep);
    const skillIndex = segments.lastIndexOf('skills');
    const cmdIndex = segments.lastIndexOf('commands');
    const source = segments.find(s => /superpowers|ralph[-_]skills/i.test(s)) || 'plugin';
    const prefix = /superpowers/i.test(source) ? 'superpowers'
       : /ralph[-_]skills/i.test(source) ? 'ralph-skills' : '';
    if (name.toLowerCase() === 'skill.md' && skillIndex !== -1) {
      const skillName = path.basename(dir);
      add('skills', skillName, 'plugin');
      if (prefix) add('skills', prefix + ':' + skillName, 'plugin');
    }
    if (name.toLowerCase().endsWith('.md') && cmdIndex !== -1) {
      const commandName = name.slice(0, -3);
      if (prefix) add('commands', prefix + ':' + commandName, 'plugin');
    }
  }, { n: 6000 });

  function mdNames(dir) {
    try { return fs.readdirSync(dir).filter(s => s.endsWith('.md'))
       .map(s => s.slice(0, -3)).filter(allowed).sort(); }
    catch { return []; }
  }
  const settings = (() => { try {
    return JSON.parse(fs.readFileSync(path.join(root, 'settings.json'), 'utf8'));
  } catch { return {}; } })();
  const userConfig = (() => { try {
    return JSON.parse(fs.readFileSync(path.join(home, '.claude.json'), 'utf8'));
  } catch { return {}; } })();
  const hooks = ['skill-gate-check', 'vault-session-init', 'log-to-vault',
    'stop-vault-log', 'dead-code-check'].map(name => ({
      name, present: fs.existsSync(path.join(root, 'hooks', name + '.mjs'))
  }));
  const config = [
    ['CLAUDE.md', path.join(root, 'CLAUDE.md')],
    ['skill-gates.json', path.join(root, 'workflows', 'skill-gates.json')],
    ['personas', path.join(root, 'personas')],
    ['commands', path.join(root, 'commands')],
    ['wave-protocol.md', path.join(root, 'workflows', 'wave-protocol.md')],
    ['completion-mandate.md', path.join(root, 'workflows', 'completion-mandate.md')],
    ['developer-orchestration.md', path.join(root, 'rules', 'developer-orchestration.md')]
  ].map(([name, file]) => ({ name, present: fs.existsSync(file) }));
  const memory = ['Sessions','Learnings','ADRs','Dispatch-Logs','PRDs','Diagrams',
    'Projects','Templates'].map(name => ({name,
      present: fs.existsSync(path.join(vault, name)) }));
  const mcp = Object.entries(userConfig.mcpServers || {}).filter(([name]) => allowed(name))
    .map(([name, cfg]) => ({name, transport: cfg?.type === 'http' ? 'http'
       : cfg?.type === 'sse' ? 'sse' : 'stdio'}));
  res.setHeader('Cache-Control', 'no-store');
  res.json({
    skills: [...entries.skills.values()].sort((a,b) => a.name.localeCompare(b.name)),
    commands: [...entries.commands.values()].sort((a,b) => a.name.localeCompare(b.name)),
    agents: mdNames(path.join(root, 'agents')),
    hooks,
    events: Object.keys(settings.hooks || {}).filter(allowed),
    config, memory,
    obsidianVaultPresent: fs.existsSync(vault),
    obsidianConfigPresent: fs.existsSync(path.join(vault, '.obsidian')),
    mcp,
    // No implementation/agent telemetry is captured. Do not claim tasks ran.
    runEvidenceAvailable: false
  });
});
// END VIDEO DEVELOPMENT ARCHITECTURE INVENTORY

'''

FRONTEND = r'''
// BEGIN VIDEO DEVELOPMENT SYSTEM HUB
// A faithful read-only representation of the layers visible in the source video.
// This does NOT invoke agents, execute completion checks, or report live runs.
const VIDEO_GROUPS = [
  {title:'Orchestration', items:['team-driven-development','dispatching-parallel-agents','writing-plans','executing-plans','sc:workflow']},
  {title:'Quality', items:['simplify','code-review','clean-code-typescript','karpathy-guidelines','code-splitting','gauge-improvements','security-review','verification-before-completion']},
  {title:'Development', items:['test-driven-development','using-git-worktrees','finishing-a-development-branch','receiving-code-review','fix-build']},
  {title:'Debugging', items:['systematic-debugging','test-fixing','root-cause-analysis']},
  {title:'Discovery', items:['superpowers:brainstorming','sc:brainstorm','ralph-skills:prd','sc:research']},
  {title:'Design', items:['frontend-design','ui-ux-pro-max','web-design-guidelines','figma:figma-use']},
  {title:'Writing', items:['humanizer','elements-of-style','sc:document','claude-md-management']},
  {title:'Integrations', items:['vercel:nextjs','vercel:ai-sdk','vercel:deploy','react-native-best-practices','expo:deployment','stripe:best-practices','sentry:sentry-workflow','atlassian:triage-issue','Notion:search']},
  {title:'Operations', items:['sc:pm','ship-learn-next','claude-api']}
];
const VIDEO_STAGES = [
  {id:'triage', name:'Triage', desc:'Discover the need, inspect context and identify existing solutions.', tools:['superpowers:brainstorming','sc:research','ralph-skills:prd']},
  {id:'contract', name:'Contract', desc:'Define scope, acceptance criteria, task ownership and plan.', tools:['writing-plans','skill-gates.json','sc:workflow']},
  {id:'dispatch', name:'Dispatch', desc:'Delegate independent work with explicit file ownership and safe integration.', tools:['dispatching-parallel-agents','executing-plans','wave-protocol.md']},
  {id:'review', name:'Review', desc:'Validate implementation, tests, reuse, security and code quality.', tools:['code-review','security-review','verification-before-completion']},
  {id:'ship', name:'Ship', desc:'Complete the verified release checklist. Never auto-commit, push or deploy.', tools:['simplify','code-review','reuse-audit','dead-code-scan','vault-learning']}
];
const VIDEO_MANDATE = ['simplify','code-review','reuse-audit','dead-code-scan','vault-learning'];
const VIDEO_ROLES = [
 ['tech lead','system-architect'], ['backend','backend-architect'],
 ['frontend','frontend-architect'], ['design','frontend-architect'],
 ['QA','quality-engineer'], ['security','security-engineer'],
 ['PM','pm-agent'], ['devops','devops-architect'],
 ['writer','technical-writer'], ['product','requirements-analyst'],
 ['diagrams','']
];

function renderDevelopmentHub() {
  const screen = window.__videoHubInventory;
  if (!screen) {
    if (!window.__videoHubLoading) {
      window.__videoHubLoading = true;
      fetch('/api/development-architecture', {cache:'no-store'})
        .then(r => { if (!r.ok) throw new Error('inventory endpoint unavailable'); return r.json(); })
        .then(d => { window.__videoHubInventory = d; window.__videoHubLoading = false;
          if (State.currentTab === 'devhub') renderTabContent(); })
        .catch(() => { window.__videoHubLoading = false; window.__videoHubError = true;
          if (State.currentTab === 'devhub') renderTabContent(); });
    }
    return `<div class="section"><div class="section-title">Development System</div>
      ${window.__videoHubError ? 'Inventory could not load. Check the local server and refresh.' : 'Loading local capabilities...'}</div>`;
  }
  const safe = value => escapeHtml(String(value ?? ''));
  const names = [...(screen.skills || []), ...(screen.commands || [])].map(x => x.name);
  const fullNames = new Set(names.map(n => n.toLowerCase()));
  const basicNames = new Set(names.map(n => n.toLowerCase().split(':').pop()));
  const config = new Map((screen.config || []).map(x => [x.name.toLowerCase(), !!x.present]));
  const hasTool = n => n.endsWith('.json') || n.endsWith('.md')
    ? !!config.get(n.toLowerCase())
    : (n.includes(':') ? fullNames.has(n.toLowerCase()) : basicNames.has(n.toLowerCase()));
  const chip = (label, found, quiet = false) =>
    `<span class="vhub-chip ${found ? 'vhub-on' : 'vhub-off'}" title="${found?'Detected in local inventory':'Not detected in scanned sources'}">${safe(label)}<em>${found?'detected':'not found'}</em></span>`;
  const plainChip = (label, found) =>
    `<span class="vhub-chip ${found?'vhub-on':'vhub-off'}">${safe(label)}</span>`;
  const active = VIDEO_STAGES.find(x => x.id === (window.__videoStage || 'triage')) || VIDEO_STAGES[0];
  window.showVideoStage = id => { window.__videoStage = id; if (State.currentTab === 'devhub') renderTabContent(); };
  const agentNames = new Set((screen.agents || []).map(n => n.toLowerCase()));
  const roles = VIDEO_ROLES.map(([role, agent]) =>
    `<span class="vhub-chip ${agent && agentNames.has(agent)?'vhub-on':'vhub-off'}" title="${safe(agent||'Role not mapped')}">${safe(role)}</span>`).join('');
  const groups = VIDEO_GROUPS.map(g => {
    const detected = g.items.filter(hasTool).length;
    return `<section class="vhub-category"><div class="vhub-category-header">
        <strong>${safe(g.title)}</strong><small>${detected}/${g.items.length} detected</small></div>
      <div class="vhub-items">${g.items.map(n => chip(n,hasTool(n))).join('')}</div></section>`;
  }).join('');
  const lower = (title, detail, items) => `<div class="vhub-layer"><div class="vhub-layer-top">
      <strong>${safe(title)}</strong><small>${safe(detail)}</small></div>
      <div class="vhub-items">${items.join('')}</div></div>`;
  const hookLayer = lower('Hook layer','Lifecycle events, limited automation',
    (screen.hooks || []).map(h => plainChip(h.name,h.present)));
  const configLayer = lower('Config layer','Rules of the system',
    (screen.config || []).filter(x => x.name !== 'developer-orchestration.md').map(c => plainChip(c.name,c.present)));
  const memoryLayer = lower('Memory layer','Decisions persist across sessions',
    [plainChip('Obsidian vault',screen.obsidianVaultPresent),
    ...(screen.memory || []).map(m => plainChip(m.name,m.present))]);
  const mcps = (screen.mcp || []).map(m => `<span class="vhub-chip vhub-on">${safe(m.name)}<em>${safe(m.transport)}</em></span>`).join('');
  const stages = VIDEO_STAGES.map((s,i) =>
    `<button type="button" class="vhub-stage ${(active.id===s.id)?'active':''}" onclick="showVideoStage('${s.id}')">
      <span>${i+1 < 10 ? '0'+(i+1) : i+1}</span><strong>${safe(s.name)}</strong></button>`).join('');
  const shipItems = ['Review changed files and scope','Run project tests and type checking',
    'Run lint and relevant build','Inspect secrets and authorization risks',
    'Check reuse, complexity and dead code','Prepare PR and release notes',
    'Deployment only with explicit approval','Confirm rollback and write approved vault note'];
  const ship = active.id === 'ship'
    ? `<div class="vhub-ship"><strong>Ship preflight — checklist, not automated evidence</strong>
       <div class="vhub-ship-grid">${shipItems.map(n=>`<div>□ ${safe(n)}</div>`).join('')}</div>
       <p>No checks are marked passed until verified during a real development session.</p></div>` : '';
  return `
<style>
.video-hub{font-size:13px;color:var(--text-primary,var(--text,#e4eaf4));padding:2px 2px 45px}
.video-hub *{box-sizing:border-box}
.vhub-eyebrow{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#8ea6c8;font-weight:700}
.vhub-heading{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:8px 0 18px;flex-wrap:wrap}
.vhub-heading h1{font-size:22px;letter-spacing:-.6px;margin:0;color:#e7efff}
.vhub-note{font-size:11px;color:#9babbe;max-width:480px;line-height:1.6}
.vhub-top{border:1px solid #4073b8;background:linear-gradient(120deg,#131f35,#171c2f);border-radius:11px;padding:14px 16px;margin:10px 0}
.vhub-top h2{color:#72bdff;font-size:14px;margin:0 0 11px;font-weight:700}
.vhub-stages{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:7px}
.vhub-stage{min-width:0;border:1px solid #344964;background:#121c2c;color:#e1eaf5;border-radius:8px;cursor:pointer;padding:10px 4px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:4px}
.vhub-stage span{font-size:10px;color:#7a91af}.vhub-stage strong{font-size:12px}.vhub-stage:hover,.vhub-stage.active{background:#1c3453;border-color:#5bb9ff}
.vhub-desc{margin:10px 0 8px;color:#b7cce1;line-height:1.5}
.vhub-plain{border:1px solid #38445a;border-radius:10px;background:#171e2f;padding:14px 16px;margin:10px 0}
.vhub-plain h2{font-size:14px;color:#dde8fb;margin:0 0 10px}
.vhub-small{font-size:11px;color:#8ca8cb}
.vhub-items{display:flex;align-items:center;flex-wrap:wrap;gap:6px}
.vhub-chip{display:inline-flex;align-items:center;gap:5px;font-size:11px;line-height:1.4;padding:5px 9px;border:1px solid #35465d;border-radius:7px;background:#142035;color:#c7d5e7;white-space:normal;overflow-wrap:anywhere}
.vhub-chip em{font-size:9px;color:#91a5bc;font-style:normal}.vhub-chip.vhub-on{border-color:#275c7b;color:#8dd9f6}.vhub-chip.vhub-off{opacity:.65;border-style:dashed}
.vhub-skills{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:11px 0}
.vhub-category{min-width:0;border:1px solid #313c53;background:#161e30;border-radius:10px;padding:14px;min-height:125px}
.vhub-category-header{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:12px;color:#72bdff;letter-spacing:.8px;text-transform:uppercase;font-size:11px}
.vhub-category-header small{font-size:10px;color:#8fa5c4;letter-spacing:0;text-transform:none}
.vhub-layer{border:1px solid #38445a;background:#161f30;padding:12px 16px;margin:8px 0;border-radius:9px}
.vhub-layer-top{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:9px}.vhub-layer-top strong{color:#f4df9a}.vhub-layer-top small{color:#96a8c2}
.vhub-ship{margin-top:12px;background:#12283a;border:1px solid #366b91;border-radius:8px;padding:12px;color:#cbdcec}.vhub-ship-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;margin:10px 0}.vhub-ship p{font-size:11px;color:#94adc2}
.vhub-footer{border-top:1px solid #34425a;margin-top:16px;padding-top:13px;color:#95acc6;font-size:11px}
@media(max-width:790px){.vhub-skills,.vhub-ship-grid{grid-template-columns:1fr}.vhub-stages{grid-template-columns:repeat(3,minmax(0,1fr))}}
</style>
<div class="video-hub">
  <div class="vhub-eyebrow">SYSTEM · WHAT THE RUNTIME STANDS ON</div>
  <div class="vhub-heading"><h1>Developer Orchestration System</h1>
    <div class="vhub-note">Inspired by the supplied video · Global configuration · Development only · Read-only architecture</div></div>
  <div class="vhub-top"><h2>Workflow surface</h2><div class="vhub-stages">${stages}</div>
    <p class="vhub-desc"><strong>${safe(active.name)}:</strong> ${safe(active.desc)}</p>
    <div class="vhub-items">${active.tools.map(n=>chip(n,hasTool(n))).join('')}</div>${ship}</div>
  <div class="vhub-top"><div style="display:flex;justify-content:space-between;gap:8px"><h2>Completion mandate</h2><span class="vhub-small">Post-task checks · execution unverified</span></div>
    <div class="vhub-items">${VIDEO_MANDATE.map(n=>chip(n,hasTool(n))).join('')}</div></div>
  <div class="vhub-plain"><div style="display:flex;justify-content:space-between;gap:8px"><h2>Agent layer</h2><span class="vhub-small">${(screen.agents||[]).length} global agents found · video roles mapped where possible</span></div>
    <div class="vhub-items">${roles}</div><p class="vhub-small" style="margin-top:10px">Installed agents: ${(screen.agents||[]).map(safe).join(' · ')||'None detected'}</p></div>
  <div class="vhub-plain"><div style="display:flex;justify-content:space-between;gap:8px"><h2>Skill layer</h2><span class="vhub-small">${(screen.skills||[]).length} discovered skill names · ${(screen.commands||[]).length} command names</span></div>
    <div class="vhub-skills">${groups}</div></div>
  ${hookLayer}${configLayer}${memoryLayer}
  <div class="vhub-layer"><div class="vhub-layer-top"><strong>MCP integration layer</strong><small>${(screen.mcp||[]).length} user-scoped configured servers</small></div>
    <div class="vhub-items">${mcps || 'No MCP inventory found'}</div></div>
  <div class="vhub-footer">A detected skill is not proof it ran. Status reflects discovered local filenames and configuration only.
  Plugin and built-in discovery may be incomplete. Use Claude Code /skills and /mcp as the authoritative live views.
  No actions, builds, commits, deployments, vault writes, or model calls are triggered by this page.</div>
</div>`;
}
// END VIDEO DEVELOPMENT SYSTEM HUB

'''


def patch_file(path: pathlib.Path, source: str) -> str:
    if path.name == "server.js":
        if 'BEGIN VIDEO DEVELOPMENT ARCHITECTURE INVENTORY' in source:
            raise ValueError('Backend patch already installed')
        anchor = "app.get('/api/scan', async (req, res) => {"
        if source.count(anchor) != 1:
            raise ValueError('Unexpected Claude Map server.js: API scan anchor missing or duplicated')
        return source.replace(anchor, BACKEND + anchor, 1)
    if 'BEGIN VIDEO DEVELOPMENT SYSTEM HUB' in source:
        raise ValueError('Development video dashboard already installed')
    start_marker = 'function renderDevelopmentHub() {'
    end_marker = 'function renderMCP() {'
    if source.count(start_marker) != 1 or source.count(end_marker) != 1:
        raise ValueError('Development Hub/MCP anchors not found uniquely: verify custom hub is installed')
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    between = source[start:end]
    functions = re.findall(r'\bfunction\s+(\w+)\s*\(', between)
    if not functions or functions[0] != 'renderDevelopmentHub' or any(
        x not in {'renderDevelopmentHub','itemName','namesMatching','renderNames'} for x in functions
    ):
        raise ValueError('Unexpected helper functions between hub and MCP: ' + ', '.join(functions))
    return source[:start] + FRONTEND + source[end:]


def run():
    ap = argparse.ArgumentParser(description='Install a video-inspired, read-only Claude Map Development Hub')
    ap.add_argument('--map-dir', help='Claude Map npm package directory')
    args = ap.parse_args()
    if args.map_dir:
        root = pathlib.Path(args.map_dir)
    else:
        npm = subprocess.run(['npm', 'root', '-g'], text=True, capture_output=True, check=True, shell=(sys.platform == 'win32'))
        root = pathlib.Path(npm.stdout.strip()) / 'claude-map'
    server = root / 'server.js'
    frontend = root / 'public' / 'app.js'
    for f in (server, frontend):
        if not f.is_file():
            sys.exit(f'Missing: {f}')
    originals = {f: f.read_text(encoding='utf-8') for f in (server, frontend)}
    try:
        patched = {f: patch_file(f, originals[f]) for f in originals}
    except ValueError as error:
        sys.exit('No changes made. ' + str(error))
    destination = pathlib.Path.home() / ('claude-map-video-backup-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    destination.mkdir(parents=True, exist_ok=False)
    shutil.copy2(server, destination / 'server.js')
    shutil.copy2(frontend, destination / 'app.js')
    try:
        for f, body in patched.items():
            f.write_text(body, encoding='utf-8')
        for f in patched:
            check = subprocess.run(['node', '--check', str(f)], capture_output=True, text=True, shell=(sys.platform == 'win32'))
            if check.returncode:
                raise RuntimeError('Syntax check failed: ' + str(f) + '\n' + check.stderr)
    except Exception as err:
        for f, body in originals.items():
            f.write_text(body, encoding='utf-8')
        sys.exit(f'Patch was automatically rolled back: {err}')
    print('Video-inspired Development Hub patch installed and passed node --check.')
    print('Backup: ' + str(destination))
    print('Files changed: server.js and public/app.js ONLY.')
    print('Restart claude-map and refresh the Development Hub tab.')

if __name__ == '__main__':
    run()
