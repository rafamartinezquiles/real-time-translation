# Offline OCR & AI Translation System
A privacy-focused, fully offline tool for extracting and translating text from images, PDFs, and documents — powered by Tesseract OCR, Argos Translate, FastAPI, TypeScript, and React.
![](images/System.gif)

## Overview and Background
This project delivers a fully offline, end-to-end pipeline for reading and translating text from virtually any document format, including images (JPG/PNG), photos, screenshots, and standard PDFs. By avoiding cloud APIs and paid services, it prioritizes privacy, accessibility, and transparency, relying entirely on open-source OCR and translation models to process content locally.

The system combines several key components to achieve this: Tesseract for optical character recognition, Argos Translate for offline neural machine translation, FastAPI for backend orchestration of OCR, PDF parsing, and translation, React + TypeScript with Vite for a fast and intuitive browser-based interface, and PyPDF2 for efficient PDF text extraction. Together, these tools make document translation universal, offline, and effortless, empowering anyone to understand information across languages without requiring specialized knowledge or an internet connection.

## Table of Contents
```
real-time-translation
|__ images
|   |__ example.png 
|   |__ System.gif
|__ backend
|   |__ src
|   |   |__ config.py
|   |   |__ install_argos_models.py
|   |   |__ main.py
|   |   |__ models.py
|   |   |__ ocr_engine.py
|   |   |__ routes.py
|   |   |__ translation_engine.py
|__ frontend
|   |__ src
|   |   |__ styles.css
|   |   |__ main.tsx
|   |   |__ api.ts
|   |   |__ App.tsx
|   |__ node_modules
|   |__ index.html
|   |__ package-lock.json
|   |__ package.json
|   |__ tsconfig.json
|   |__ vite.config.ts
README.md
LICENSE
.gitignore
requirements.txt
```

## Getting started

### Resources used
A high-performance Acer Nitro 5 laptop, powered by an Intel Core i7 processor and an NVIDIA GeForce GTX 1650 GPU (4 GB VRAM), was used for model training and evaluation. Due to the large size of the dataset, the training process was computationally demanding and prolonged. Nevertheless, this hardware configuration provided a stable and efficient environment, enabling consistent experimentation and reliable validation of the gesture-recognition models.


### Installing
The project is deployed in a local machine, so you need to install the next software and dependencies to start working:

1. Create and activate the new virtual environment for the project

```bash
conda create --name real-time-translation python=3.11
conda activate real-time-translation
```

2. Clone repository

```bash
git clone https://github.com/rafamartinezquiles/real-time-translation.git
```

3. In the same folder that the requirements are, install the necessary requirements

```bash
cd real-time-translation
pip install -r requirements.txt
```

## Execution
Running this project involves starting both the backend (which performs OCR, PDF processing, and translation) and the frontend (which provides the user interface). The steps below walk through the full execution process in a clear, beginner-friendly way, ensuring that everything works smoothly from the moment the repository is cloned.

Begin by opening a terminal and navigating to the backend/ directory of the project. 

```bash
cd backend
```

This folder contains the Python FastAPI server responsible for the heavy lifting: running OCR through Tesseract, extracting text from PDFs, detecting language, and performing offline translation using Argos Translate. Before starting the server, make sure your Python virtual environment is activated and with the requirements installed!

Since this project performs OCR locally, you must also ensure that Tesseract OCR is installed on your machine. On Windows, this involves installing the “tesseract-ocr-w64-setup” package from the official UB Mannheim build. Once installed, confirm that tesseract.exe is available in your system PATH by typing tesseract --version in your terminal. If the command works, the OCR engine is correctly installed. Before launching the backend, all translation models must be downloaded so the system can translate text between languages offline. This is done through a dedicated helper script. From inside the backend directory, run 

```bash
python -m src.install_argos_models
```

The script will automatically fetch and install the required Argos Translate packages for English, Spanish, French, German, and Italian in both directions. This step only needs to be done once. After the models are installed, the backend is ready to run. Start it with the command:

```bash
uvicorn src.main:app --reload --port 8000
```

With your backend running on http://localhost:8000, the next step is to launch the frontend. Open a second terminal window and navigate to the frontend/ directory. 

```bash
cd frontend
```

The frontend is a React + TypeScript application built with Vite, which provides a fast development server and instant updates as you work. Install the frontend dependencies. This step downloads all required JavaScript packages, including React, Vite, and the components used in the interface.

```bash
npm install
```

Once the installation is complete, start the development server by running:

```bash
npm run dev
```

This will launch the UI at http://localhost:5173. When you open that address in your browser, you will see the full interface with an upload form, language selectors, and a results panel. Behind the scenes, the frontend communicates directly with the FastAPI backend, sending uploaded files for OCR or PDF parsing and receiving translated text in return.

At this point, the entire system is operational. Simply upload any image or PDF and select the target language. If the file is an image, the backend will automatically perform OCR using Tesseract. If the file is a PDF, the system will extract the embedded text using PyPDF2. In both cases, the extracted text is analyzed to determine its original language and then translated offline using the Argos models installed earlier. Within a few seconds, your browser will display both the original extracted text and its translated version side-by-side.

Once both servers are running, no additional setup is required. The system can operate entirely offline, safely processing sensitive documents without sending data to any external services. You can now explore, test, and extend the tool freely, translating documents in a private, efficient, and user-friendly environment.