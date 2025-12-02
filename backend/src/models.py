"""
models.py

Pydantic models that describe the data shapes exchanged
between the backend and the frontend.
"""

from pydantic import BaseModel


class TranslationResponse(BaseModel):
    """
    This model describes the JSON response returned after
    processing an uploaded file and translating its text.
    """

    detected_language: str
    target_language: str
    ocr_language: str
    original_text: str
    translated_text: str
