# Layer B - Prompt Building and Model Query

This folder contains the logic for handling prompts and interacting with the Large Language Model (LLM).

Layer B is responsible for:

- Building the complete prompt from user input and retrieved context.
- Loading and managing the LLM (API, 8-bit, or 4-bit model).
- Sending prompts to the LLM and returning generated responses.

It does NOT handle API interaction, database storage, or raw retrieval - only the prompt and model steps.

---

## File Structure

| File | Responsibility |
|:-----|:---------------|
| `b0_pipeline.py` | Orchestrates the full process: build prompt > call model > return answer. |
| `b1_build_prompt.py` | Builds a clean text prompt from user question + context snippets. |
| `b2_call_model.py` | Loads the configured model (API, 8-bit, or 4-bit) and sends prompts to it for inference. |

---

## Process Flow

1. `b0_pipeline.py` receives a user question.
2. It retrieves any relevant context (from Layer C - Retrieval).
3. It uses `b1_build_prompt.py` to build the final prompt text.
4. It passes the prompt to `b2_call_model.py` to get a model-generated answer.
5. It returns the answer back to the API layer.

---

## What Are Context Snippets?

- **Context snippets** are small sections of text retrieved from the project files based on the user's question.
- They are pulled from documents like `.md`, `.py`, `.txt` files during the retrieval step (Layer C).
- The best-matching snippets are included in the prompt sent to the model, helping it generate more relevant answers.

Example context snippet:

> Git is a distributed version control system that tracks changes in source code during software development.

If a user asks:  "What is Git?"

The system retrieves this snippet (and others like it), adds them to the prompt, and then asks the LLM to generate an answer based on the combined information.

---

## How the System Uses Context Snippets

The flow of information:

1. **User Question**  
   Example: "What is Git?"

2. **File Retrieval (Layer C)**  
   Search stored files for relevant content.  
   Example file found:  
   "Git is a distributed version control system..."

3. **Chunking and Embedding**  
   Break documents into manageable pieces.  
   Embed pieces as vectors for efficient search.

4. **Search and Retrieve Top Matches**  
   Find the most relevant snippets based on user question.

5. **Build Prompt**  
   Insert retrieved snippets + user's question into a final prompt.

6. **Call the Model**  
   Send the prompt to the LLM to generate an answer.

7. **Return Answer**  
   Deliver the model-generated answer back through the API.

---

## What Are Embeddings?

An **embedding** is a way of converting text into a set of numbers that captures its meaning.

When the system processes a text snippet, it uses an embedding model to generate a vector — a long list of numbers representing the meaning of the text.

Each embedding (vector) is a **numeric representation** of the text, designed so that:

- Texts with similar meanings produce similar embeddings.
- Texts with different meanings produce very different embeddings.

Embeddings allow the system to perform **semantic search** — finding related meanings instead of relying on exact word matching.

Embeddings are created once during the **vectorization** step and are stored for fast retrieval when answering user questions.

### Example:

Text snippet:

> Git is a distributed version control system that tracks changes in source code.

Embedding (vector format):

> [0.12, -0.34, 0.88, 0.15, ..., -0.22]

(Real embeddings usually have hundreds of dimensions.)

---

## What Are Vectors?

When we create an **embedding** for a text snippet, the result is a **vector** — a list of numbers representing the meaning of the text.

In other words: An embedding *is* a vector.

We use the terms depending on context:
- **Embedding** refers to the process and the idea of capturing meaning.
- **Vector** refers to the numeric form produced by that process.

When we process the documents, each chunk of text is transformed into a vector by the embedding process.

### Why Vectors Matter:

Vectors are stored for quick retrieval later when answering user questions.

- **Fast searching:** Instead of reading every file, the system compares vectors to find matches quickly.
- **Similarity detection:** Even if the words aren't exactly the same, similar meanings produce similar vectors.
- **Efficiency:** Searching numeric vectors is much faster than searching raw text.

### What Do the Numbers in a Vector Indicate?

Each number in a vector represents one feature or aspect of the meaning of the text.

- The **position** in the vector (first number, second number, etc.) corresponds to a specific learned feature.
- The **value** (positive, negative, near zero, large) reflects how strongly that feature appears in the text.

Each vector acts as a **numeric signature** representing the meaning of the text.

Important: 

- Vector features are learned automatically by the embedding model during training and are not directly human-readable.
- Rather than looking at feature values individually, we care about the **overall pattern** of the vector.
- Snippets with similar meanings produce **vectors with similar patterns**.
- This lets the system find related information quickly, even if the wording is different.
- Vectors capture the meaning or essence of a piece of text, NOT the exact wording.

---

## Model Usage Notes

- The local pretrained LLM model (if used) is loaded once when the server starts (singleton style) inside `b2_call_model.py`.
- API-based clients (OpenAI, OpenRouter) are initialized once at startup but do not load full models locally.
- All model queries should go through `b0_pipeline.py` to keep responsibilities clear.
- No other layers (API, Retrieval, Storage) should directly access or manipulate the model.

---

## Example Usage (Inside API Layer)

```python
from backend.B_prompt_model.b0_pipeline import query

# Example: Process a user question. Call query function and get a response
answer = query(user_input="What is Git?")
```
