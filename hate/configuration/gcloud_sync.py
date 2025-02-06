import os
from pathlib import Path

class GCloudSync:
        
    def Sync_folder2cloud(self, gcp_bucket_url:str, file_path: Path, file_name:str):
        command = f"gsutil cp {file_path}/{file_name} gs://{gcp_bucket_url}" #copy a to b
        os.system(command)
        
    def sync_cloud2folder(self, gcp_bucket_url, file_path,file_name):
        command = f"gsutil cp gs://{gcp_bucket_url} {file_path}/{file_name}"
        os.system(command)
        