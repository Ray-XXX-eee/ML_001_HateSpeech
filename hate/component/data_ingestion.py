from pathlib import Path
import pandas as pd

class DataIngestion:
    def __init__(self, data_path: Path):
        self.data_path = data_path

    def download_data(self):
        # :Should be moved to utility. already have downloaded data. If making for user need uploaded data option.  
        pass
    def read_data(self):
        return pd.read_csv(self.data_path)
    