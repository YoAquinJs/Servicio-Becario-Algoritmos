"""Este modulo contiene el manejo de registro y autenticacion de usuarios"""

import json
from fastapi import HTTPException
from modules.paths import USER_REGISTRY, ENCODING

def register_user(user: str) -> None:
    """TODO
    """
    with open(USER_REGISTRY, "r+", encoding=ENCODING) as file:
        users: list[str] = json.loads(file.read())["users"]
        if user in users:
            raise HTTPException(400, detail="Usuario ya existe")

        users.append(user)
        file.write(json.dumps({"users" : users}))

def delete_user(user: str) -> None:
    """TODO
    """
    with open(USER_REGISTRY, "r+", encoding=ENCODING) as file:
        users: list[str] = json.loads(file.read())["users"]
        if not user in users:
            raise HTTPException(400, detail="Usuario no existe")

        users.append(user)
        file.write(json.dumps({"users" : users}))
