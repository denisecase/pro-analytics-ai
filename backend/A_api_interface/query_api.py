"""
File: backend/A_api_interface/query_api.py

FastAPI endpoint for handling LLM-powered query requests.

This module:
- Receives a user's question via POST at /query.
- Applies optional environment gating (e.g., local-only in 'dev' mode).
- Supports both local development and cloud deployment (e.g., AWS Lambda via Mangum).
- Enforces IP-based rate limiting (1 request/hour) using `slowapi` to discourage abuse.
- Includes CORS middleware for frontend compatibility.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sys
from pathlib import Path

# Add Rate limiting
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

# Ensure project root is in sys.path for imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Local imports
from utils.logger import logger
from utils.config import ENV  
from A_api_interface.query_schema import QueryRequest, QueryResponse
from backend.B_prompt_model.b0_pipeline import query  

app = FastAPI()

# Rate limiter: 1 request per IP per hour
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Exception handler for rate limits
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    logger.warning(f"Rate limit exceeded: {request.client.host}")
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Please try again later."}
    )

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MAIN POST endpoint
@app.post("/query", response_model=QueryResponse)
@limiter.limit("1/hour")  
async def ask_question(request: Request, payload: QueryRequest):
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
