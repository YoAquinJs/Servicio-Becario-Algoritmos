"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Comand de ejecucion:
uvicorn main:app --reload
"""

from fastapi import FastAPI, HTTPException
from modules.config_files import ConfigFile
from modules.credibility_matrix import load_credibility_matrix
from modules.execute import run_executable

app = FastAPI()

@app.get("/")
async def root():
    """Root de la api"""
    return {"response":"root"}

@app.get("/config/{config_type}")
async def get_config(config_type: str):
    """Retorna la informacion actual del archivo de configuracion solicitado"""
    config_file = ConfigFile.get_type(config_type)
    if config_file is None:
        error_msg = f"archivo de configuracion '{config_type} no encontrado"
        raise HTTPException(status_code=404, detail=error_msg)

    return config_file.load_file()

@app.post("/config/{config_type}")
async def modify_config(config_type: str, config_data: dict):
    """Guarda la configuracion en su archivo correspondiente"""
    config_file = ConfigFile.get_type(config_type)
    if config_file is None:
        error_msg = f"archivo de configuracion '{config_type} no encontrado"
        raise HTTPException(status_code=404, detail=error_msg)

    config_file.save_file(config_data)
    return {"response":"configuracion "}

@app.get("/matrix/{matrix_type}")
async def output(matrix_type: str):
    """Retorna la matriz de credibilidad del indice especificado"""
    return load_credibility_matrix(matrix_type)

@app.post("/execute")
async def execute() -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    return run_executable()
