# Python

**Why you might need it:** Supports selected tooling, tests and Python development. Not required to use every Claude Code feature.

<br />

## 1. Get it from the official source

[Python — official installation page](https://www.python.org/downloads/windows/)

Download the supported current Python release or the Python install manager from Python.org. On older installations, ensure `python` and `py` resolve correctly; don't blindly modify PATH if you already use a version manager.

Create project-specific virtual environments instead of installing all packages globally:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip --version
```

If you're inside the public Ardizuo repository, don't create project files you intend to commit as dependencies.

<br />

## 2. Verify

```powershell
python --version
py --version
```

<br />

## 3. If something goes wrong

If `python` opens the Microsoft Store, check Windows App Execution Aliases or use `py`. If the selected Python has no `pip`, follow the [official pip instructions](https://packaging.python.org/en/latest/tutorials/installing-packages/).



<br />

[All installation guides](./README.md) · [Prerequisites](../prerequisites.md) · [Troubleshooting](../troubleshooting.md)
