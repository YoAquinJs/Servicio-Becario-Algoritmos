"""Modulo para la funcionalidad de carga de matrices de credibilidad"""

from os import path
from fastapi import HTTPException
from backend.modules.base_algorithm import ExecAlgorithm

OUTPUT_EXT = ".txt"
EXEC_FILES_DIR = "Files"
ENCODING = "utf-8"


def get_algorithm(algorithm: str) -> type[ExecAlgorithm]:
    """Obtiene el algoritmo a partir de su nombre"""
    parsed_algorithm: type[ExecAlgorithm]
    match algorithm:
        case CredibilityMatrixAlgorithm.exec_config_dir:
            parsed_algorithm = CredibilityMatrixAlgorithm
        case SortingAlgorithm.exec_config_dir:
            parsed_algorithm = SortingAlgorithm
        case _:
            error_msg = f"Algoritmo '{algorithm}' no encontrado"
            raise HTTPException(status_code=404, detail=error_msg)
    return parsed_algorithm

class CredibilityMatrixAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Matrices de Credibilidad"""
    exec_config_dir = "Calculate credibility matrix"
    exec_output_dir = "Credibility matrices"
    exec_param = 4

    @classmethod
    def get_output(cls, output_type: str) -> str:
        try:
            output_path = path.join(EXEC_FILES_DIR,
                                    cls.exec_config_dir,
                                    cls.exec_output_dir,
                                    output_type)+f"-CredibilityMatrix{OUTPUT_EXT}"
            with open(output_path, "r", encoding=ENCODING) as file:
                return file.read()
        except FileNotFoundError as exc:
            error_msg = f"matriz de credibilidad '{output_type}' no encontrada"
            raise HTTPException(status_code=404, detail=error_msg) from exc

class SortingAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Calculo de Sorteo"""
    exec_config_dir = "Calculate sorting"
    exec_output_dir = "Sorting"
    exec_param = 5

    @classmethod
    def get_output(cls, output_type: str) -> str:
        return ""
