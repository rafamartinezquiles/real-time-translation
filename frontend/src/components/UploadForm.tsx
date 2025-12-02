import React, { useRef, useState } from "react";
import { LanguageOption, uploadAndTranslate, TranslationResult } from "../api";
import LanguageSelector from "./LanguageSelector";

interface UploadFormProps {
  languages: LanguageOption[];
  onResult: (result: TranslationResult) => void;
  onError: (message: string) => void;
}

const UploadForm: React.FC<UploadFormProps> = ({
  languages,
  onResult,
  onError
}) => {
  const [targetLanguage, setTargetLanguage] = useState<string>("");
  const [ocrLanguage, setOcrLanguage] = useState<string>("eng");
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);

  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const fileInput = fileInputRef.current;

    if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
      onError("Please choose a file to upload.");
      return;
    }

    if (!targetLanguage) {
      onError("Please choose a target language.");
      return;
    }

    const file = fileInput.files[0];

    setIsSubmitting(true);
    onError(""); // clear previous error if any

    try {
      const result = await uploadAndTranslate(file, targetLanguage, ocrLanguage);
      onResult(result);
    } catch (e: any) {
      onError(e.message || "An unexpected error occurred.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <h2 className="card-title">Upload &amp; Translate</h2>
      <p className="card-description">
        Images will be processed with OCR. Plain text files will be read
        directly.
      </p>

      <div className="field">
        <label className="field-label">File</label>
        <input
          ref={fileInputRef}
          type="file"
          className="file-input"
          accept="image/*,.txt"
        />
        <small className="help-text">
          Supported: image files (for OCR) and simple text files.
        </small>
      </div>

      <LanguageSelector
        label="Translate into"
        value={targetLanguage}
        options={languages}
        onChange={setTargetLanguage}
      />

      <div className="field">
        <label className="field-label">OCR language code (Tesseract)</label>
        <input
          className="text-input"
          value={ocrLanguage}
          onChange={(e) => setOcrLanguage(e.target.value)}
          placeholder="e.g. eng, spa, fra..."
        />
        <small className="help-text">
          This affects how the OCR engine reads the image. It is often similar
          to the target language, but it does not have to be.
        </small>
      </div>

      <button className="primary-button" type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Translating..." : "Translate"}
      </button>
    </form>
  );
};

export default UploadForm;
