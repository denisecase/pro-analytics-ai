import os
from dotenv import load_dotenv
from utils.logger import logger

# ==========================================================
# Load environment variables
# ==========================================================

# Check environment: dev (local), prod (deployed)
ENV = os.getenv("ENV", "dev")

if ENV == "dev":
    dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
    load_dotenv(dotenv_path)
    logger.info(f"Loaded .env from {dotenv_path}")
else:
    logger.info("Running in production — relying on environment variables.")

# ==========================================================
# Model and System Configuration
# ==========================================================

# Quantization Mode:
# - none  → hosted APIs like OpenAI/OpenRouter
# - 8bit → local 8-bit quantized model (bitsandbytes)
# - 4bit → local 4-bit quantized model (AutoGPTQ)
QUANT_MODE = os.getenv("QUANT_MODE", "none").lower()

# Hosted LLM API Providers
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# Local HuggingFace Model Name (only if QUANT_MODE is "8bit" or "4bit")
MODEL_NAME = os.getenv("MODEL_NAME", "TheBloke/TinyLlama-1.1B-Chat-v1.0-GPTQ")

# Model settings
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Embedding settings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
VECTOR_DB = os.getenv("VECTOR_DB", "chroma")
