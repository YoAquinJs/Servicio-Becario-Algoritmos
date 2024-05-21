"""Modulo de la clase base de los archivos de configuracion"""

from __future__ import annotations

from abc import ABC, abstractmethod
from os import path

from fastapi import HTTPException

from modules.base_algorithm import ExecAlgorithm
from modules.paths import ENCODING, EXEC_FILES_DIR, TXT_EXT


class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""
    #Overrides in each sub class
    config_type: str

    @classmethod
    def _read_config_file(cls, algorithm: type[ExecAlgorithm]) -> str:
        file_path = path.join(EXEC_FILES_DIR, algorithm.exec_config_dir, cls.config_type+TXT_EXT)
        with open(file_path, "r", encoding=ENCODING) as file:
            return file.read()

    @classmethod
    def _write_config_file(cls, algorithm: type[ExecAlgorithm], data: str) -> None:
        file_path = path.join(EXEC_FILES_DIR, algorithm.exec_config_dir, cls.config_type+TXT_EXT)
        with open(file_path, "w", encoding=ENCODING) as file:
            file.write(data.replace('\r\n', '\n'))

    @classmethod
    def load_file(cls, algorithm: type[ExecAlgorithm]) -> str:
        """Retorna la informacion guardada del archivo de configuracion,
           Puede lanzar un HTTPException si hay algun fallo"""
        try:
            return cls._read_config_file(algorithm)
        except FileNotFoundError as exc:
            error_msg = f"Algoritmo no posee el archivo de configuracion '{cls.config_type}'"
            raise HTTPException(status_code=404, detail=error_msg) from exc

    @classmethod
    def save_file(cls, algorithm: type[ExecAlgorithm], data: str) -> None:
        """Guarda el archivo de configuracion con la informacion recibida,
           Puede lanzar un HTTPException si hay algun fallo, Http code 404
           si la informacion enviada no cumple con el formato requerido"""
        if not cls.is_valid_format(data):
            error_msg = f"Formato invalido para el archivo '{cls.config_type}'"
            raise HTTPException(status_code=404, detail=error_msg)

        try:
            cls._write_config_file(algorithm, data)
        except FileNotFoundError as exc:
            error_msg = f"Algoritmo no posee el archivo de configuracion '{cls.config_type}'"
            raise HTTPException(status_code=404, detail=error_msg) from exc

    @classmethod
    @abstractmethod
    def is_valid_format(cls, data: str) -> bool:
        """Valida si los datos enviados, son compatibles con el formato
        del archivo de configuaracion correspondiente"""
