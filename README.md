# QuietPlaces - Backend (Starter)

## Overview
Simple FastAPI backend for the project. Provides endpoints to create/list places and a /health endpoint.
Uses SQLAlchemy and supports PostgreSQL via `DATABASE_URL` env var. Defaults to a local SQLite file for easy testing.

## Files
- app/main.py         - FastAPI app entry
- app/db.py           - DB engine & session setup
- app/models.py       - SQLAlchemy models + Pydantic schemas
- app/routes.py       - API routes
- requirements.txt
- Dockerfile
- tests/test_api.py   - basic pytest tests using TestClient
- .env.example        - example environment variables

## Quick steps to run locally in PyCharm
1. Open PyCharm -> Open directory `backend_starter/backend` as project.
2. Create a virtual environment (python 3.10+).
3. Install requirements: `pip install -r requirements.txt`
4. (Optional) To use PostgreSQL, set environment variable `DATABASE_URL` to your Postgres connection string.
   Example: `postgresql://dev:devpassword@localhost:5432/quietdb`
5. Run the app:
   `uvicorn app.main:app --reload --port 8000 --host 0.0.0.0`
6. Open http://localhost:8000/docs for interactive API docs.

## Run tests
From project root run: `pytest -q`
