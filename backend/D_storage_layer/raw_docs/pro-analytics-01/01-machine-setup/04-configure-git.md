# 04-configure-git.md

After installing Git, configure the global user.name and user.email. 

##  Open VS Code. 

Open your newly installed VS Code editor. We'll use the terminal available in VS Code.

## New Terminal

Use the VS Code menu to select Terminal >  New Terminal.
Opening a new terminal will ensure the terminal knows about the newly installed git. 

## Important: Know Your Terminal Type

If Windows, always use a terminal type of PowerShell. Do not use Command Prompt - it is deprecated.
If Mac/Linux, use the default (typically zsh or bash).


Configure your git user.name and user.email. 
Use YOUR name and email in the commands below. 
Use the same email you used for GitHub. 
School emails may be temporary - you may wish to use a more permanent email. 
Change these commands to use your information instead. 
Run one command at a time and hit ENTER or RETURN after each line to execute it. 

```shell
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
git config --list
```

Verify that the last command correctly shows your user.name and user.email. 
