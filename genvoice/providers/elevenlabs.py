import requests
from genvoice.logger import log_info, log_error,log_debug
from genvoice.config import GENVOICE_CONFIG

ELEVENLABS_API_KEY = GENVOICE_CONFIG.ELEVENLABS_API_KEY
VOICE_ID = GENVOICE_CONFIG.ELEVENLABS_VOICE_ID
BASE_URL = GENVOICE_CONFIG.ELEVENLABS_API_URL

def generate_video(script_text: str) -> str:
    url = f"{BASE_URL}/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": script_text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    log_debug(f"📦 ElevenLabs Payload: {payload}")
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            output_path = "output/elevenlabs_audio.mp3"
            with open(output_path, "wb") as f:
                f.write(response.content)
            log_info(f"✅ Audio saved to {output_path}")
            return output_path
        else:
            log_error(f"❌ ElevenLabs generation failed: {response.text}")
            return None
    except Exception as e:
        log_error(f"❌ Exception during ElevenLabs API call: {e}")
        return None