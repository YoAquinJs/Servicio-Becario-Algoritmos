"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Juan Sebastian Gonzalez A01644942

Comando de ejecucion:
uvicorn main:app
"""

import logging
from typing import Any, Awaitable, Callable
from uuid import UUID

from fastapi import Depends, FastAPI
from fastapi import HTTPException as StarletteHTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from modules.algorithms import get_algorithm
from modules.base_algorithm import ExecAlgorithm
from modules.config_files import get_config_type
from modules.execute import run_executable
from modules.user_auth import delete_user, get_user_id, is_user, register_user
from modules.user_storage import assert_user_storage, reset_user_storage

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

# User

assert_user_storage()

@app.get("/user/{user}")
async def exists_user(user: str) -> dict[str, bool]:
    """Registra un nuevo usuario"""
    exists = is_user(user)
    return {"exists":exists}

@app.post("/user/{user}")
async def reg_user(user: str) -> dict[str, str]:
    """Registra un nuevo usuario"""
    register_user(user)
    return {"response":f"Usuario '{user}' registrado"}

@app.delete("/user/{user}")
async def del_user(user: str) -> dict[str, str]:
    """Elimina un usuario"""
    delete_user(user)
    return {"response":f"Usuario '{user}' eliminado"}

@app.post("/reset_user/{user}")
async def reset_user(user: str) -> dict[str, str]:
    """Resetea los archivos de un usuario"""
    reset_user_storage(get_user_id(user))
    return {"response":f"Usuario '{user}' reseteado"}

# Algortithm

@app.get("/config/{user}/{algorithm}/{config_type}")
async def get_config(config_type: str,
                     user: UUID = Depends(get_user_id),
                     algorithm: type[ExecAlgorithm] = Depends(get_algorithm)
                     ) -> dict[str, str]:
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    config = get_config_type(config_type).load_file(algorithm, user)
    return {"config": config}

@app.post("/config/{user}/{algorithm}/{config_type}")
async def modify_config(config_type: str, config_data: str,
                        user: UUID = Depends(get_user_id),
                        algorithm: type[ExecAlgorithm] = Depends(get_algorithm)
                        ) -> dict[str, str]:
    """Guarda la configuracion en su archivo correspondiente"""
    get_config_type(config_type).save_file(algorithm, user, config_data)
    return {"response": f"Configuracion ({config_type}) guardada"}

@app.get("/outputs/{user}/{algorithm}")
async def get_outputs(user: UUID = Depends(get_user_id),
                      algorithm: type[ExecAlgorithm] = Depends(get_algorithm)
                      ) -> dict[str, list[str]]:
    """Obtiene los nombres de resultados de los algoritmos"""
    outputs = algorithm.get_outputs(user)
    return {"outputs": outputs}

@app.get("/output/{user}/{algorithm}/{output_type}")
async def get_output(output_type: str,
                     user: UUID = Depends(get_user_id),
                     algorithm: type[ExecAlgorithm] = Depends(get_algorithm)
                     ) -> dict[str, str]:
    """Retorna la matriz de credibilidad del indice especificado"""
    output = algorithm.get_output(user, output_type)
    return {"output": output}

@app.post("/execute/{user}/{algorithm}")
async def execute(user: UUID = Depends(get_user_id),
                  algorithm: type[ExecAlgorithm] = Depends(get_algorithm)
                  ) -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    result = run_executable(algorithm, user)
    return {"response": result}
