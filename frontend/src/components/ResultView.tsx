import React from "react";
import { TranslationResult } from "../api";

interface ResultViewProps {
  result: TranslationResult | null;
  error: string;
}

const ResultView: React.FC<ResultViewProps> = ({ result, error }) => {
  if (error) {
    return (
      <div className="card error-card">
        <h2 className="card-title">Something went wrong</h2>
        <p>{error}</p>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="card">
        <h2 className="card-title">Result</h2>
        <p className="card-description">
          The extracted and translated text will appear here.
        </p>
      </div>
    );
  }

  return (
    <div className="card">
      <h2 className="card-title">Translation Result</h2>
      <div className="meta-row">
        <span>Detected language: {result.detected_language}</span>
        <span>Target: {result.target_language}</span>
        <span>OCR: {result.ocr_language}</span>
      </div>

      <div className="text-columns">
        <div className="text-block">
          <h3>Original text</h3>
          <pre>{result.original_text}</pre>
        </div>
        <div className="text-block">
          <h3>Translated text</h3>
          <pre>{result.translated_text}</pre>
        </div>
      </div>
    </div>
  );
};

export default ResultView;
