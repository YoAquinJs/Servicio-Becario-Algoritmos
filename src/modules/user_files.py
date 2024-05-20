"""
Este modulo verifica que la carpeta files, requerida por el ejecutable,
se encuentre con su formato valido, por cada usuario
"""

import json
import shutil
from os import path
from zipfile import ZipFile
from modules.paths import USER_REGISTRY, EXEC_FILES_DIR, COMPRESSED_FILES_ZIP, ENCODING


def assert_user_storage() -> None:
    if path.exists(USER_REGISTRY):
        return

    with open(USER_REGISTRY, "w", encoding=ENCODING) as file:
        user_json = {
            "users":[]
        }
        file.write(json.dumps(user_json))

def update_files(user: str) -> None:
    """Actualiza el directorio Files"""
    if path.exists(EXEC_FILES_DIR):
        shutil.rmtree(EXEC_FILES_DIR)
    with ZipFile(COMPRESSED_FILES_ZIP, 'r') as zip_ref:
        zip_ref.extractall(path.dirname(EXEC_FILES_DIR))
