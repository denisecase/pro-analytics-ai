from utils.logger import logger

def chunk_text(source_path: str, text: str, max_length: int = 300) -> list[dict]:
    logger.info(f"Chunking file: {source_path}")
    chunks = [
        {
            "source": source_path,
            "text": text[i:i+max_length]
        }
        for i in range(0, len(text), max_length)
    ]
    logger.info(f"Created {len(chunks)} chunks from {source_path}")
    return chunks
