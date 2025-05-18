# File: backend/B_prompt_model/b1_build_prompt_wrapper.py
# ==========================================================
# Layer B1 - Wrapper Logic (b1_build_prompt_wrapper.py)
# ==========================================================
# This file handles local retrieval logic using `chroma_store`.
# If local results are sufficient, it returns them directly.
# If not, it signals to proceed with the full RAG process.
# ==========================================================

from backend.D_storage_layer.chroma_store import query_chunks
from utils.logger import logger

def wrapper_retrieval(user_input: str) -> list[str]:
    """
    Attempts local retrieval using ChromaDB before RAG processing.

    Args:
        user_input (str): The user's question or query.

    Returns:
        list[str]: Retrieved context chunks if confidence is high, empty list otherwise.
    """
    # Step 1: Detect specific terms only when "project" is mentioned
    if (
        "project" in user_input.lower() and 
        any(keyword in user_input.lower() for keyword in ["create", "init", "initialize", "start"])
    ):
        logger.info(f"Detected project initialization query: {user_input}")
        
        # Perform a more focused search in ChromaDB
        local_chunks = query_chunks("project initialization", top_k=5)

        # Step 2: Inject the response with both options
        response = (
            "Local results from pro-analytics-01:\n\n"
            "### Option 1: New Project\n"
            "Create a new repository from scratch by following the steps:\n"
            "1. Create a local folder for your project.\n"
            "2. Initialize Git with `git init`.\n"
            "3. Create a new repository on GitHub and connect it as a remote.\n\n"
            
            "### Option 2: Existing Repo\n"
            "Clone an existing repository using:\n"
            "`git clone <repository-url>`\n"
            "Followed by:\n"
            "`cd <repository-folder>`\n\n"
            
            "You can now proceed with either setup directly."
        )

        # If local chunks are found, prepend them with the response
        if local_chunks:
            return [response] + local_chunks
        else:
            # If no local chunks found, return just the response
            return [response]

    # If it is not a project setup, just query ChromaDB normally
    return query_chunks(user_input)
