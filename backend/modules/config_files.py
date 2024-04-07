"""Modulo de las clases que especifican el formato de los archivos de configuracion"""

from __future__ import annotations
from typing import Optional

from abc import ABC, abstractmethod
from fastapi import HTTPException

class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""
    FILE_EXTENSION = '.txt'

    @classmethod
    @abstractmethod
    def save_file(cls, data: dict) -> None:
        """Guarda el archivo de configuracion con la informacion recibida,
           Puede lanzar un HTTPException si hay algun fallo"""

    @classmethod
    @abstractmethod
    def load_file(cls) -> dict:
        """Retorna la informacion guardada del archivo de configuracion,
           Puede lanzar un HTTPException si hay algun fallo"""

    @staticmethod
    def get_type(config_type: str) -> Optional[type[ConfigFile]]:
        """Obtiene el tipo correspondiente """
        match config_type:#TODO poner los tipos de archivos de configuracion
            case "":
                return ConfigFile
            case _:
                return None

#TODO crear todos los tipos de archivos de configuracion en su clase correspondiente

#TODO performance matrix

#TODO weigths
