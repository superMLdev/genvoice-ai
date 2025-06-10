import os
import logging
from datetime import datetime

LOG_TO_FILE = os.getenv("GENVOICE_LOG_TO_FILE", "true").lower() == "true"
LOG_FILE = os.getenv("GENVOICE_LOG_FILE", "genvoice.log")

def setup_logger():
    logger = logging.getLogger("genvoice")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="\033[94m[%(asctime)s]\033[0m %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    if LOG_TO_FILE:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()

def log_info(msg): logger.info(msg)
def log_error(msg): logger.error(msg)
def log_debug(msg): logger.debug(msg)
