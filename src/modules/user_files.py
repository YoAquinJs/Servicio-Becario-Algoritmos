"""
Este modulo verifica que la carpeta files, requerida por el ejecutable,
se encuentre con su formato valido, por cada usuario
"""

import json
import os
import shutil
import uuid
from os import path
from zipfile import ZipFile

from modules.paths import (COMPRESSED_FILES_ZIP, ENCODING, EXEC_FILES_DIR,
                           USER_RECORD, USER_STORAGE)


def assert_user_storage() -> None:
    """TODO
    """
    if not path.exists(USER_RECORD):
        with open(USER_RECORD, "w", encoding=ENCODING) as file:
            user_json = json.dumps({
                "users":{}
            })
            file.write(user_json)

    if not path.exists(USER_STORAGE):
        os.mkdir(USER_STORAGE)


def reset_user_files(user: str) -> None:
    """Actualiza el directorio Files del usuario especificado"""
    # user_id: str = uuid.uuid4().
    # print(user_id)
    # if path.exists(path.join()):
    #     shutil.rmtree(EXEC_FILES_DIR)
    # with ZipFile(COMPRESSED_FILES_ZIP, 'r') as zip_ref:
    #     zip_ref.extractall(path.dirname(EXEC_FILES_DIR))
