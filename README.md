# pro-analytics-ai

This project demonstrates an OpenAI ChatGPT like project illustrating the structure and implementation of a Retrieval-Augmented Generation (RAG) system built with Python, vector embeddings, and Large Language Models (LLM).

IMPORTANT: Growing a working LLM system requires **serious hardware** and **significant storage**.
Read the requirements BEFORE attempting (or just read the repo to get an idea.)
This initial, local-only implementation takes a whooping **300 GB** of space. 

## Limited Focus / Small Raw Data Set (~100 KB)

This assistant is trained on the [pro-analytics-01](https://github.com/denisecase/pro-analytics-01) guide and is designed to help with setting up and working on professional analytics projects using Git, Python, and VS Code.

The corpus includes the relevant `.md`, `.py`, `.ipynb`, `.txt`, and configuration files from the project.

| File Type | Example Files | Approx Size | Notes |
|:----------|:--------------|:------------|:------|
| Markdown files (.md) | README.md, setup_os.md, etc. | ~50 KB | Instructions and guides |
| Python scripts (.py) | demo_script.py, install_python.py, etc. | ~25 KB | Basic educational scripts |
| Jupyter notebooks (.ipynb) | demo_notebook.ipynb | ~25 KB | Demo workflows |
| Configuration files (.txt, .gitignore, requirements.txt) | requirements.txt, .gitignore | ~2–5 KB | Important setup information |

**Total estimated training set size: ~100 KB (before tokenization).**
---

## Assistant Behavior Customization (GUIDELINES.md)

In addition to the raw project content, this assistant uses a small [`GUIDELINES.md`](backend/D_storage_layer/raw_docs/GUIDELINES.md) file to define behavior standards.

The guidelines influence how the assistant:

- Confirms the user's operating system and terminal as needed.
- Formats answers professionally and concisely.
- Provides technically accurate and context-aware support.
- Asks only one clarifying question at a time.

This customization improves the consistency, professionalism, and usefulness of the responses, especially when helping new analysts.

---

## Requirements (⭐32+ GB RAM, ⭐0.5 TB+ SSD)

The information size is trivial, but building a brain from it takes a great deal of effort, memory, and space. 
The biggest example took **300 GB** easily, and with additional quanitization support, we may get that below **100 GB**.
For an illustration of how the space is used, see [SPACE.md](SPACE.md).

Machine requirements even for this small corpus are:

- 32 GB RAM minimum (64 GB preferred for smoother training and inference)
- 1 TB SSD storage minimum (model, environment, temporary files)
- 4–8 CPU cores (modern i7, Ryzen 5, or equivalent recommended)
- GPU: Strongly recommended (NVIDIA T4, A10, 3060 or better)
  - Optional for API-based usage only (requires more space ~300 GB).
  - Required for running 8-bit or 4-bit quantized local models.
- Ubuntu 20.04/22.04 recommended (or WSL2 on Windows 11)

Tested on a machine with a 12-core (24-thread) CPU, 64 GB RAM, no discrete GPU (integrated graphics only), and a 2 TB NVMe SSD.

Additional:

- Use **Python 3.11** for better compatibility and performance with modern ML libraries.
- Machine Learning libraries like PyTorch and HuggingFace can require **0.5 GB or more** of installation space.
- On **Windows**, perform all operations inside **WSL2** (Ubuntu) to avoid compatibility problems and streamline Python, Git, and ML tool use.
   - Open PowerShell, type `wsl` and hit return.
   - If setting up WSL for the first time, store your WSL username and password - you will need the password during later installations. 

## Large Tools (and their Space Requirements)

| Tool/Library | Purpose | Approx Size |
|:-------------|:--------|:------------|
| sentence-transformers | Generating vector embeddings | **~0.5–1 GB** |
| chromadb | Local vector database storage | ~100–200 MB |
| fonttools | Dependency for tokenizer backends | ~50–100 MB |
| openai | Querying GPT models (API client) | ~50 MB |
| fastapi | Local API interaction (backend server) | ~50 MB |
| uvicorn | ASGI server for running FastAPI | ~50 MB |
| bitsandbytes | For 8-bit quantization (optional) | ~80 MB |
| auto-gptq | 4-bit model loader (optional) | ~150–250 MB |
| | pretrained 4-bit models  | **~0.3–1 GB** per model |

Summary

- Total base environment without quantization: **~1–2 GB**
- With 8-bit quantization support: **~2–2.5 GB**
- With 4-bit quantization support: **~2.5–3.5 GB**


For more information about space requirements when building a neural net brain, see [SPACE.md](SPACE.md).

## Pretrained Language Models

Pretrained large language models (LLMs) have already been trained to understand and generate human language.
They are available for free from sources like [Hugging Face](https://huggingface.co/models).
When loading a model using libraries like `transformers` or `auto-gptq`, the model files are automatically downloaded into a local Hugging Face cache, typically located at `~/.cache/huggingface/` (in Linux and WSL systems) so the large files can be shared across projects.

These models include the trained neural network weights needed to generate text, answer questions, or perform other natural language tasks.  
Pretrained models can be very large — often **1 GB or more per model**, even when quantized (compressed) into 8-bit or 4-bit formats.

IMPORTANT: Make sure you have sufficient **disk space** and **memory** before attempting to download and run larger models.

---

## Architecture

Front End

- Simple HTML/CSS/JS web app

L
| Layer  | Responsibility | Depends On | Expanded Description |
|:-------|:---------------|:------------|:---------------------|
| utils  | Logging and Configuration | none | Core utility functions for logging important events and managing settings. Foundation for all other layers. |
| C      | Retrieval (Context Finder) | utils | Takes a user question and searches for related information from the stored vector database (in chromadb). Needs utils for configuration and logging. |
| B      | Prompt Building and Querying | C | Builds a full prompt using both the user's question and retrieved context, then sends it to an LLM model (via openai library or local API). Needs the retrieval layer to gather context first. |
| A      | API Interface (Public Endpoint) | B | Exposes a public API (e.g., using fastapi and uvicorn) that receives user questions, calls the prompt/query layer, and returns answers. Only depends on layer B. |

For more information about the magic that happens in layer B, see the [backend/B_prompt_model/README.md](backend/B_prompt_model/README.md).

---

## LLM Source Options (Choose One if Using Full-Precision or API Models)

- OpenRouter	Open-source LLMs + OpenAI compatibility (free w/key)
- OpenAI API	Clean, reliable, simple for students (paid w/key)

Prices for GPT-3.5 are pretty affordable

- $0.0015 per 1,000 tokens (input)
- $0.002 per 1,000 tokens (output)

---

## Current Status

Runs locally, not yet hosted.


| Feature                     | Description                                         |
|-----------------------------|-----------------------------------------------------|
| Frontend Input + Button     | Captures and sends question to the backend  |
| FastAPI Backend             | Handles POST requests, logs content        |
| Embedded Markdown Knowledge | Chunks & indexes repository content        |
| RAG + OpenRouter API   | Builds a prompt from relevant context and queries LLM |
| UI Response      | Displays answer in the interface      |


---

## Responses Will Change (Set Temp to 0 to be Consistent)

Answers will change. To get consistent responses, we can set the 'temperature' to zero. 

```python
response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0
)
```

Since we haven't done that, responses will vary. For example:

- Git is a version control system.
- Git is a version control system that allows you to track changes in your code, collaborate with others, and manage your project's history effectively.
 
![Example](images/pro-analytics-ai.png)

---

## Create Repos folder and Clone (One-Time to Get Started)

- Create ~/repos folder: `mkdir -p ~/repos`
- Clone your repo with `git clone your-repo-url`
- Open in VS Code: `code .`

## Get LLM API Key (One-Time Task)

1. Go to: https://openrouter.ai/
2. Click "Sign In" (top right). You can use Google, GitHub, or email
3. After logging in, go to: <https://openrouter.ai/account>
4. Scroll to the API Keys section
5. Click "Create Key". Name it `Pro-Analytics-AI` or something. Set amount to 1. 
6. Copy your new API key (it will start with or-)
7. Paste it into your `.env` file like this:

OPENROUTER_API_KEY=or-xxxxxxxxxxxxxxxxxxxx

## Create a .venv and Install Dependencies

- Open the project repository folder in VS Code. 
- Open a new terminal (bash or zsh) (e.g. using the VS Code menu / Terminal / New Terminal) and run the following commands one at a time. 
- For more info, see requirements.txt. 
- Add `--timeout 100` to let each file take 100 seconds instead of default 15 seconds. 
- Run update again after installing deadsnakes.

```shell
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 python3.11-venv -y
sudo apt install uvicorn -y
```

```shell
python3.11 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt --timeout 100
```

Note 1. You need to rerun the last install command several times to get all packages downloaded and installed correctly into your local project virtual environment (.venv). 

Note 2. When returning to the project, remember to activate your .venv before installing requirements or running code. 


## To Run Locally - Terminal 1 of 2 (Server/API):

To launch the backend:

```shell
uvicorn backend.A_api_interface.query_api:app --host 0.0.0.0 --port 8000 --reload
```
Keep the terminal open and don't use it for anything else while running the backend. 

## To Run Locally - Terminal 2 of 2 (Client):

To test it, open another terminal and run:

```shell
curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is git?"}'
```

Use CTRL+C - hold down the CTRL and c key together - (multiple times if needed) to kill the process. 

## To Open a Front End Web Page Preview

Install VS Code Extension Live Preview. 
In VS Code, right-click `docs/index.html` and select "Show Preview". 


## Optional / As Needed: Update Content As the Source Repository Changes

```shell
git clone https://github.com/denisecase/pro-analytics-01 backend/D_storage_layer/raw_docs/pro-analytics-01
rm -rf backend/D_storage_layer/raw_docs/pro-analytics-01/.git
rm -rf backend/D_storage_layer/raw_docs/pro-analytics-01/.vscode
rm -rf backend/D_storage_layer/raw_docs/pro-analytics-01/logs
```

This updates the content and deletes the .git folder and other unneeded parts from backend/D_storage_layer/raw_docs/pro-analytics-01.
