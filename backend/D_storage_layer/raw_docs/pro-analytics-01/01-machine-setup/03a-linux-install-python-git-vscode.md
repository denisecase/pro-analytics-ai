# 03-linux-install-python-git-vscode.md

This page provides instructions to install or verify Python, Git, and Visual Studio Code on a Linux machine using the apt package manager.


## Steps to Install or Verify

Open a terminal and run the following commands:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git code
python3 --version
pip3 --version
git --version
code --version
```

If any version commands return an error, ensure the corresponding package is installed.
Work on the installs until all --version commands correctly return a value. 
