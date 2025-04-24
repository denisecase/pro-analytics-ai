# 03b-mac-install-python-git-vscode.md

This page provides instructions to install or verify Python, Git, and Visual Studio Code on a macOS machine using the Homebrew package manager.
These tools are essential for professional data analytics.

It also includes steps to install pyenv (for managing multiple Python versions) and PowerShell (pwsh), a popular cross-platform terminal.

## Steps to Install and Verify

Open a terminal and run the following commands:

```zsh
brew update
brew install python3
brew install git
brew install --cask visual-studio-code
brew install pyenv
brew install --cask powershell

python3 --version
git --version
code --version
pyenv --version
pwsh --version
```

## Multiple Versions of Python with pyenv

If you need to add an earlier version of Python (e.g. to use with complex tools such as Kafka or Spark), use pyenv to install additional Python versions like so:

```zsh
pyenv install 3.11.11
```

## Aside: GUI Applications & Cask Installs

The --cask option is used for GUI applications like Visual Studio Code and PowerShell. 
These apps will appear in Finder, Dock, and Spotlight search, just like other macOS applications.
