"""
Backend para el prototipo web del proyecto de servicio
becario: Toma de Desciciones con Algoritmos Geneticos

Comando de ejecucion:
uvicorn main:app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.algorithms import get_algorithm
from modules.config_files import get_config_type
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
