"""Este modulo contiene la clase base para la representacion de un algoritmo de ejecucion"""

from abc import ABC, abstractmethod
from os import path
from fastapi import HTTPException
from modules.paths import EXEC_FILES_DIR, ENCODING


class ExecAlgorithm(ABC):
    """Clase base de los diferentes algoritmos de ejecucion"""

    exec_config_dir: str
    exec_output_dir: str
    exec_param: int

    @classmethod
    def get_output(cls, output_type: str) -> str:
        """Obtiene los resultados del algoritmo correspondiente"""
        try:
            output_path = path.join(EXEC_FILES_DIR,
                                    cls.exec_config_dir,
                                    cls.exec_output_dir,
                                    cls._get_output_path(output_type))
            with open(output_path, "r", encoding=ENCODING) as file:
                return file.read()
        except FileNotFoundError as exc:
            error_msg = f"resultados del algoritmo '{cls.exec_config_dir}'\
                          '{output_type}' no encontrado"
            raise HTTPException(status_code=404, detail=error_msg) from exc

    @classmethod
    @abstractmethod
    def get_outputs(cls) -> list[str]:
        """Obtiene los nombres de los tipos de resultados"""

    @classmethod
    @abstractmethod
    def _get_output_path(cls, output_type: str) -> str:
        """Obtiene la direccion del archivo de resultados"""
