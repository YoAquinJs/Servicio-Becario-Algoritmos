"""Modulo para la funcionalidad de carga de matrices de credibilidad"""

from os import path
from fastapi import HTTPException
from modules.algorithm import ExecAlgorithm, EXECUTABLE_CONFIG_DIR, EXECUTABLE_OUTPUT_DIR

OUTPUT_EXT = ".txt"
EXEC_FILES_DIR = "Files"
ENCODING = "utf-8"

def load_algorithm_output(algorithm: ExecAlgorithm, output_type: str) -> str:
    """Carga el archivo resultante del algoritmo"""
    try:
        output_path = path.join(EXEC_FILES_DIR,
                                EXECUTABLE_CONFIG_DIR[algorithm],
                                EXECUTABLE_OUTPUT_DIR[algorithm],
                                output_type)+OUTPUT_EXT
        with open(output_path, "r", encoding=ENCODING) as file:
            return file.read()
    except FileNotFoundError as exc:
        error_msg = f"archivo de resultado '{output_type}' no encontrada"
        raise HTTPException(status_code=404, detail=error_msg) from exc
