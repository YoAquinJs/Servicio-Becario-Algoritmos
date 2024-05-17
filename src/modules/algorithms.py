"""Modulo para la funcionalidad de carga de matrices de credibilidad"""

from os import path, listdir
from typing import Callable
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
EXEC_FILES_DIR = "Files"

class CredibilityMatrixAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Matrices de Credibilidad"""
    exec_config_dir = "Calculate credibility matrix"
    exec_output_dir = "Credibility matrices"
    exec_param = 4

    @classmethod
    def get_outputs(cls) -> list[str]:
        """Obtiene los nombres de los tipos de resultados"""
        outputs_dir = path.join(EXEC_FILES_DIR, cls.exec_config_dir, cls.exec_output_dir)
        return [f.split("-")[0] for f in listdir(outputs_dir)]

    @classmethod
    def _get_output_path(cls, output_type: str) -> str:
        return output_type+f"-CredibilityMatrix{OUTPUT_EXT}"

class SortingAlgorithm(ExecAlgorithm):
    """Representa el algoritmo de ejecucion Calculo de Sorteo"""
    exec_config_dir = "Calculate sorting"
    exec_output_dir = "Sorting"
    exec_param = 5

    @classmethod
    def get_outputs(cls) -> list[str]:
        """Obtiene los nombres de los tipos de resultados"""
        outputs_dir = path.join(EXEC_FILES_DIR, cls.exec_config_dir, cls.exec_output_dir)
        exists_out: Callable[[str], bool] = \
            lambda dir: path.exists(path.join(outputs_dir, dir, f"Assignments{OUTPUT_EXT}"))
        return [dir for dir in listdir(outputs_dir) if exists_out(dir)]

    @classmethod
    def _get_output_path(cls, output_type: str) -> str:
        return path.join(output_type, f"Assignments{OUTPUT_EXT}")
