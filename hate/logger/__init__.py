from datetime import datetime
import os
import logging
import sys
from from_root import from_root

PROJECT_NAME = "hate speech detection"
LOG_FILE = f"{datetime.now().strftime("%Y-%m-%d-%H-%M")}.log"
LOG_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging_str =  "%(asctime)s - %(levelname)s - %(module)s.py - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(sys.stdout)
    ])
# logger = logging.getLogger(PROJECT_NAME)
