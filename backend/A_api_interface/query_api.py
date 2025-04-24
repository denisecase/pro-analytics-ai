# File: backend/A_api_interface/query_api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sys
from pathlib import Path

# Ensure project root is in sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Local imports
from utils.logger import logger

from utils.logger import logger
from utils.config import ENV  
from A_api_interface.query_schema import QueryRequest, QueryResponse
from B_prompt_model.query_pipeline import query  # was: from main import query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query", response_model=QueryResponse)
async def ask_question(payload: QueryRequest):
    if ENV != "dev":
        logger.info(f"Ignoring query in {ENV} mode.")
        return QueryResponse(
            answer=(
                "Hello!\n"
                "Thank you for visiting. This assistant runs locally, but is not yet hosted for wider access."
            )
        )

    question = payload.question
    logger.info(f"Received query: {question}")
    answer = query(question)
    return QueryResponse(answer=answer)
