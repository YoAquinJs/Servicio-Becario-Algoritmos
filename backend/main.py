"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Comand de ejecucion:
uvicorn main:app --reload
"""

from subprocess import CalledProcessError, TimeoutExpired, run
from fastapi import FastAPI, HTTPException
from config_files import ConfigFile

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

@app.get("/matrix/{matrix_index}")
async def output(matrix_type: str):
    """Retorna la matriz de credibilidad del indice especificado"""
    credibility_matrix = None #TODO encontrar la matriz correspondiente
    if credibility_matrix is None:
        error_msg = f"matriz de credibilidad '{matrix_type}' no encontrada"
        raise HTTPException(status_code=404,detail=error_msg)

    return credibility_matrix

@app.post("/execute")
async def execute() -> dict[str, str]:
    """Ejecuta el archivo .jar calculando las matrices de credibilidad"""
    command = "java -jar executable.jar 4"
    try:
        result = run(command, shell=True, capture_output=True, text=True, check=True)
        return {"response":result.stdout}
    except CalledProcessError as err:
        raise HTTPException(status_code=500, detail=err.output) from err
    except TimeoutExpired as err:
        error_msg = "timeout en la ejecucion del algoritmo"
        raise HTTPException(status_code=500, detail=error_msg) from err
