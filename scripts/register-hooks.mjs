// Optional global Claude Code lifecycle hook registration.
// Dry-run unless --apply; no model use, no vault writes, no external calls.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const apply = process.argv.includes('--apply');
const configIndex = process.argv.indexOf('--config-dir');
const config = configIndex >= 0 ? process.argv[configIndex + 1] :
  (process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), '.claude'));
if (!config || config.includes('"')) throw new Error('Invalid Claude config directory.');
const settingsFile = path.join(config, 'settings.json');
const specs = [
  ['UserPromptSubmit', null, 'skill-gate-check.mjs', false],
  ['SessionStart', 'startup|resume', 'vault-session-init.mjs', false],
  ['PostToolUse', 'Write|Edit|MultiEdit|NotebookEdit', 'log-to-vault.mjs', true],
  ['PostToolUse', 'Write|Edit|MultiEdit', 'dead-code-check.mjs', false],
  ['Stop', null, 'stop-vault-log.mjs', false],
];
for (const [, , file] of specs) {
  if (!fs.existsSync(path.join(config, 'hooks', file))) {
    throw new Error(`Missing installed hook: hooks/${file}. Run install-development.ps1 first.`);
  }
}
const existingText = fs.existsSync(settingsFile) ? fs.readFileSync(settingsFile, 'utf8').replace(/^\uFEFF/, '') : '{}';
let settings;
try { settings = JSON.parse(existingText); } catch { throw new Error('Existing settings.json is not valid JSON; refusing to modify.'); }
if (!settings || Array.isArray(settings) || typeof settings !== 'object') throw new Error('Unexpected settings.json root.');
if (settings.hooks != null && (Array.isArray(settings.hooks) || typeof settings.hooks !== 'object')) throw new Error('Unexpected hooks object.');
const hooks = settings.hooks || {};
const pending = [];
for (const [event, matcher, filename, async] of specs) {
  const basename = filename.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const known = (hooks[event] || []);
  if (!Array.isArray(known)) throw new Error(`Unexpected hook array: ${event}`);
  // Windows commands contain backslashes. Normalize separators before checking.
  // The old RegExp treated only / as a separator after JS string unescaping,
  // which caused every repeat run on Windows to append five duplicate hooks.
  const registered = known.some(entry =>
    Array.isArray(entry?.hooks) && entry.hooks.some(h => {
      if (typeof h?.command !== 'string') return false;
      const normalized = h.command.replace(/\\/g, '/');
      const pattern = new RegExp(`(?:^|[\\/\\s"'])${basename}(?=$|[\\s"'])`, 'i');
      return pattern.test(normalized);
    })
  );
  if (registered) {
    continue;
  }
  const script = path.join(config, 'hooks', filename);
  const def = { type: 'command', command: `node "${script}"`, timeout: 10000 };
  if (async) def.async = true;
  const entry = matcher ? { matcher, hooks: [def] } : { hooks: [def] };
  pending.push({event, entry, filename});
}
console.log(`Claude config: ${config}`);
console.log(`Existing settings: ${fs.existsSync(settingsFile) ? 'present' : 'absent'}`);
console.log(`New hook registrations: ${pending.length}`);
for (const item of pending) console.log(`  ${item.event}: ${item.filename}${item.entry.matcher ? ' ['+item.entry.matcher+']' : ''}`);
if (!apply) { console.log('DRY RUN. Add --apply after reviewing changes. Existing settings and vault untouched.'); process.exit(0); }
if (!pending.length) { console.log('No changes: matching hook commands already registered.'); process.exit(0); }
const newHooks = {...hooks};
for (const {event,entry} of pending) newHooks[event] = [...(newHooks[event] || []), entry];
settings.hooks = newHooks;
fs.mkdirSync(config, {recursive:true});
if (fs.existsSync(settingsFile)) {
  // Private backup next to the settings file. This can contain secrets: NEVER commit it.
  const stamp = new Date().toISOString().replace(/[:.]/g,'-');
  const backup = path.join(config, `settings.json.ardizuo-backup-${stamp}`);
  fs.copyFileSync(settingsFile, backup, fs.constants.COPYFILE_EXCL);
  console.log('Original settings backed up privately under Claude config directory.');
}
const temp = `${settingsFile}.ardizuo-tmp-${process.pid}`;
try {
  fs.writeFileSync(temp, JSON.stringify(settings, null, 2) + '\n', {encoding:'utf8',flag:'wx',mode:0o600});
  // A fresh check prevents silently replacing changed settings during this short operation.
  if (fs.existsSync(settingsFile) && fs.readFileSync(settingsFile, 'utf8').replace(/^\uFEFF/, '') !== existingText) {
    throw new Error('settings.json changed since reading; refusing to replace.');
  }
  fs.renameSync(temp, settingsFile);
} catch (e) { try { fs.unlinkSync(temp); } catch {} throw e; }
console.log(`Added ${pending.length} hook registrations. Restart Claude Code and inspect /hooks.`);
