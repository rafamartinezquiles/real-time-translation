"""
config.py

Centralized configuration values for the backend application.
Keeping configuration in one place makes the code easier to maintain.
"""

from pathlib import Path

# Base directory of the backend project
BASE_DIR = Path(__file__).resolve().parent.parent

# Directory where we could store temp files (if needed later)
TEMP_DIR = BASE_DIR / "tmp"
TEMP_DIR.mkdir(exist_ok=True)

# Default OCR language (ISO code for Tesseract, e.g. "eng" for English)
DEFAULT_OCR_LANG = "eng"

# Mapping from human-readable language names to ISO codes for Argos & Tesseract.
LANGUAGE_CODES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
}
