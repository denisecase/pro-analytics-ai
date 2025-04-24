# 03-windows-install-python-git-vscode.md

This page provides instructions to install or verify Python, Git, and Visual Studio Code on a Windows machine using the Winget package manager.

## Steps to Install or Verify

Open a PowerShell terminal and run the following commands:

```powershell
winget install --id Python.Python.3
winget install --id Git.Git
winget install --id Microsoft.VisualStudioCode
```

Close that terminal. 

Open a PowerShell terminal again and run the following commands to verify. 

```powershell
py --version
python --version
pip --version
git --version
code --version
```

## ADVANCED: Multiple Versions of Python

This is not typically needed. 
Only continue with this section if you need to add an earlier version of Python (e.g. to use with complex tools such as Kafka or Spark).

In that case, we can install additional Python versions like so:

```powershell
winget install --id Python.Python.3.11.11
```

Note: py --version and python --version may return different versions depending on which order they were installed, system path settings, and more. 
We will specify the desired Python version when creating the project virtual environment in the next workflow.
