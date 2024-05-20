"""Este modulo contiene la constante EXEC_FILES_DIR"""

from os import path
from uuid import UUID

COMPRESSED_FILES_ZIP = path.join(path.curdir, "Files.zip")
EXEC_FILES_DIR = path.join(path.curdir, "Files")
ENCODING = "utf-8"
TXT_EXT = ".txt"
USER_RECORD = "users.json"
USER_STORAGE = "user_storage"

def get_user_path(user_id: UUID) -> str:
    """Retorna el path al directorio del usuario"""
    return path.join(USER_STORAGE, str(user_id))
