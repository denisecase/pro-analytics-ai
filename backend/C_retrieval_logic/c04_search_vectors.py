from utils.logger import logger

def search_vectors(query: str, embedded_chunks: list[dict], top_k: int = 3) -> list[dict]:
    logger.info("Running placeholder vector search...")
    # Replace with real similarity search later
    return embedded_chunks[:top_k]
