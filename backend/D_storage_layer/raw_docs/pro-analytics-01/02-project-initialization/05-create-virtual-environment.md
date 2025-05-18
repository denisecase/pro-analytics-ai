# 🟠 05-create-virtual-environment.md

This page provides instructions to create a place in your project repository folder that will hold the Python virtual environment for the project. 
It provides an isolated Python environment for the project, so we don't mess up the global Python used by our machine. 

This is typically just done once at the beginning of a project.
If it gets messed up, we can delete .venv and recreate it at any time. 


## Before Starting

Open your project repository in VS Code. 

We'll open a new terminal in VS Code and run a single command to create a new .venv folder for the local project virtual environment.

## Windows Users - Task 1. Create .venv

Run the following command from the project root directory.
 
On Windows, Use PowerShell (not cmd):

```shell
py -m venv .venv
```

## Mac/Linux Users - Task 1. Create .venv

Run the following command from the project root directory.

On Mac/Linux, Use zsh or bash:

```shell
python3 -m venv .venv
```

## Accept VS Code Suggestions

If VS Code asks: We noticed a new environment has been created. 
Do you want to select it for the workspace folder?
Click Yes. 

---

## OPTIONAL/ADVANCED OPTION (Only if Older Python is Needed)

*Do not continue with this section unless you are using complex tools like Apache Kafka or Apache Spark that may take a while to catch up to the latest version of Python. Know these instructions are here when you need them later.*

Most projects can use the latest Python 3.x, but some tools (like Apache Kafka or Apache Spark) may require an older version.
First, see the machine setup instructions to install additional versions of Python. 
Then, specify the required version when creating the virtual environment. 
For example:

### On Windows, Use PowerShell (NOT cmd)

```powershell
py -3.11 -m venv .venv
```

### On Mac/Linux, Use Default Terminal (e.g., zsh or bash)

```shell
pyenv local 3.11.11
python3 -m venv .venv
```

---

[🟠 Finished with Part 2: Project Initialization](PROJECT-INITIALIZATION.md)
