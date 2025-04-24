MAX_CONTEXT_LENGTH = 3000  # characters, not tokens

def build_prompt(question: str, chunks: list[str]) -> str:
    context = "\n\n".join(chunks)
    context = context[:MAX_CONTEXT_LENGTH]  # truncate safely
    return (
        "You are a helpful assistant who only answers questions "
        "based on the provided context.\n\n"
        f"Context:\n{context}\n\nQuestion:\n{question}"
    )
