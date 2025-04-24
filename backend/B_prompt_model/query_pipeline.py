from C_retrieval_logic.c01_load_files import load_markdown_files
from C_retrieval_logic.c02_chunk_text import chunk_text
from C_retrieval_logic.c03_embed_chunks import embed_chunks
from C_retrieval_logic.c04_search_vectors import search_vectors
from C_retrieval_logic.c05_rank_chunks import rank_chunks
from B_prompt_model.call_model import call_model

def query(user_input: str) -> str:
    files = load_markdown_files()
    all_chunks = []
    for path, text in files:
        all_chunks.extend(chunk_text(path, text))

    embedded_chunks = embed_chunks(all_chunks)
    top_chunks = search_vectors(user_input, embedded_chunks)
    ranked_chunks = rank_chunks(top_chunks)

    return call_model(user_input, [chunk["text"] for chunk in ranked_chunks])
