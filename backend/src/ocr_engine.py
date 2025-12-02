"""
ocr_engine.py

This module is responsible solely for Optical Character Recognition (OCR).
It converts an image into plain text using Tesseract.

Keeping OCR in its own module makes it easy to:
- Swap Tesseract for another engine in the future.
- Reuse OCR logic in other parts of the application.
"""

from io import BytesIO
from PIL import Image
import pytesseract
from typing import Optional


# IMPORTANT: Windows path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def run_ocr_on_image_bytes(
    image_bytes: bytes, ocr_language: str = "eng"
) -> str:
    """
    Run OCR on raw image bytes and return the extracted text.

    Parameters
    ----------
    image_bytes : bytes
        The raw bytes of the uploaded image file.
    ocr_language : str, optional
        The language code used by Tesseract (e.g., 'eng', 'spa').

    Returns
    -------
    str
        The text recognized in the image. This text may contain
        line breaks and minor OCR errors, depending on image quality.
    """
    # Convert raw bytes to a PIL image that Tesseract can understand
    image = Image.open(BytesIO(image_bytes))

    # pytesseract.image_to_string performs the actual OCR
    extracted_text = pytesseract.image_to_string(image, lang=ocr_language)

    # It is usually a good idea to strip leading/trailing whitespace
    return extracted_text.strip()


def is_probably_image(content_type: Optional[str]) -> bool:
    """
    Very small helper to decide if the file is likely to be an image
    based on its MIME type.

    Parameters
    ----------
    content_type : str or None
        The MIME type of the incoming file, e.g. 'image/png'.

    Returns
    -------
    bool
        True if it looks like an image, False otherwise.
    """
    if not content_type:
        return False

    return content_type.startswith("image/")
