# app.py
"""
CLI version of HeyGenAI: Load file, run RAG, generate video script, call HeyGen API.
"""
import os
import time
import requests
from dotenv import load_dotenv
from rag_pipeline.retriever import load_documents, create_vector_store
from rag_pipeline.generator import generate_script
from rag_pipeline.heygen_video import generate_video

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")


def check_video_status(video_id, headers):
    url = f"https://api.heygen.com/v2/video/{video_id}/status"
    print("Checking video status...")
    for _ in range(10):
        res = requests.get(url, headers=headers)
        data = res.json()
        if data.get("status") == "completed":
            return data.get("download_url")
        print("...still processing...")
        time.sleep(6)
    return None


def main():
    file_path = "examples/sample_script.txt"
    print(f"📄 Loading file: {file_path}")
    docs = load_documents(file_path)
    db = create_vector_store(docs)

    query = "Summarize this for a video explainer"
    print("🧠 Generating script from documents...")
    script = generate_script(docs, query)
    print("\n🎬 Generated Script:\n")
    print(script)

    print("\n📽️ Sending script to HeyGen...")
    videoId = generate_video(script)

    if videoId:
        print("✅ Video generation started. Video ID:", videoId)
        headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
        download_url = check_video_status(videoId, headers)
        if download_url:
            print("\n🎉 Video is ready!")
        else:
            print("⚠️ Video still processing. Check your HeyGen dashboard later.")
    else:
        print("❌ Video generation failed:", videoId)


if __name__ == "__main__":
    main()
