import os
from pathlib import Path
import sys
from hate.logger import logging
from hate.exception import CustomErrorMsg
from hate.configuration.gcloud_sync import GCloudSync
from from_root import from_root
# logging.info('logger test')

# try:
#     a = 7/0
# except Exception as e:
#     raise CustomErrorMsg(e, sys) from e

GCloudSync().Sync_folder2cloud('gs://hate-speech-data-ray',os.path.join(from_root(),'data'),'HateSpeech.zip')

