#!/bin/bash
source .venv/bin/activate
uvicorn backend.A_api_interface.query_api:app --reload --port 8000
