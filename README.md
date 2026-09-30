# 🎥 YouTube Video Assistant

An AI-powered Chrome Extension that allows users to interact with YouTube videos through a chatbot.

The application extracts the transcript of a YouTube video and uses AI/NLP techniques to understand the content and provide answers to user questions.

---

## 🚀 Features

- 🎥 Chat with YouTube videos
- 📝 Extract YouTube video transcripts
- 🤖 Ask questions about the video
- 💬 Get AI-generated responses
- 🧠 Uses LangChain for text processing
- 🤗 Uses Hugging Face models
- 🌐 Chrome Extension interface
- ⚡ Python backend with FastAPI
- 🔐 Environment variable support for API tokens

---

## 🏗️ Project Architecture

```text
YouTube-Video-Assistant
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   └── package-lock.json
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── ...
│
├── .env.example
├── .gitignore
├── package-lock.json
└── README.md
