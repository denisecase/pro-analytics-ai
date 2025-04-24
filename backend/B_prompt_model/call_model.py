# File: backend/B_prompt_model/call_model.py

from dotenv import load_dotenv
from utils.logger import logger
from B_prompt_model.build_prompt import build_prompt
import os
from utils.config import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    OPENAI_MODEL,
)

# Load environment variables
load_dotenv()

# Import OpenAI v1 client
from openai import OpenAI

# Initialize client dynamically
if LLM_PROVIDER == "openrouter":
    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )
    logger.info("Using OpenRouter (free) as LLM provider.")
elif LLM_PROVIDER == "openai":
    client = OpenAI(api_key=OPENAI_API_KEY)
    logger.info("Using OpenAI (paid) as LLM provider.")
else:
    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")


def call_model(question: str, chunks: list[str]) -> str:
    if not chunks:
        logger.warning("No relevant content found. Returning fallback message.")
        return (
            "Sorry, I can’t help with that.\n"
            "My knowledge is focused on helping you set up professional Python projects "
            "the recommended way."
        )

    logger.info(f"Using {len(chunks)} chunks for prompt context.")
    prompt = build_prompt(question, chunks)

    estimated_tokens = len(prompt) // 4
    logger.info(f"Prompt length: {len(prompt)} characters (~{estimated_tokens} tokens)")
    logger.debug(f"Prompt sent to model:\n{prompt}")

    # New v1+ client format
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content.strip()
    logger.info("Received response from model.")
    return answer
