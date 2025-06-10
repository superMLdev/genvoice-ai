import requests
from genvoice.logger import log_error,log_debug
from genvoice.config import GENVOICE_CONFIG

HEYGEN_API_KEY = GENVOICE_CONFIG.HEYGEN_API_KEY
HEYGEN_API_URL = GENVOICE_CONFIG.HEYGEN_API_URL
AVATAR_ID = GENVOICE_CONFIG.HEYGEN_AVATAR_ID
VOICE_ID = GENVOICE_CONFIG.HEYGEN_VOICE_ID


def generate_video(script_text: str) -> str:
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": AVATAR_ID,
                    "avatar_style": "normal"
                },
                "voice": {
                    "type": "text",
                    "input_text": script_text,
                    "voice_id": VOICE_ID,
                    "speed": 1.0
                },
                "background": {
                    "type": "color",
                    "value": "#FFFFFF"
                }
            }
        ],
        "dimension": {"width": 1280, "height": 720},
        "title": f"Generated Video - {AVATAR_ID}"
    }

    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    log_debug(f"📦 HeyGen Payload: {payload}")
    response = requests.post(HEYGEN_API_URL, headers=headers, json=payload)

    try:
        res_json = response.json()
        log_debug(f"📬 HeyGen API Response: {res_json}")
        video_id = res_json.get("data", {}).get("video_id")
        if video_id:
            log_error(f"✅ Video submitted successfully. Video ID: {video_id}")
            return video_id
        else:
            log_error(f"❌ Video generation failed: {res_json}")
            return None
    except Exception as e:
        log_error(f"❌ Error parsing HeyGen response: {e}")
        return None