"""
main.py

Entry point of the FastAPI application.

This file:
- Creates the FastAPI app instance.
- Includes the API routes defined in routes.py.
- Configures CORS so the frontend (running on another port) can talk to the backend.

Run this with:
    uvicorn src.main:app --reload
from the backend directory.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router as translation_router

app = FastAPI(
    title="Offline OCR Translator",
    description=(
        "A small web service that performs OCR on uploaded files and "
        "translates the extracted text into a target language, without "
        "using paid external APIs."
    ),
)

# Allow requests from the typical frontend dev server port (e.g., Vite at 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach our translation routes to the main app
app.include_router(translation_router)
