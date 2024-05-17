"""
Este modulo verifica que la carpeta files, requerida por el ejecutable,
se encuentre con su formato valido
"""

import shutil
from os import path
from zipfile import ZipFile
from modules.paths import EXEC_FILES_DIR, COMPRESSED_FILES_ZIP


def update_files() -> None:
    """Actualiza el directorio Files"""
    if path.exists(EXEC_FILES_DIR):
        shutil.rmtree(EXEC_FILES_DIR)
    with ZipFile(COMPRESSED_FILES_ZIP, 'r') as zip_ref:
        zip_ref.extractall(path.dirname(EXEC_FILES_DIR))
