import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "hate"

file_list = [
    f"{project_name}/component/__init__.py",
    f"{project_name}/component/data_ingestion.py",
    f"{project_name}/component/data_transformation.py",
    f"{project_name}/component/model_trainer.py",
    f"{project_name}/component/model_evaluation.py",
    f"{project_name}/component/model_pusher.py",
    f"{project_name}/configuration/gcloud_sync.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/entity_config.py",
    f"{project_name}/entity/artifact_config.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py"
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ML/__init__.py",
    f"{project_name}/ML/model.py"
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py"
]

for file_path in file_list:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file {file_name}")
        
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as file:
            logging.info(f"Created file: {file_name}")
    else:
        logging.info(f"File already exists: {file_name}")
        
logging.info("Project structure created successfully!")