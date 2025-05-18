# File: backend/D_storage_layer/chroma_store.py
# ==========================================================
# Centralized ChromaDB Logic for storage and retrieval
# - Stores embeddings and metadata
# - Handles local retrieval for high-confidence matches
# ==========================================================

import os
import chromadb
from chromadb.config import Settings
from backend.utils.logger import logger

# Get absolute path
CHROMA_PERSIST_DIRECTORY = os.path.abspath("backend/D_storage_layer/chroma_store")
print(f"ChromaDB is using persist directory: {CHROMA_PERSIST_DIRECTORY}")

# Ensure the directory exists
if not os.path.exists(CHROMA_PERSIST_DIRECTORY):
    print(f"Directory {CHROMA_PERSIST_DIRECTORY} not found. Creating it now.")
    os.makedirs(CHROMA_PERSIST_DIRECTORY)
else:
    print(f"Directory {CHROMA_PERSIST_DIRECTORY} already exists.")

# Initialize ChromaDB Client
client = chromadb.PersistentClient(
    path=CHROMA_PERSIST_DIRECTORY
)

# Get or create the collection
collection = client.get_or_create_collection(name="project-docs")

# Confidence threshold for high-quality matches
CONFIDENCE_THRESHOLD = 0.75

def store_chunks(chunks: list[dict]):
    """
    Stores chunks in ChromaDB for later retrieval.

    Args:
        chunks (list[dict]): List of chunk dictionaries to store.
    """
    print(f"Number of documents in collection: {collection.count()}")

    logger.info(f"Storing {len(chunks)} chunks in Chroma...")

    # Enhanced Metadata
    documents = []
    metadatas = []
    ids = []

    for i, chunk in enumerate(chunks):
        if "pro-analytics-01" in chunk["source"].lower():
            documents.append(chunk["text"])
            tags = ["pro-analytics-01"]  # Base tag

            # Phase Tags
            if "machine-setup" in chunk["source"].lower():
                tags.append("Machine Setup")
            if "project-initialization" in chunk["source"].lower():
                tags.append("Project Initialization")
            if "repeatable-workflow" in chunk["source"].lower():
                tags.append("Repeatable Workflow")

            # Task Type Tags
            if "setup" in chunk["text"].lower():
                tags.append("Setup Task")
            if "initialize" in chunk["text"].lower():
                tags.append("Initialization Task")
            if "workflow" in chunk["text"].lower():
                tags.append("Workflow Task")

            # Cheat Sheet Tags
            if "cheatsheet" in chunk["text"].lower():
                tags.append("CheatSheet")

            # Command Tags
            if "git " in chunk["text"].lower():
                tags.append("Git Command")
            if "pip " in chunk["text"].lower():
                tags.append("Pip Command")
            if "python " in chunk["text"].lower() or "py " in chunk["text"].lower():
                tags.append("Python Command")

            # Audio Guide Tags
            if "audio guides" in chunk["text"].lower():
                tags.append("Audio Guide")

            # Explore Section Tags
            if "explore" in chunk["text"].lower():
                tags.append("Explore Section")

            metadatas.append({
                "source": chunk["source"],
                 "tags": ", ".join(tags)
            })
            ids.append(f"{i}-{chunk['source']}")

    # Add to ChromaDB
    logger.info(f"Adding {len(documents)} documents to ChromaDB.")
    existing_ids = set(collection.get()['ids'])
    new_documents, new_metadatas, new_ids = [], [], []

    for doc, meta, doc_id in zip(documents, metadatas, ids):
        if doc_id not in existing_ids:
            new_documents.append(doc)
            new_metadatas.append(meta)
            new_ids.append(doc_id)

    if new_documents:
        collection.add(
            documents=new_documents,
            metadatas=new_metadatas,
            ids=new_ids
        )
        
    # Verification Check
    current_count = collection.count()
    logger.info(f"Number of documents in collection after insertion: {current_count}")

    if current_count != len(ids):
        logger.warning(f"Discrepancy in document count. Expected {len(ids)}, found {current_count}")
    else:
        logger.info(f"Chunks stored successfully with metadata. Here are the first 5 document IDs:")
        logger.info(f"{ids[:5]}")

    # Additional Verification - Fetch back a sample
    sample_docs = collection.query(query_texts=["setup"], n_results=2)
    logger.info(f"Sample query results: {sample_docs}")


def query_chunks(user_input: str, top_k: int = 3) -> list[str]:
    """
    Queries ChromaDB for relevant chunks based on user input.

    Args:
        user_input (str): The user's question or query.
        top_k (int): Number of top results to retrieve.

    Returns:
        list[str]: High-confidence results if found, empty list otherwise.
    """
    logger.info(f"Attempting local retrieval for: {user_input}")

    logger.info("Collection Stats:")
    logger.info(f"Total documents: {collection.count()}")
    results = collection.get()
    for idx, doc in enumerate(results['documents'][:5]):
        logger.info(f"{idx+1}. {doc}")

    results = collection.query(
        query_texts=[user_input],
        n_results=top_k
    )
    
    # Loop through flattened lists
    high_confidence_chunks = []
    for doc, meta, dist in zip(results['documents'], results['metadatas'], results['distances']):
        
        # Check if `dist` is a non-empty list
        if isinstance(dist, list) and len(dist) > 0:
            actual_distance = dist[0]
        else:
            logger.warning(f"No distance found for document: {meta}. Skipping.")
            continue  # Skip this iteration
        
        # Distance Check - Distance is inverse of confidence
        if actual_distance <= CONFIDENCE_THRESHOLD:  
            logger.info(f"Found a confident match: {meta}")
             # Extract string from list
            high_confidence_chunks.append(doc[0]) 

    if high_confidence_chunks:
        logger.info(f"Local retrieval successful: Found {len(high_confidence_chunks)} chunks.")
        return high_confidence_chunks
    
    logger.warning("Local retrieval not sufficient. Proceeding with RAG.")
    return []