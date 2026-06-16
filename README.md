# YouTube Transcript Chatbot Extension

A Chrome extension that allows users to ask questions about any YouTube video using transcript-based Retrieval-Augmented Generation (RAG).

## Features

* Ask questions about the current YouTube video
* Automatic transcript retrieval
* LangChain-powered retrieval pipeline
* Hugging Face LLM integration
* Sidebar interface inside YouTube
* FastAPI backend

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* FAISS
* Hugging Face

### Frontend

* Chrome Extension (Manifest V3)
* JavaScript
* CSS

## Project Structure

```text
backend/
├── app.py
├── chatbot.py
└── .env

extension/
├── manifest.json
├── content.js
└── sidebar.css
```

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Add your Hugging Face token to `.env`
5. Run FastAPI:

```bash
uvicorn app:app --reload
```

6. Load the extension via:

```text
chrome://extensions
```

## Future Improvements

* Streaming responses
* Timestamp citations
* Transcript caching
* User authentication
* Chrome Web Store deployment
