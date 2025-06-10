# 🎙️ GenVoice-AI
**GenVoice-AI** is a modular, plug-and-play framework for generating AI-driven voice and video content from text using Retrieval-Augmented Generation (RAG). It supports multiple providers like **HeyGen** and **ElevenLabs**, and is extensible for future integrations.

![HeyGen Flow Diagram](docs/flow_diagram.png)
---

## 🔍 Overview

This project demonstrates how to:

- Use **RAG** (Retrieval-Augmented Generation) to extract meaningful information from documents
- Generate video scripts using **OpenAI GPT / Mistral**
- Convert scripts into professional videos using **HeyGen’s API**

---

## 🏗️ Architecture

1. **Document Indexing (FAISS / Chroma / Qdrant)**
2. **RAG Chain (LangChain or custom logic)**
3. **Script Generation via OpenAI or Mistral**
4. **HeyGen API for video rendering**
5. **Frontend: Streamlit or Gradio** or python backend or API based

---

## 🚀 Features

- ✅ **Text-to-Video** with HeyGen
- ✅ **Text-to-Speech** with ElevenLabs
- 🧠 RAG-powered script generation (PDF/Text)
- 🛠️ CLI support for automation
- 🧩 Pluggable provider registry
- 📝 Logging with timestamps & color
- 🔊 Optional Speech-to-Text
- 🔐 Config via `.env`

---

## 📁 Project Structure

```
genvoice-ai/
├── genvoice/
│   ├── cli.py
│   ├── config.py
│   ├── logger.py
│   ├── utils.py
│   ├── registry.py
│   ├── speech_to_text.py
│   └── providers/
│       ├── heygen.py
│       └── elevenlabs.py
├── examples/
│   └── sample_script.txt
├── .env.example
├── requirements.txt
├── main.py
└── README.md
```
---

## 🧩 Providers

| Provider     | Type          | Description                                  |
|--------------|---------------|----------------------------------------------|
| HeyGen       | Text → Video  | Avatar-based video generation from script    |
| ElevenLabs   | Text → Speech | Natural voiceover generation from text       |

---

## 🧪 Example CLI Usage

```bash
# HeyGen Video Generation
python main.py --provider heygen --file examples/sample_script.txt

# ElevenLabs Audio Generation
python main.py --provider elevenlabs --file examples/sample_script.txt
```

---

## 🧑‍💻 Setup Instructions

1. Clone & Install
```bash
git clone https://github.com/supermldev/genvoice-ai.git
cd genvoice-ai
pip install -r requirements.txt
```

Configure .env
```bash
cp .env.example .env
# Fill in API keys, voice/avatar IDs, etc.
```
.env Configuration
```
# Common
OPENAI_API_KEY=your_openai_api_key

# HeyGen
HEYGEN_API_KEY=your_heygen_api_key
HEYGEN_AVATAR_ID=Angela-inTshirt-20220820
HEYGEN_VOICE_ID=1bd001e7e50f421d891986aad5158bc8

# ElevenLabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=your_elevenlabs_voice_id

# Logging
GENVOICE_LOG_FILE=genvoice.log
```
## RAG for Script Generation

Powered by LangChain & OpenAI to summarize text or PDF input into a script:

```bash
examples/sample_script.txt → 🎬 video/audio script
```

## 🧰 Logging & Debugging
All logs are saved to GENVOICE_LOG_FILE with timestamp + color output:
```angular2html
[2025-06-10 12:32:05] [INFO] 📬 API Response: ...
[2025-06-10 12:32:06] [ERROR] ❌ Failed to generate video
```


## 🧱 Extending with New Providers

Create a new module under genvoice/providers/ and register it in registry.py:

```python
# registry.py
from .providers import mynewprovider

PROVIDER_REGISTRY = {
    "heygen": heygen.generate_video,
    "elevenlabs": elevenlabs.generate_video,
    "mynew": mynewprovider.generate_video,
}
```
## 📦 Folder Structure

```
genvoice-ai/
│
├── app.py                  # Main CLI or runner
├── .env.example            # Sample environment variables
├── requirements.txt
├── README.md
│
├── genvoice/
│   ├── core/               # Core logic
│   │   ├── document_loader.py
│   │   ├── vector_store.py
│   │   └── script_generator.py
│   │
│   ├── providers/          # Modular video/voice services
│   │   ├── heygen.py
│   │   └── elevenlabs.py   # e.g., future text-to-speech module
│   │
│   ├── utils/              # Helpers (logging, polling, etc.)
│   └── config.py           # Config loader and constants
│
└── examples/
    └── sample_script.txt
```

## 📹 Example Use Cases
	•	🎓 Educational Explainers
	•	🏢 Internal Corporate Training
	•	📢 Marketing Demos
	•	🧾 Document Summaries into Video

## 🎯 Roadmap
	•	HeyGen Video Support
	•	ElevenLabs Audio Support
	•	RAG Script Generation
	•	Provider Registry Pattern
	•	Webhook support
	•	Text + Audio → Final Video (FFmpeg)
	•	UI (Gradio/Streamlit)

## 📄 License
MIT © SuperML.dev
Free to use and modify with credit.

> ##  ✨ Powered by SuperML.dev
