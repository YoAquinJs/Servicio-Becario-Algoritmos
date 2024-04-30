"""Modulo de las clases que especifican el formato de los archivos de configuracion"""

from __future__ import annotations

from abc import ABC, abstractmethod
from os import path
from fastapi import HTTPException
from modules.algorithm import ExecAlgorithm, EXECUTABLE_CONFIG_DIR

CONFIG_EXT = ".txt"
EXEC_FILES_DIR = "Files"
ENCODING = "utf-8"

DATA_SEPARATOR = "\t"

def _read_config_file(algorithm: ExecAlgorithm, config_type: str) -> str:
    file_path = path.join(EXEC_FILES_DIR, EXECUTABLE_CONFIG_DIR[algorithm], config_type)+CONFIG_EXT
    with open(file_path, "r", encoding=ENCODING) as file:
        return file.read()

def _write_config_file(algorithm: ExecAlgorithm, config_type: str, data: str) -> None:
    file_path = path.join(EXEC_FILES_DIR, EXECUTABLE_CONFIG_DIR[algorithm], config_type)+CONFIG_EXT
    with open(file_path, "w", encoding=ENCODING) as file:
        file.write(data.replace('\r\n', '\n'))

class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""
    #Overrides in each sub class
    config_type: str

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        """Retorna la informacion guardada del archivo de configuracion,
           Puede lanzar un HTTPException si hay algun fallo"""
        return _read_config_file(algorithm, cls.config_type)

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        """Guarda el archivo de configuracion con la informacion recibida,
           Puede lanzar un HTTPException si hay algun fallo, Http code 400
           si la informacion enviada no cumple con el formato requerido"""
        if not cls.is_valid_format(data):
            error_msg = f"Formato invalido para el archivo '{cls.config_type}'"
            raise HTTPException(status_code=500, detail=error_msg)
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    @abstractmethod
    def is_valid_format(cls, data: str) -> bool:
        """Valida si los datos enviados, son compatibles con el formato
        del archivo de configuaracion correspondiente"""

    @staticmethod
    def get_type(config_type: str) -> type[ConfigFile]:
        """Obtiene el tipo correspondiente """
        config: type[ConfigFile]
        match config_type:
            case AdditionalCriteriaParametersConfig.config_type:
                config = AdditionalCriteriaParametersConfig
            case CredibilityCriteriaConfig.config_type:
                config = CredibilityCriteriaConfig
            case CriteriaDirectionsConfig.config_type:
                config = CriteriaDirectionsConfig
            case CriteriaHierarchyConfig.config_type:
                config = CriteriaHierarchyConfig
            case CriteriaInteractionsConfig.config_type:
                config = CriteriaInteractionsConfig
            case CriteriaParametersConfig.config_type:
                config = CriteriaParametersConfig
            case PerformanceMatrixConfig.config_type:
                config = PerformanceMatrixConfig
            case UseValueFunctionConfig.config_type:
                config = UseValueFunctionConfig
            case VetoThresholdsForSupercriteriaConfig.config_type:
                config = VetoThresholdsForSupercriteriaConfig
            case WeightsConfig.config_type:
                config = WeightsConfig
            case _:
                error_msg = f"archivo de configuracion '{config_type} no encontrado"
                raise HTTPException(status_code=404, detail=error_msg)
        return config

class AdditionalCriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Additional criteria parameters"""
    config_type = "Additional criteria parameters"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class CredibilityCriteriaConfig(ConfigFile):
    """Clase para configuracion de Credibility criteria"""
    config_type = "Credibility criteria"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class CriteriaDirectionsConfig(ConfigFile):
    """Clase para configuracion de Criteria directions"""
    config_type = "Criteria directions"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class CriteriaHierarchyConfig(ConfigFile):
    """Clase para configuracion de Criteria hierarchy"""
    config_type = "Criteria hierarchy"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class CriteriaInteractionsConfig(ConfigFile):
    """Clase para configuracion de Criteria interactions"""
    config_type = "Criteria interactions"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class CriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Criteria parameters"""
    config_type = "Criteria parameters"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class PerformanceMatrixConfig(ConfigFile):
    """Clase para configuracion de Performance matrix"""
    config_type = "Performance matrix"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class UseValueFunctionConfig(ConfigFile):
    """Clase para configuracion de Use value function"""
    config_type = "Use value function"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class VetoThresholdsForSupercriteriaConfig(ConfigFile):
    """Clase para configuracion de Veto thresholds for supercriteria"""
    config_type = "Veto thresholds for supercriteria"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True

class WeightsConfig(ConfigFile):
    """Clase para configuracion de Weights"""
    config_type = "Weights"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True
