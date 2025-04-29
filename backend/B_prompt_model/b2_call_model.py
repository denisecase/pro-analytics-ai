# ==========================================================
# Layer B2 - Call Model (b2_call_model.py)
# ==========================================================
# This file handles model interaction in a Retrieval-Augmented Generation (RAG) system.
#
# It is responsible for:
# - Loading the Large Language Model (LLM) based on configuration.
#   - "none"  then use external APIs like OpenAI or OpenRouter.
#   - "8bit"  then load a local 8-bit quantized model using bitsandbytes.
#   - "4bit"  then load a local 4-bit quantized model using AutoGPTQ.
# - Accepting prompts built from retrieved knowledge and user questions.
# - Sending prompts to the LLM and returning generated answers.
#
# This module supports both API-based and fully local deployments.
#
# In this RAG system:
# - Retrieved documents (Layer C) + user questions form the prompt (Layer B1).
# - The prompt is sent to the LLM via this module (Layer B2).
# - The system behavior is customized using assistant guidelines (GUIDELINES.md).

# ==========================================================

from dotenv import load_dotenv
from utils.logger import logger
from backend.B_prompt_model.b1_build_prompt import build_prompt
from utils.config import (
    LLM_PROVIDER,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    OPENAI_MODEL,
    MODEL_NAME,
    QUANT_MODE  # "none", "8bit", or "4bit"
)
import os

# Load environment variables
load_dotenv()

# Initialize model/client globals
client = None
model = None
tokenizer = None

# ==========================================================
# Model Loaders
# ==========================================================

def load_none_model():
    from openai import OpenAI

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

    return client, None, None

def load_8bit_model():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        # quantization_config=quant_config,  # Quant config is commented out for now
        device_map="auto",
        trust_remote_code=True
    )
    logger.info("Using 8-bit quantized model loaded locally.")
    return None, model, tokenizer

def load_4bit_model():
    from auto_gptq import AutoGPTQForCausalLM
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = AutoGPTQForCausalLM.from_quantized(
        MODEL_NAME,
        device_map="auto",
        trust_remote_code=True
    )
    logger.info("Using 4-bit quantized model loaded locally.")
    return None, model, tokenizer

# ==========================================================
# Load the correct model
# ==========================================================

if QUANT_MODE == "none":
    client, model, tokenizer = load_none_model()
elif QUANT_MODE == "8bit":
    client, model, tokenizer = load_8bit_model()
elif QUANT_MODE == "4bit":
    client, model, tokenizer = load_4bit_model()
else:
    raise ValueError(f"Unsupported QUANT_MODE: {QUANT_MODE}")


# ==========================================================
# Main Call Function
# ==========================================================

def call_model(question: str, chunks: list[str]) -> str:
    """
    Builds a full Retrieval-Augmented Generation (RAG) prompt by combining assistant guidelines,
    retrieved context chunks, and the user's question, then sends it to the configured LLM
    (hosted API or local quantized model) and returns the generated answer.

    Args:
        question (str): The user's input question.
        chunks (list[str]): Retrieved context snippets related to the question.

    Returns:
        str: The model's generated answer based on the combined prompt.
    """

    if not chunks:
        logger.warning("No relevant content found. Returning fallback message.")
        return (
            "Sorry, I can't help with that.\n"
            "My knowledge is focused on helping you set up professional Python projects "
            "the recommended way."
        )

    logger.info(f"Using {len(chunks)} chunks for prompt context.")
    prompt = build_prompt(question, chunks)

    estimated_tokens = len(prompt) // 4
    logger.info(f"Prompt length: {len(prompt)} characters (~{estimated_tokens} tokens)")
    logger.debug(f"Prompt sent to model:\n{prompt}")

    if QUANT_MODE == "none":
        # Using OpenAI or OpenRouter API
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0  # deterministic
        )
        answer = response.choices[0].message.content.strip()

    else:
        # Using local model (8bit or 4bit)
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_new_tokens=512)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    logger.info("Received response from model.")
    return answer
