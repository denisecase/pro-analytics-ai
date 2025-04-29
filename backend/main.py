# File: backend/main.py

import sys
from pathlib import Path

# Ensure project root is in sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Local imports
from utils.logger import logger

from backend.B_prompt_model.b0_pipeline import query
from C_retrieval_logic.c01_load_files import load_markdown_files
from C_retrieval_logic.c02_chunk_text import chunk_text
from C_retrieval_logic.c03_embed_chunks import embed_chunks
from C_retrieval_logic.c04_search_vectors import search_vectors
from C_retrieval_logic.c05_rank_chunks import rank_chunks
from D_storage_layer.chroma_store import collection, store_chunks


def main():
    logger.info("START main pipeline")

    # Step 1: Load files
    files = load_markdown_files()
    logger.info(f"Loaded {len(files)} markdown files.")

    # Step 2: Chunk files
    all_chunks = []
    for path, text in files:
        chunks = chunk_text(path, text)
        all_chunks.extend(chunks)
    logger.info(f"Total chunks created: {len(all_chunks)}")

    # Step 3: Check if already stored in Chroma
    if collection.count() == 0:
        logger.info("No existing Chroma data. Embedding and storing new chunks...")
        embedded_chunks = embed_chunks(all_chunks)
        store_chunks(embedded_chunks)
    else:
        logger.info("Chroma already contains data. Skipping embedding/storage.")

    # Step 4: Get user query and search
    user_question = "How do I start my Python project?"
    top_chunks = search_vectors(user_question, all_chunks)

    # Step 5: Rank results
    ranked_chunks = rank_chunks(top_chunks)

    # Step 6: Call query pipeline (builds prompt + calls LLM)
    response = query(user_question)

    # Step 7: Output result
    logger.info(f"Answer: {response}")
    print("\n=== Assistant Response ===")
    print(response)

    logger.info("END main pipeline")


if __name__ == "__main__":
    main()
    logger.info("Script executed directly.")
