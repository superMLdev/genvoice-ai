import os
import tempfile
import requests
from genvoice.logger import log_info, log_error

try:
    import whisper
    model = whisper.load_model("base")
except ImportError:
    model = None
    log_error("Whisper not installed. Run `pip install -U openai-whisper` to enable transcription.")

def transcribe_audio(audio_url: str) -> str:
    """
    Downloads an audio file from a URL and transcribes it using Whisper.
    """
    if model is None:
        return "[Transcription unavailable: Whisper not installed.]"

    try:
        response = requests.get(audio_url)
        if response.status_code != 200:
            log_error(f"Failed to download audio: {audio_url}")
            return ""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_audio:
            tmp_audio.write(response.content)
            tmp_audio_path = tmp_audio.name

        result = model.transcribe(tmp_audio_path)
        os.remove(tmp_audio_path)
        return result["text"]

    except Exception as e:
        log_error(f"Error during transcription: {e}")
        return ""