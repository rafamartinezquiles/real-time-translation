# Offline OCR & AI Translation System
A privacy-focused, fully offline tool for extracting and translating text from images, PDFs, and documents — powered by Tesseract OCR, Argos Translate, FastAPI, TypeScript, and React.
![](images/System.gif)

## Overview and Background
This project delivers a fully offline, end-to-end pipeline for reading and translating text from virtually any document format, including images (JPG/PNG), photos, screenshots, and standard PDFs. By avoiding cloud APIs and paid services, it prioritizes privacy, accessibility, and transparency, relying entirely on open-source OCR and translation models to process content locally.

The system combines several key components to achieve this: Tesseract for optical character recognition, Argos Translate for offline neural machine translation, FastAPI for backend orchestration of OCR, PDF parsing, and translation, React + TypeScript with Vite for a fast and intuitive browser-based interface, and PyPDF2 for efficient PDF text extraction. Together, these tools make document translation universal, offline, and effortless, empowering anyone to understand information across languages without requiring specialized knowledge or an internet connection.