"""
translation_engine.py

This module encapsulates all translation-related functionality.

We use Argos Translate, which is an offline, open-source translation
library (so no external paid API calls are needed).
"""

from typing import Tuple

from langdetect import detect, LangDetectException
from argostranslate import package, translate

from .config import LANGUAGE_CODES


def _ensure_language_package_installed(source_lang_code: str, target_lang_code: str) -> None:
    """
    Ensure that an Argos Translate language package for the desired
    source-target pair is installed.

    Notes
    -----
    - In practice, language packages are installed via the CLI:
        argos-translate-cli --install <package-id>
      For example:
        argos-translate-cli --install en_es
    - Here we simply load installed packages. If none is found for
      this pair, we raise an error so the caller can handle it.
    """
    # Load installed Argos Translate packages
    package.update_package_index()
    available_packages = package.get_installed_packages()

    for p in available_packages:
        if p.from_code == source_lang_code and p.to_code == target_lang_code:
            # We found a suitable package
            return

    # If we get here, then the correct package is not installed
    raise RuntimeError(
        f"No Argos Translate package installed for {source_lang_code} -> {target_lang_code}. "
        "Please install it using 'argos-translate-cli --install "
        f"{source_lang_code}_{target_lang_code}'."
    )


def detect_language(text: str) -> str:
    """
    Detect the language of a given text using langdetect.

    Parameters
    ----------
    text : str
        The input text whose language we want to detect.

    Returns
    -------
    str
        Two-letter ISO language code like 'en', 'es', etc.

    Notes
    -----
    - Language detection is heuristic and may not be perfect,
      especially for very short texts.
    """
    try:
        return detect(text)
    except LangDetectException:
        # If detection fails, fall back to English as a neutral default
        return "en"


def translate_text(
    original_text: str, target_language_code: str
) -> Tuple[str, str]:
    """
    Translate the provided text to the desired target language.

    Parameters
    ----------
    original_text : str
        Text to translate.
    target_language_code : str
        ISO code of the target language (e.g., 'en', 'es').

    Returns
    -------
    (detected_language, translated_text) : Tuple[str, str]
        detected_language : ISO code of the language detected in original_text.
        translated_text   : The translated text.

    Raises
    ------
    RuntimeError
        If no appropriate Argos Translate package is installed.
    """
    # First detect the source language from the text
    detected_lang_code = detect_language(original_text)

    # Make sure Argos has a model for this translation pair
    _ensure_language_package_installed(detected_lang_code, target_language_code)

    # Load translations
    translate.load_installed_packages()
    available_translations = translate.get_installed_translations()

    # Find the exact translation object we need
    translator = None
    for t in available_translations:
        if t.from_lang.code == detected_lang_code and t.to_lang.code == target_language_code:
            translator = t
            break

    if translator is None:
        raise RuntimeError(
            f"No installed translator found for {detected_lang_code} -> {target_language_code}."
        )

    # Perform translation
    translated = translator.translate(original_text)
    return detected_lang_code, translated
