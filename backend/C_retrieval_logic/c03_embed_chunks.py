from sentence_transformers import SentenceTransformer
from utils.logger import logger

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks: list[dict]) -> list[dict]:
    texts = [chunk["text"] for chunk in chunks]
    logger.info(f"Embedding {len(texts)} chunks...")
    vectors = model.encode(texts).tolist()
    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector
    logger.info("Embedding complete.")
    return chunks
