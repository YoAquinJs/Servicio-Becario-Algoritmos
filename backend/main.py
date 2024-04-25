"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Comand de ejecucion:
py -m uvicorn main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.algorithm import ExecAlgorithm
from modules.config_files import ConfigFile
from modules.output import load_algorithm_output
from modules.execute import run_executable

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

@app.get("/config/{algorithm}/{config_type}")
async def get_config(algorithm: str, config_type: str) -> dict[str, str]:
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    config = ConfigFile.get_type(config_type).load_file(ExecAlgorithm[algorithm])
    return {"config": config}

@app.post("/config/{algorithm}/{config_type}")
async def modify_config(algorithm: str, config_type: str, config_data: str):
    """Guarda la configuracion en su archivo correspondiente"""
    ConfigFile.get_type(config_type).save_file(ExecAlgorithm[algorithm], config_data)
    return {"response": f"Configuracion ({config_type}) guardada"}

@app.get("/output/{algorithm}/{output_type}")
async def get_output(algorithm: str, output_type: str) -> dict[str, str]:
    """Retorna la matriz de credibilidad del indice especificado"""
    output = load_algorithm_output(ExecAlgorithm[algorithm], output_type)
    return {"output": output}

@app.post("/execute/{algorithm}")
async def execute(algorithm: str) -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    result = run_executable(ExecAlgorithm[algorithm])
    return {"response": result}
