import os
from dotenv import load_dotenv

load_dotenv()

GENVOICE_CONFIG = {
    "OPENAI_API_KEY": os.getenv("GENVOICE_OPENAI_API_KEY"),
    "HEYGEN_API_KEY": os.getenv("GENVOICE_HEYGEN_API_KEY"),
    "ELEVENLABS_API_KEY": os.getenv("GENVOICE_ELEVENLABS_API_KEY"),
    "DEFAULT_PROVIDER": os.getenv("GENVOICE_DEFAULT_PROVIDER", "heygen"),
    "GENVOICE_LOG_FILE": os.getenv("GENVOICE_LOG_FILE", "genvoice.log"),
    "GENVOICE_LOG_LEVEL": os.getenv("GENVOICE_LOG_LEVEL", "INFO"),
    "HEYGEN_API_URL": os.getenv("GENVOICE_HEYGEN_API_URL"),
    "ELEVENLABS_API_URL": os.getenv("ELEVENLABS_API_URL"),
}