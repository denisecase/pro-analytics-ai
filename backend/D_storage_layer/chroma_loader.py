# File: backend/D_storage_layer/chroma_loader.py
import os
from backend.D_storage_layer.chroma_store import store_chunks
from backend.utils.logger import logger

# Path to the local clone of pro-analytics-01 repo
PRO_ANALYTICS_PATH = "backend/D_storage_layer/raw_docs/pro-analytics-01"

def get_markdown_files():
    """
    Recursively retrieves all Markdown files from the pro-analytics-01 directory.
    """
    md_files = []
    for root, dirs, files in os.walk(PRO_ANALYTICS_PATH):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    logger.info(f"Found {len(md_files)} markdown files.")
    return md_files

def chunk_markdown(file_path):
    """
    Chunk markdown content by headers or paragraphs.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Split by two new lines as a rough chunking strategy
    chunks = content.split("\n\n")
    
    # Create a chunk list
    chunk_data = []
    for idx, chunk in enumerate(chunks):
        if len(chunk.strip()) > 20:  # Avoid storing very tiny fragments
            chunk_data.append({
                "text": chunk.strip(),
                "source": file_path
            })
    
    logger.info(f"Chunked {file_path} into {len(chunk_data)} parts.")
    return chunk_data

def load_and_store():
    """
    Loads markdown files, chunks them, and stores them in ChromaDB.
    """
    all_chunks = []
    markdown_files = get_markdown_files()
    
    for md_file in markdown_files:
        chunks = chunk_markdown(md_file)
        all_chunks.extend(chunks)
    
    if all_chunks:
        store_chunks(all_chunks)
        logger.info(f"Successfully stored {len(all_chunks)} chunks into ChromaDB.")
    else:
        logger.warning("WARNING: No chunks found to store.")
