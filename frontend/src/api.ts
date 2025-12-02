/**
 * api.ts
 *
 * Centralized API helpers for talking to the Python backend.
 * This keeps HTTP logic out of the UI components.
 */

export interface LanguageOption {
  name: string;
  code: string;
}

export interface TranslationResult {
  detected_language: string;
  target_language: string;
  ocr_language: string;
  original_text: string;
  translated_text: string;
}

const BACKEND_URL = "http://localhost:8000";

export async function fetchLanguages(): Promise<LanguageOption[]> {
  const response = await fetch(`${BACKEND_URL}/api/languages`);
  if (!response.ok) {
    throw new Error("Failed to load language list from backend.");
  }
  return response.json();
}

export async function uploadAndTranslate(
  file: File,
  targetLanguageCode: string,
  ocrLanguageCode: string
): Promise<TranslationResult> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("target_language_code", targetLanguageCode);
  formData.append("ocr_language_code", ocrLanguageCode);

  const response = await fetch(`${BACKEND_URL}/api/translate`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    const message =
      (errorBody && errorBody.detail) ||
      `Translation failed with status ${response.status}`;
    throw new Error(message);
  }

  return response.json();
}
