import os
from dotenv import load_dotenv
from utils.logger import logger

# Load .env only in dev environments
ENV = os.getenv("ENV", "dev")

if ENV == "dev":
    dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
    load_dotenv(dotenv_path)
    logger.info(f"Loaded .env from {dotenv_path}")
else:
    logger.info("Running in production — relying on environment variables.")


# Required: Set LLM Provider 
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter").lower()

# One is required, the other is optional
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Optional: Set model name or API URL here too
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Optional: Future-proof config options
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
VECTOR_DB = os.getenv("VECTOR_DB", "chroma")



