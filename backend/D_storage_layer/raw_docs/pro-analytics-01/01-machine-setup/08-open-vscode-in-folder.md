# 🟢 08-open-vscode-in-folder.md

Now, we use our new tools to verify our setup.
Be sure you have completed all earlier steps successfully and you have a `Repos` folder that is not automatically synced.

## Critical Note: We Only Use the `Repos` Folder This One Time
We are opening the Repos folder in VS Code just this once—to verify our setup.
After 🟠 Part 2, we will work in specific project folders within Repos.
Think of this as a **one-time health check** before we move on.

## VS Code Editor is Folder-based / Project-based 

VS Code is a **folder-based editor**. 
That means everything we do—whether editing files, running code, or using Git assumes that we’ve opened a specific folder.
If we open VS Code without opening a folder, many features may not work as expected. For example:

- The terminal might not open
- Python environments might not be detected
- Git integration may fail to activate

**Always start by opening a folder in VS Code.** 
In this course, that will usually be a project folder inside the `Repos` folder (once we create on in Part 2).

---

## Verify: Open VS Code in Your `Repos` Folder

### Option 1 (Graphical):

1. Open your `Repos` folder using File Explorer (Windows) or Finder (Mac).
2. Right-click on the folder and choose **"Open with Code"**.

### Option 2 (Terminal, if configured):

If you installed the `code` command in your terminal (e.g., using the Command Palette), you can type one of the following, the first works in Mac or Linux, the second command works in Windows PowerShell:

- `code ~/Repos`
- `code C:\Repos`

Either option should open your Repos folder in VS Code.

---

## Using the Integrated Terminal in VS Code

Once you’ve opened a folder in VS Code:

1. Go to the top menu and select **Terminal** > **New Terminal**.
2. A terminal will appear in the lower part of the VS Code window.

This is called the **integrated terminal**. You can run commands here just like in your regular system terminal.

### Terminal Types

On most systems, VS Code defaults to the system’s default shell:

- **Mac or Linux**: zsh or bash
- **Windows**: PowerShell, Command Prompt, or Git Bash (if installed)

You can change your default shell by clicking the dropdown next to the plus sign (`+`) in the terminal tab.

---

## Troubleshooting: Terminal Won’t Open in VS Code (Windows)

Some Windows users find the terminal in VS Code won’t open if no folder is loaded. This is a known issue, especially if:

- You opened VS Code without a folder
- You’re using a secondary drive (like D:\)
- No default working directory is configured

### Solution

1. In VS Code, go to **File > Preferences > Settings**
2. In the search box, type: `terminal.integrated.cwd`
3. Set this field to a valid folder path like `C:\Repos`

This ensures that the terminal has a default folder to open in—even when VS Code is opened without a project.

---

## Professional Practice: Always Open the Project Folder

- Important: After Part 2, **only open project folders**, not `Repos`.
- Examples: `pro-analytics-01`, `data-prep-01`, `my-analysis-project`.
- This ensures:
    - The terminal opens correctly
    - Git works properly
    - Python environments are detected

---

## Verify Installations

On Mac/Linux:

```shell
python3 --version
pip3 --version
git config --list
```

In Windows PowerShell:

```powershell
py --version
pip --version
git config --list
```

Make sure your version commands show numbers and your config lists your user.name and user.email.
If not, return to the instructions and redo the tasks until success. 
You need these tools installed and configured to complete the projects. 

---

[🟢 Finished with Part 1: Machine Setup](MACHINE-SETUP.md)


