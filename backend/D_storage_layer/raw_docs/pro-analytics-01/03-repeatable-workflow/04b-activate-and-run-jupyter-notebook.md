# 🔵 04b-activate-and-run-jupyter-notebook.md

This page explains how to run Jupyter notebooks in VS Code. When we execute code in a Jupyter notebook, the kernel runs the code interactively, allowing us to test, visualize, and document our analysis step by step.

A notebook is a web based interactive environment commonly used for exploratory data analysis (EDA) and more.

## Important Note

Use this only when your project uses **Jupyter notebook (`.ipynb`)** files. 
If your project only uses Python script (`.py`) files, you will not need this. 

## Before Starting

Open your project repository folder in VS Code. 
Ensure the .venv is activated. If it is already active, you don't need to reactivate it.  

We must have installed all the external dependencies needed for our project to run into the virtual environment first. 

### Install the Jupyter Extension for VS Code  
- Open the Extensions view in VS Code by pressing Ctrl+Shift+X (Windows/Linux) or Cmd+Shift+X (Mac).  
- Search for "Jupyter" and install the official extension.

### Open the Notebook in VS Code

Open the notebook in VS Code. The file will have a .ipynb extension. 

## Task 1. Select Notebook Kernel

Open the project notebook in VS Code. The file will have a .ipynb extension.
- If prompted, select a Python interpreter that corresponds to your .venv.  
- If not prompted, click the kernel selector in the top-right corner of the notebook editor and choose the interpreter associated with your Python Environment / .venv.
- Or:
   - From VS Code Menu, select View / Command Palette... (CTRL SHIFT P)
   - Type: Python: Select Interpreter 
   - Choose your .venv from the list

## Task 2. Start and Run a Jupyter Notebook

1. Open the project notebook in VS Code. The file will have a .ipynb extension.

2. Execute cells:  
   - Click on a cell and press Shift+Enter to execute it and move to the next cell.  
   - Alternatively, use Ctrl+Enter to execute the current cell without moving.

3. Save your notebook periodically to avoid losing progress. Or make sure the File / Autosave option is on.

## AS-NEEDED: If `.venv` packages (e.g., `pandas`) are not recognized  

1. Create a `.vscode` folder in your project.  
2. Add a `settings.json` file.  
3. Copy the full content from our shared [`.vscode/settings.json`](./.vscode/settings.json).  
4. Close and reopen your notebook.  
5. Activate the `.venv` environment.  
6. Verify or set the kernel as needed.  

## AS-NEEDED: Restart 

You may need to exit the notebook and restart the kernel periodically for best results. As needed, reopen, restart, and run all to verify.  

## AS-NEEDED: New External Dependencies

If any new external dependencies have been added to any Python scripts, add the external dependencies to requirements.txt and re-run the install dependencies process first. 

## ALWAYS: Fully Execute Notebooks before add-commit-push
Keep your notebooks organized and execute them fully before running git add-commit-push to GitHub.

## Experience

- Understand the role of a Jupyter kernel.
- Understand how to select and verify that the kernel and environment match to ensure all dependencies are correctly available.  
- Learn Markdown to make professional notebooks. 
- Use only one top level title. 
- Use numbered second-level headings to organize your work.
- Document your process and steps in the notebook and tell a story with data. 

---

[🔵 Continue with Part 3: Repeatable Workflow](REPEATABLE-WORKFLOW.md)
