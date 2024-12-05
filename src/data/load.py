import os
from kaggle.api.kaggle_api_extended import KaggleApi

download_path = os.path.expanduser("../../data/external")

# Crear el directorio si no existe
os.makedirs(download_path, exist_ok=True)

api = KaggleApi()
api.authenticate()

# Descargar el dataset
api.dataset_download_files("lainguyn123/student-performance-factors", path=download_path, unzip=True)

print("Path to dataset files:", download_path)