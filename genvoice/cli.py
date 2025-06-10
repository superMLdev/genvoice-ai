import argparse
from genvoice.provider_registry import ProviderRegistry
from genvoice.utils import read_text_from_file
from genvoice.logger import log_info, log_error

def main():
    parser = argparse.ArgumentParser(description="GenVoice AI Video/Audio Generator")
    parser.add_argument("input_file", help="Path to the text or PDF file")
    parser.add_argument("--provider", choices=["heygen", "elevenlabs"], default=None, help="Provider to use (default from config)")
    parser.add_argument("--transcribe", action="store_true", help="Enable speech-to-text transcription")
    parser.add_argument("--output", help="Output file or directory path (optional)")

    args = parser.parse_args()

    try:
        provider = ProviderRegistry.get(args.provider)
        text = read_text_from_file(args.input_file)
        log_info(f"📤 Input loaded. Length: {len(text)} characters")

        video_or_audio = provider.generate(text)

        log_info(f"✅ Generation complete: {video_or_audio}")

        if args.transcribe:
            from genvoice.speech_to_text import transcribe_audio
            transcript = transcribe_audio(video_or_audio)
            log_info(f"📝 Transcript:\n{transcript}")

    except Exception as e:
        log_error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()