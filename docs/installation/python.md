# 🐍 Python 3


Python runs Ardizuo's setup scripts and optional MCP tooling. It is required by the current assisted installer.


<br />
<br />


## 📥 Windows PowerShell


```powershell
winget install --id Python.Python.3.13 --exact --source winget
```

A newer supported Python release is also suitable. Reopen PowerShell:

```powershell
python --version
python -m pip --version
```


<br />
<br />


## ⌨️ Bash alternative


macOS with Homebrew:

```bash
brew install python
python3 --version
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y python3 python3-venv
python3 --version
```


<br />
<br />


## 🛠️ Troubleshooting


If `python` opens the Microsoft Store on Windows, check App Execution Aliases or try `py --version`. Avoid placing a project virtual environment inside files you intend to commit. Official source: [python.org](https://www.python.org/downloads/).

[Installation index](./README.md)
