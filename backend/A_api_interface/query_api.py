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
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
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

# 1. Middleware first: CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Rate limiting second
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

# 3. API ROUTES Next
# MAIN POST endpoint limit to 10 per minute and 200 per day
@app.post("/query", response_model=QueryResponse)
@limiter.limit("10/minute;200/day")  
async def ask_question(request: Request, payload: QueryRequest):
    # if ENV == "dev":
    #     logger.info(f"Ignoring query in {ENV} mode.")
    #     return QueryResponse(
    #         answer=(
    #             "Hello!\n"
    #             "Thank you for visiting. This assistant runs locally, but is not yet hosted for wider access."
    #         )
    #     )

    question = payload.question
    logger.info(f"Received query: {question}")
    answer = query(question)
    return QueryResponse(answer=answer)


# 4. Redirect root to docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs/")

# 5. Static files for frontend LAST
# Go to http://<your-ec2-ip>:8000/ and it will serve index.html
app.mount("/docs", StaticFiles(directory="docs", html=True), name="static")

