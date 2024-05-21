"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Juan Sebastian Gonzalez A01644942

Comando de ejecucion:
uvicorn main:app
"""

import logging
from typing import Any, Awaitable, Callable

from fastapi import FastAPI
from fastapi import HTTPException as StarletteHTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from modules.algorithms import get_algorithm
from modules.config_files import get_config_type
from modules.execute import run_executable
from modules.user_auth import delete_user, get_user_id, is_user, register_user
from modules.user_storage import assert_user_storage

# Logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("errors.log"),
    ]
)

# API

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    """TODO"""
    if exc.status_code == 500:
        logging.error(exc.detail)
    return JSONResponse(
            content=exc.detail,
            status_code=exc.status_code,
            headers=exc.headers,
        )

@app.middleware("http")
async def exception_middleware(request: Request, call_next: Callable[[Request], Awaitable[Any]]):
    """TODO"""
    try:
        return await call_next(request)
    except Exception as e: # pylint: disable=broad-except
        logging.error(str(e))
        return JSONResponse(content=str(e), status_code=500)

@app.get("/")
async def root():
    """Root de la api"""
    return {"response":"root"}

# User auth

assert_user_storage()

@app.get("/user/{user}")
async def exists_user(user: str):
    """Registra un nuevo usuario"""
    exists = is_user(user)
    return {"response":f"Usuario '{user}' {'existe' if exists else 'no existe'}"}

@app.post("/user/{user}")
async def reg_user(user: str):
    """Registra un nuevo usuario"""
    register_user(user)
    return {"response":f"Usuario '{user}' registrado"}

@app.delete("/user/{user}")
async def del_user(user: str):
    """Registra un nuevo usuario"""
    delete_user(user)
    return {"response":f"Usuario '{user}' eliminado"}

# Algortithm

@app.get("/config/{algorithm}/{user}/{config_type}")
async def get_config(algorithm: str, user: str, config_type: str) -> dict[str, str]:
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    config = get_config_type(config_type).load_file(get_algorithm(algorithm), get_user_id(user))
    return {"config": config}

@app.post("/config/{algorithm}/{user}/{config_type}")
async def modify_config(algorithm: str, user: str, config_type: str, config_data: str):
    """Guarda la configuracion en su archivo correspondiente"""
    get_config_type(config_type).save_file(get_algorithm(algorithm), get_user_id(user), config_data)
    return {"response": f"Configuracion ({config_type}) guardada"}

@app.get("/outputs/{algorithm}/{user}")
async def get_outputs(algorithm: str, user: str) -> dict[str, list[str]]:
    """Obtiene los nombres de resultados de los algoritmos"""
    outputs = get_algorithm(algorithm).get_outputs(get_user_id(user))
    return {"outputs": outputs}

@app.get("/output/{algorithm}/{user}/{output_type}")
async def get_output(algorithm: str, user: str, output_type: str) -> dict[str, str]:
    """Retorna la matriz de credibilidad del indice especificado"""
    output = get_algorithm(algorithm).get_output(get_user_id(user), output_type)
    return {"output": output}

@app.post("/execute/{algorithm}/{user}")
async def execute(algorithm: str, user: str) -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    result = run_executable(get_algorithm(algorithm), get_user_id(user))
    return {"response": result}
