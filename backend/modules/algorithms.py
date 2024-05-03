"""Modulo para la funcionalidad de carga de matrices de credibilidad"""

from os import path
from fastapi import HTTPException
from modules.base_algorithm import ExecAlgorithm


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

OUTPUT_EXT = ".txt"

class CredibilityMatrixAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Matrices de Credibilidad"""
    exec_config_dir = "Calculate credibility matrix"
    exec_output_dir = "Credibility matrices"
    exec_param = 4

    @classmethod
    def _get_output_path(cls, output_type: str) -> str:
        return output_type+f"-CredibilityMatrix{OUTPUT_EXT}"

class SortingAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Calculo de Sorteo"""
    exec_config_dir = "Calculate sorting"
    exec_output_dir = "Sorting"
    exec_param = 5

    @classmethod
    def _get_output_path(cls, output_type: str) -> str:
        return path.join(output_type, f"Assignments{OUTPUT_EXT}")
