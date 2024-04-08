"""Modulo de las clases que especifican el formato de los archivos de configuracion"""

from __future__ import annotations

from abc import ABC, abstractmethod
from os import path
from fastapi import HTTPException

CONFIG_DIRECTORY = path.join("Files", "Calculate credibility matrix")
ENCODING = "utf-8"

def _read_config_file(config_type: str) -> str:
    with open(path.join(CONFIG_DIRECTORY, config_type), "r", encoding=ENCODING) as file:
        return file.read()

def _write_config_file(config_type: str, data: str) -> None:
    with open(path.join(CONFIG_DIRECTORY, config_type), "w", encoding=ENCODING) as file:
        file.write(data)

class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""

    @classmethod
    @abstractmethod
    def save_file(cls, data: str) -> None:
        """Guarda el archivo de configuracion con la informacion recibida,
           Puede lanzar un HTTPException si hay algun fallo"""

    @classmethod
    @abstractmethod
    def load_file(cls) -> str:
        """Retorna la informacion guardada del archivo de configuracion,
           Puede lanzar un HTTPException si hay algun fallo"""

    @staticmethod
    def get_type(config_type: str) -> type[ConfigFile]:
        """Obtiene el tipo correspondiente """
        config: type[ConfigFile]
        match config_type:
            case "Additional criteria parameters":
                config = AdditionalCriteriaParametersConfig
            case "Credibility criteria":
                config = CredibilityCriteriaConfig
            case "Criteria directions":
                config = CriteriaDirectionsConfig
            case "Criteria hierarchy":
                config = CriteriaHierarchyConfig
            case "Criteria interactions":
                config = CriteriaInteractionsConfig
            case "Criteria parameters":
                config = CriteriaParametersConfig
            case "Performance matrix":
                config = PerformanceMatrixConfig
            case "Use value function":
                config = UseValueFunctionConfig
            case "Veto thresholds for supercriteria":
                config = VetoThresholdsForSupercriteriaConfig
            case "Weights":
                config = WeightsConfig
            case _:
                error_msg = f"archivo de configuracion '{config_type} no encontrado"
                raise HTTPException(status_code=404, detail=error_msg)
        return config

class AdditionalCriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Additional criteria parameters"""
    config_type = "Additional criteria parameters.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class CredibilityCriteriaConfig(ConfigFile):
    """Clase para configuracion de Credibility criteria"""
    config_type = "Credibility criteria.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class CriteriaDirectionsConfig(ConfigFile):
    """Clase para configuracion de Criteria directions"""
    config_type = "Criteria directions.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class CriteriaHierarchyConfig(ConfigFile):
    """Clase para configuracion de Criteria hierarchy"""
    config_type = "Criteria hierarchy.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class CriteriaInteractionsConfig(ConfigFile):
    """Clase para configuracion de Criteria interactions"""
    config_type = "Criteria interactions.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class CriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Criteria parameters"""
    config_type = "Criteria parameters.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class PerformanceMatrixConfig(ConfigFile):
    """Clase para configuracion de Performance matrix"""
    config_type = "Performance matrix.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class UseValueFunctionConfig(ConfigFile):
    """Clase para configuracion de Use value function"""
    config_type = "Use value function.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class VetoThresholdsForSupercriteriaConfig(ConfigFile):
    """Clase para configuracion de Veto thresholds for supercriteria"""
    config_type = "Veto thresholds for supercriteria.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)

class WeightsConfig(ConfigFile):
    """Clase para configuracion de Weights"""
    config_type = "Weights.txt"

    @classmethod
    def save_file(cls, data: str) -> None:
        _write_config_file(cls.config_type, data)

    @classmethod
    def load_file(cls) -> str:
        return _read_config_file(cls.config_type)
