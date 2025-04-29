# ==========================================================
# Layer B1 - Build Prompt (b1_build_prompt.py)
# ==========================================================
# This file builds the full structured prompt sent to the LLM.
# 
# Responsibilities:
# - Load assistant behavior guidelines (static system message).
# - Join retrieved context chunks into a usable reference section.
# - Safely truncate the context if necessary to stay within model limits.
# - Format everything into a complete Retrieval-Augmented Generation (RAG) prompt.
# 
# This ensures the model receives a well-structured, professional, and
# behavior-controlled input for every user query.
# ==========================================================

from typing import List
from pathlib import Path

# Maximum context size (in characters, not tokens)
MAX_CONTEXT_LENGTH = 3000

# Path to the assistant behavior guidelines
GUIDELINES_PATH = Path("backend/D_storage_layer/raw_docs/GUIDELINES.md")

# Load guidelines once when this module is first imported
if GUIDELINES_PATH.exists():
    GUIDELINES_TEXT = GUIDELINES_PATH.read_text(encoding="utf-8").strip()
else:
    GUIDELINES_TEXT = (
        "You are a helpful assistant who only answers questions "
        "based on the provided context."
    )

def build_prompt(question: str, chunks: List[str]) -> str:
    """
    Builds a full Retrieval-Augmented Generation (RAG) prompt by combining:
    - Assistant behavior guidelines
    - Retrieved context chunks
    - User's input question

    Args:
        question (str): The user's input question.
        chunks (List[str]): List of relevant text chunks retrieved from the knowledge base.

    Returns:
        str: A full, structured prompt ready to send to the LLM.
    """
    # Join all context chunks together, separated by double newlines
    context = "\n\n".join(chunks)

    # Truncate the context if necessary
    if len(context) > MAX_CONTEXT_LENGTH:
        context = context[:MAX_CONTEXT_LENGTH]

    # Build the final formatted prompt
    prompt = (
        f"{GUIDELINES_TEXT}\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )

    return prompt
