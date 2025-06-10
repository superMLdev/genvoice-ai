import os
from dotenv import load_dotenv
from genvoice.core.document_loader import load_documents
from genvoice.core.vector_store import create_vector_store
from genvoice.core.script_generator import generate_script
from genvoice.providers.heygen import generate_video

load_dotenv()

def main():
    print("\n📁 Project structure and boilerplate for genvoice-ai initialized.")
    file_path = "examples/sample_script.txt"
    print(f"📄 Loading file: {file_path}")

    docs = load_documents(file_path)

    print("🧠 Generating script from documents...")
    script = generate_script(docs, "Summarize the content for a video explainer")
    print("\n🎬 Generated Script:\n", script)

    print("\n📽️ Sending script to HeyGen...")
    result = generate_video(script)

    if result.get("data", {}).get("video_id"):
        print("✅ Video submitted successfully. Video ID:", result["data"]["video_id"])
    else:
        print("❌ Video generation failed:", result)

if __name__ == "__main__":
    main()
