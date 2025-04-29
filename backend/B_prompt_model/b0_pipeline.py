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
from backend.B_prompt_model.b2_call_model import call_model

def query(user_input: str) -> str:
    """
    Runs the full Retrieval-Augmented Generation (RAG) pipeline:

    1. Loads all available content files.
    2. Chunks text into manageable pieces.
    3. Embeds chunks into vectors.
    4. Searches embeddings for relevant matches to the user input.
    5. Ranks top matches for relevance.
    6. Builds a full prompt including guidelines, context, and question.
    7. Calls the LLM to generate the answer.

    Args:
        user_input (str): The user's question or input.

    Returns:
        str: The model's generated answer based on retrieved context.
    """
    # Step 1: Load files from storage
    files = load_markdown_files()

    # Step 2: Chunk files into smaller pieces
    all_chunks = []
    for path, text in files:
        all_chunks.extend(chunk_text(path, text))

    # Step 3: Embed the chunks into vector space
    embedded_chunks = embed_chunks(all_chunks)

    # Step 4: Search for vectors relevant to user query
    top_chunks = search_vectors(user_input, embedded_chunks)

    # Step 5: Rank the top chunks by relevance
    ranked_chunks = rank_chunks(top_chunks)

    # Step 6–7: Build prompt and call the model
    return call_model(user_input, [chunk["text"] for chunk in ranked_chunks])
