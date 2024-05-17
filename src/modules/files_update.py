"""
Este modulo verifica que la carpeta files, requerida por el ejecutable,
se encuentre con su formato valido
"""

import os
from os import path
from zipfile import ZipFile
from modules.paths import EXEC_FILES_DIR

def update_files(expected_files_path: str, compressed_files_path: str) -> None:
    """Actualiza el directorio Files"""
    if path.exists(expected_files_path):
        os.rmdir(expected_files_path)
    with ZipFile(compressed_files_path, 'r') as zip_ref:
        zip_ref.extractall(expected_files_path)
