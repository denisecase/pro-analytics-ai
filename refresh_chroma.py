# File: refresh_chroma.py (in root directory)
import os
from backend.D_storage_layer.chroma_loader import get_markdown_files, chunk_markdown
from backend.D_storage_layer.chroma_store import store_chunks
from backend.utils.logger import logger

# Define the path to the raw docs
PRO_ANALYTICS_PATH = "backend/D_storage_layer/raw_docs/pro-analytics-01"


def refresh_chroma():
    """
    Rebuilds the ChromaDB index by reloading markdown files and storing fresh chunks.
    """
    if not os.path.exists(PRO_ANALYTICS_PATH):
        logger.error(f"ERROR: Path not found: {PRO_ANALYTICS_PATH}")
        return
    
    logger.info("Refreshing ChromaDB with new content...")
    
    all_chunks = []
    markdown_files = get_markdown_files()
    
    for md_file in markdown_files:
        chunks = chunk_markdown(md_file)
        all_chunks.extend(chunks)
    
    if all_chunks:
        store_chunks(all_chunks)
        logger.info(f"Successfully reinitialized ChromaDB with {len(all_chunks)} chunks.")
    else:
        logger.warning("No chunks found to store.")

if __name__ == "__main__":
    refresh_chroma()
