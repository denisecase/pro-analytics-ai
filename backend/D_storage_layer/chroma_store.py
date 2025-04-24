# File: backend/D_storage_layer/chroma_store.py
# Persist: Embeddings / Text chunks / Metadata (e.g., source path)

import chromadb
from chromadb.config import Settings
from utils.logger import logger

client = chromadb.Client(Settings(
    persist_directory="backend/D_storage_layer/chroma_store"
))

collection = client.get_or_create_collection(name="project-docs")

def store_chunks(chunks: list[dict]):
    logger.info(f"Storing {len(chunks)} chunks in Chroma...")
    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[f"{i}-{c['source']}" for i, c in enumerate(chunks)]
    )
    logger.info("Chunks stored successfully.")
