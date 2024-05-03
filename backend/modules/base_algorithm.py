"""Este modulo contiene la clase base para la representacion de un algoritmo de ejecucion"""

from abc import ABC, abstractmethod


class ExecAlgorithm(ABC):
    """Clase base de los diferentes algoritmos de ejecucion"""

    exec_config_dir: str
    exec_output_dir: str
    exec_param: int

    @classmethod
    @abstractmethod
    def get_output(cls, output_type: str) -> str:
        """Obtiene los resultados del algoritmo correspondiente"""
