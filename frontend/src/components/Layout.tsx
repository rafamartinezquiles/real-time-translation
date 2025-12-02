import React, { ReactNode } from "react";

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout">
      <header className="header">
        <h1>Offline OCR Translator</h1>
        <p className="subtitle">
          Upload an image or text file, extract the text, and translate it —
          no external APIs.
        </p>
      </header>
      <main className="main">{children}</main>
      <footer className="footer">
        <span>Built with Python, TypeScript, and open-source tools.</span>
      </footer>
    </div>
  );
};

export default Layout;
