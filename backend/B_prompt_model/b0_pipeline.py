# ==========================================================
# Layer B0 - Pipeline Controller (b0_pipeline.py)
# ==========================================================
# This file coordinates the full Retrieval-Augmented Generation (RAG) flow:
#
# Responsibilities:
# - Load raw content files (Layer C)
# - Chunk files into manageable pieces
# - Embed chunks into vector representations
# - Search vectors based on user input
# - Rank retrieved chunks for relevance
# - Build a full structured prompt (Layer B1)
# - Call the configured LLM model (Layer B2)
# - Return the final generated answer
#
# This module orchestrates all major layers (C, B1, B2) to serve user queries.
# ==========================================================

from C_retrieval_logic.c01_load_files import load_markdown_files
from C_retrieval_logic.c02_chunk_text import chunk_text
from C_retrieval_logic.c03_embed_chunks import embed_chunks
from C_retrieval_logic.c04_search_vectors import search_vectors
from C_retrieval_logic.c05_rank_chunks import rank_chunks
from backend.B_prompt_model.b1_build_prompt_wrapper import wrapper_retrieval  
from backend.B_prompt_model.b2_call_model import call_model

def query(user_input: str) -> str:
    """
    Runs the full Retrieval-Augmented Generation (RAG) pipeline:

    1. Attempts local retrieval first (Wrapper).
    2. If no strong match, continues with RAG flow.
    3. Builds a full prompt including guidelines, context, and question.
    4. Calls the LLM to generate the answer.

    Args:
        user_input (str): The user's question or input.

    Returns:
        str: The model's generated answer based on retrieved context.
    """

    # ==========================================================
    # STEP 1: Local Retrieval Wrapper First
    # ==========================================================
    local_chunks = wrapper_retrieval(user_input)
    
    if local_chunks:
        # If we got good local results, skip RAG
        return (
            f"### Local results from pro-analytics-01:\n\n"
            f"{' '.join(local_chunks)}"
        )
    

    # ==========================================================
    # STEP 2: Full RAG Process if Local Fails
    # ==========================================================
    # Step 2.1: Load raw content files
    files = load_markdown_files()

    # Step 2.2: Chunk files into smaller pieces
    all_chunks = []
    for path, text in files:
        all_chunks.extend(chunk_text(path, text))

    # Step 2.3: Embed the chunks into vector space
    embedded_chunks = embed_chunks(all_chunks)

    # Step 2.4: Search for vectors relevant to user query
    top_chunks = search_vectors(user_input, embedded_chunks)

    # Step 2.5: Rank the top chunks by relevance
    ranked_chunks = rank_chunks(top_chunks)

    # Step 2.6–7: Build prompt and call the model
    return call_model(user_input, [chunk["text"] for chunk in ranked_chunks])
