"""
Module to call HeyGen API for video generation.
"""
import requests
import os
from dotenv import load_dotenv
load_dotenv()

HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")

def generate_video(script_text):
    url = "https://api.heygen.com/v2/video/generate"
    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": "Angela-inTshirt-20220820",
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": script_text,
                    "voice_id": "1bd001e7e50f421d891986aad5158bc8",
                    "speed": 1.0
                },
                "background": {
                    "type": "color",
                    "value": "#FFFFFF"
                }
            }
        ],
        "dimension": {
            "width": 1280,
            "height": 720
        },
        "title": "Safe Test Video"
    }

    print("📦 Payload:", payload)
    res = requests.post(url, headers=headers, json=payload)

    try:
        response_json = res.json()
        print("📬 API Response:", response_json)

        video_id = response_json.get("data", {}).get("video_id")
        if res.status_code == 200 and video_id:
            print(f"✅ Video submitted successfully. Video ID: {video_id}")
            return video_id
        else:
            print("⚠️ API responded but no video ID was found.")
            return None
    except Exception as e:
        print("❌ Failed to parse response:", e)
        print("Raw Response:", res.text)
        return None