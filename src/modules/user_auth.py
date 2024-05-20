"""Este modulo contiene el manejo de registro y autenticacion de usuarios"""

import json
from fastapi import HTTPException
from modules.paths import USER_REGISTRY, ENCODING

def _get_users() -> list[str]:
    with open(USER_REGISTRY, "r", encoding=ENCODING) as file:
        return json.loads(file.read())["users"]

def is_user(user: str) -> bool:
    """TODO
    """
    return user in _get_users()

def register_user(user: str) -> None:
    """TODO
    """
    users = _get_users()
    with open(USER_REGISTRY, "w", encoding=ENCODING) as file:
        if user in users:
            raise HTTPException(400, detail="Usuario ya existe")

        users.append(user)
        file.write(json.dumps({"users" : users}))

def delete_user(user: str) -> None:
    """TODO
    """
    users = _get_users()
    with open(USER_REGISTRY, "w", encoding=ENCODING) as file:
        if not user in users:
            raise HTTPException(400, detail="Usuario no existe")

        users.remove(user)
        file.write(json.dumps({"users" : users}))
