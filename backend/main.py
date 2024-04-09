"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Comand de ejecucion:
uvicorn main:app --reload
"""

from fastapi import FastAPI
from modules.config_files import ConfigFile
from modules.credibility_matrix import load_credibility_matrix
from modules.execute import run_executable

app = FastAPI()

@app.get("/")
async def root():
    """Root de la api"""
    return {"response":"root"}

@app.get("/config/{config_type}")
async def get_config(config_type: str) -> dict[str, str]:
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    return {"config": ConfigFile.get_type(config_type).load_file()}

@app.post("/config/{config_type}")
async def modify_config(config_type: str, config_data: str):
    """Guarda la configuracion en su archivo correspondiente"""
    ConfigFile.get_type(config_type).save_file(config_data)
    return {"response":f"Configuracion ({config_type}) guardada"}

@app.get("/matrix/{matrix_type}")
async def output(matrix_type: str) -> dict[str, list[list[float]]]:
    """Retorna la matriz de credibilidad del indice especificado"""
    return {"matrix": load_credibility_matrix(matrix_type)}

@app.post("/execute")
async def execute() -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    return {"response":run_executable()}
