# <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> Node.js and npm

**Why you might need it:** Runs JavaScript-based MCPs, Claude Map and many development tools.

<br />

## <img src="../assets/lucide/folder-open.svg" width="18" height="18" alt="" /> 1. Get it from the official source

[Node.js and npm — official installation page](https://nodejs.org/en/download)

**Recommended for beginners:** install the current **LTS** release from Node.js. npm ships with Node.js. If you need multiple versions, use a Windows Node version manager instead; see [npm guidance](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm/).

Avoid copying random `npm install -g` commands from untrusted sources. Review the package and version first.

<br />

## <img src="../assets/lucide/list-checks.svg" width="18" height="18" alt="" /> 2. Verify

```powershell
node --version
npm --version
npm config get prefix
```

<br />

## <img src="../assets/lucide/file-text.svg" width="18" height="18" alt="" /> 3. If something goes wrong

If `npm` is not recognized after installing Node.js, reopen PowerShell. If PowerShell reports that `npm.ps1` is blocked, try `npm.cmd --version` first; do not weaken system security policy as a default.



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
