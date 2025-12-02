"""
routes.py

This module defines the HTTP routes of the backend API.

We keep routes separate from the main application object to keep the
codebase modular and easy to navigate.
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse

from .models import TranslationResponse
from .ocr_engine import run_ocr_on_image_bytes, is_probably_image
from .translation_engine import translate_text
from .config import DEFAULT_OCR_LANG, LANGUAGE_CODES

router = APIRouter(prefix="/api", tags=["translation"])


@router.get("/languages")
def list_supported_languages():
    """
    Simple endpoint to let the frontend know which languages are
    available as translation targets.

    Returns
    -------
    list of {name, code}
    """
    return [{"name": name, "code": code} for name, code in LANGUAGE_CODES.items()]


@router.post("/translate", response_model=TranslationResponse)
async def translate_file(
    file: UploadFile = File(...),
    target_language_code: str = Form(...),
    ocr_language_code: str = Form(DEFAULT_OCR_LANG),
):
    """
    Accept an uploaded file, run OCR if needed, then translate the extracted text.

    Parameters
    ----------
    file : UploadFile
        The file uploaded by the user (typically an image).
    target_language_code : str
        ISO code of the language to translate into.
    ocr_language_code : str
        Language for the OCR engine (Tesseract).
    """
    # Read the entire uploaded file into memory
    content = await file.read()

    if is_probably_image(file.content_type):
        extracted_text = run_ocr_on_image_bytes(content, ocr_language=ocr_language_code)
    else:
        # If it is not an image, we treat it as a text file.
        # This is a simple fallback – you can expand this to support PDFs.
        try:
            extracted_text = content.decode("utf-8", errors="ignore")
        except Exception:
            raise HTTPException(status_code=400, detail="Unsupported file type or encoding.")

    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="No text could be extracted from the file.")

    try:
        detected_lang_code, translated = translate_text(
            original_text=extracted_text, target_language_code=target_language_code
        )
    except RuntimeError as e:
        # If translation fails because of missing language packages, we return a 500
        raise HTTPException(status_code=500, detail=str(e))

    response = TranslationResponse(
        detected_language=detected_lang_code,
        target_language=target_language_code,
        ocr_language=ocr_language_code,
        original_text=extracted_text,
        translated_text=translated,
    )
    return JSONResponse(content=response.dict())
