import requests
import time
import os
from genvoice.logger import log_info, log_error

def print_payload(label, payload):
    print(f"\n📦 {label}: {payload}")

def print_response(label, response):
    print(f"\n📬 {label}: {response}")

def handle_api_error(response):
    if isinstance(response, dict) and response.get("error"):
        print(f"❌ API Error: {response['error']}")
        return True
    return False

def download_video(video_url, output_path="downloaded_video.mp4"):
    print(f"\n⬇️ Downloading video from: {video_url}")
    response = requests.get(video_url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Video saved to: {output_path}")
    else:
        print("❌ Failed to download video")

def poll_video_status(video_id, headers, max_retries=10, interval=6):
    print("⏳ Polling video status...")
    url = f"https://api.heygen.com/v1/video/{video_id}/status"
    for attempt in range(max_retries):
        res = requests.get(url, headers=headers)
        data = res.json()
        if data.get("status") == "completed":
            return data.get("download_url")
        time.sleep(interval)
    return None

### genvoice/speech_to_text.py
# Placeholder for adding speech-to-text functionality
# Can use Whisper, AssemblyAI, Deepgram, etc.

def transcribe_audio(file_path):
    print(f"🔊 Transcribing audio: {file_path}")
    # TODO: Add real transcription logic
    return "[Transcribed text will appear here]"

def read_text_from_file(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        from PyPDF2 import PdfReader
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    else:
        raise ValueError("Unsupported file type. Only .txt and .pdf supported.")

def save_binary_file(data: bytes, path: str):
    with open(path, "wb") as f:
        f.write(data)
    log_info(f"📥 Saved file: {path}")