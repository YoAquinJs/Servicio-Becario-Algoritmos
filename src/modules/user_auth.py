"""Este modulo contiene el manejo de registro y autenticacion de usuarios"""

import json
import uuid
from typing import Any

from fastapi import HTTPException

from modules.paths import ENCODING, USER_RECORD

UserRecord = dict[str, uuid.UUID]
UserRecordJson = dict[str, UserRecord]

class UserRecordEnc(json.JSONEncoder):
    """TODO"""
    def default(self, o: Any) -> Any:
        """TODO"""
        if isinstance(o, uuid.UUID):
            return str(o)
        return super().default(o)

def user_record_dec(o: dict[str, Any]) -> Any:
    """TODO"""
    if '__uuid__' in o:
        return uuid.UUID(o['__uuid__'])
    return o

def _get_user_record() -> UserRecord:
    with open(USER_RECORD, "r", encoding=ENCODING) as file:
        return json.loads(file.read(), object_hook=user_record_dec)["users"]

def is_user(user: str) -> bool:
    """TODO
    """
    return user in _get_user_record().keys()

def register_user(user: str) -> None:
    """TODO
    """
    user_record = _get_user_record()
    with open(USER_RECORD, "w", encoding=ENCODING) as file:
        if user in user_record:
            raise HTTPException(400, detail="Usuario ya existe")

        uid = uuid.uuid4()
        while uid in user_record.keys():
            uid = uuid.uuid4()
        user_record[user] = uid

        file.write(json.dumps({"users" : user_record}, cls=UserRecordEnc))

def delete_user(user: str) -> None:
    """TODO
    """
    user_record = _get_user_record()
    with open(USER_RECORD, "w", encoding=ENCODING) as file:
        if not user in user_record:
            raise HTTPException(400, detail="Usuario no existe")

        del user_record[user]
        file.write(json.dumps({"users" : user_record}, cls=UserRecordEnc))
