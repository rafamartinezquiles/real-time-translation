import React, { useEffect, useState } from "react";
import Layout from "./components/Layout";
import UploadForm from "./components/UploadForm";
import ResultView from "./components/ResultView";
import { fetchLanguages, LanguageOption, TranslationResult } from "./api";

const App: React.FC = () => {
  const [languages, setLanguages] = useState<LanguageOption[]>([]);
  const [result, setResult] = useState<TranslationResult | null>(null);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    async function loadLanguages() {
      try {
        const langs = await fetchLanguages();
        setLanguages(langs);
      } catch (e: any) {
        setError(e.message || "Failed to load languages.");
      }
    }
    loadLanguages();
  }, []);

  return (
    <Layout>
      <div className="two-column">
        <UploadForm
          languages={languages}
          onResult={(res) => {
            setResult(res);
            setError("");
          }}
          onError={(msg) => {
            setError(msg);
            setResult(null);
          }}
        />
        <ResultView result={result} error={error} />
      </div>
    </Layout>
  );
};

export default App;
