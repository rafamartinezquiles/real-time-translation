import React from "react";
import { LanguageOption } from "../api";

interface LanguageSelectorProps {
  label: string;
  value: string;
  options: LanguageOption[];
  onChange: (value: string) => void;
}

const LanguageSelector: React.FC<LanguageSelectorProps> = ({
  label,
  value,
  options,
  onChange
}) => {
  return (
    <div className="field">
      <label className="field-label">{label}</label>
      <select
        className="select"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        <option value="" disabled>
          Choose a language...
        </option>
        {options.map((lang) => (
          <option key={lang.code} value={lang.code}>
            {lang.name} ({lang.code})
          </option>
        ))}
      </select>
    </div>
  );
};

export default LanguageSelector;
