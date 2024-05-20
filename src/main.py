"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Juan Sebastian Gonzalez A01644942

Comando de ejecucion:
uvicorn main:app
"""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.algorithms import get_algorithm
from modules.config_files import get_config_type
from modules.execute import run_executable
from modules.user_auth import delete_user, is_user, register_user
from modules.user_storage import assert_user_storage

# Logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# API

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

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

# Allgortithm

@app.get("/config/{algorithm}/{config_type}")
async def get_config(algorithm: str, config_type: str) -> dict[str, str]:
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    config = get_config_type(config_type).load_file(get_algorithm(algorithm))
    return {"config": config}

@app.post("/config/{algorithm}/{config_type}")
async def modify_config(algorithm: str, config_type: str, config_data: str):
    """Guarda la configuracion en su archivo correspondiente"""
    get_config_type(config_type).save_file(get_algorithm(algorithm), config_data)
    return {"response": f"Configuracion ({config_type}) guardada"}

@app.get("/outputs/{algorithm}")
async def get_outputs(algorithm: str) -> dict[str, list[str]]:
    """Obtiene los nombres de resultados de los algoritmos"""
    outputs = get_algorithm(algorithm).get_outputs()
    return {"outputs": outputs}

@app.get("/output/{algorithm}/{output_type}")
async def get_output(algorithm: str, output_type: str) -> dict[str, str]:
    """Retorna la matriz de credibilidad del indice especificado"""
    output = get_algorithm(algorithm).get_output(output_type)
    return {"output": output}

@app.post("/execute/{algorithm}")
async def execute(algorithm: str) -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    result = run_executable(get_algorithm(algorithm))
    return {"response": result}
