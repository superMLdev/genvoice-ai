# 🎥 heygenai — Create AI Videos with RAG and HeyGen

**Generate AI explainer videos from documents or queries using Retrieval-Augmented Generation (RAG) and HeyGen API.**

![HeyGen Flow Diagram](docs/flow_diagram.png)
---

## 🔍 Overview

This project demonstrates how to:

- Use **RAG** (Retrieval-Augmented Generation) to extract meaningful information from documents
- Generate video scripts using **OpenAI GPT / Mistral**
- Convert scripts into professional videos using **HeyGen’s API**
- Run everything through an interactive **Streamlit** or **Gradio** interface

---

## 🚀 Features

- 📄 Upload or point to documents
- 🧠 RAG retrieves context using vector search
- ✍️ LLM generates a human-like narration script
- 🗣️ Script is turned into a talking-head avatar video using HeyGen
- 🎬 Instant video link or download

---

## 🏗️ Architecture

1. **Document Indexing (FAISS / Chroma / Qdrant)**
2. **RAG Chain (LangChain or custom logic)**
3. **Script Generation via OpenAI or Mistral**
4. **HeyGen API for video rendering**
5. **Frontend: Streamlit or Gradio**

---

## 🧑‍💻 Setup

```bash
git clone https://github.com/supermldev/heygenai.git
cd heygenai
pip install -r requirements.txt
```

Create a .env file:

OPENAI_API_KEY=your-openai-key
HEYGEN_API_KEY=your-heygen-key

## ▶️ Run the App
streamlit run app.py

## 📦 Folder Structure

heygenai/
├── rag_pipeline/
│   ├── retriever.py         # Vector DB + similarity search
│   ├── generator.py         # Script generation using LLM
│   └── heygen_video.py      # HeyGen API call
├── app.py                   # Streamlit or Gradio UI
├── examples/                # Sample docs and outputs
├── docs/                    # Architecture diagram, screenshots
├── requirements.txt
└── .env

## Success
If everything is fine than you should see:
![Success Message](docs/success.png)

Video generated:
<iframe width="560" height="315" src="https://app.heygen.com/embeds/22a189825fb04a1a8d72d9a92a2f1f64" title="HeyGen video player" frameborder="0" allow="encrypted-media; fullscreen;" allowfullscreen></iframe>



## 📹 Example Use Cases
	•	🎓 Educational Explainers
	•	🏢 Internal Corporate Training
	•	📢 Marketing Demos
	•	🧾 Document Summaries into Video

## 📄 License

MIT License — free to use and modify with credit.

##  ✨ Powered by SuperML.dev
---

Let me know if you’d like:
- A `flow_diagram.png`
- The starter Python code (`app.py`, `rag_pipeline/`)
- Video upload/share functionality

Ready to scaffold the codebase too?