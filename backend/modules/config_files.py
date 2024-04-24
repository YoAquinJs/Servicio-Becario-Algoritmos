"""Modulo de las clases que especifican el formato de los archivos de configuracion"""

from __future__ import annotations

from abc import ABC, abstractmethod
from os import path
from fastapi import HTTPException
from modules.algorithm import ExecAlgorithm

CONFIG_EXT = ".txt"
CONFIG_DIRECTORY = "Files"
ENCODING = "utf-8"

def _read_config_file(algorithm: ExecAlgorithm, config_type: str) -> str:
    file_path = path.join(CONFIG_DIRECTORY, algorithm.value, config_type)+CONFIG_EXT
    with open(file_path, "r", encoding=ENCODING) as file:
        return file.read()

def _write_config_file(algorithm: ExecAlgorithm, config_type: str, data: str) -> None:
    file_path = path.join(CONFIG_DIRECTORY, algorithm.value, config_type)+CONFIG_EXT
    with open(file_path, "w", encoding=ENCODING) as file:
        file.write(data.replace('\r\n', '\n'))

class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""

    @classmethod
    @abstractmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        """Guarda el archivo de configuracion con la informacion recibida,
           Puede lanzar un HTTPException si hay algun fallo"""

    @classmethod
    @abstractmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        """Retorna la informacion guardada del archivo de configuracion,
           Puede lanzar un HTTPException si hay algun fallo"""

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
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class CredibilityCriteriaConfig(ConfigFile):
    """Clase para configuracion de Credibility criteria"""
    config_type = "Credibility criteria"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class CriteriaDirectionsConfig(ConfigFile):
    """Clase para configuracion de Criteria directions"""
    config_type = "Criteria directions"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class CriteriaHierarchyConfig(ConfigFile):
    """Clase para configuracion de Criteria hierarchy"""
    config_type = "Criteria hierarchy"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class CriteriaInteractionsConfig(ConfigFile):
    """Clase para configuracion de Criteria interactions"""
    config_type = "Criteria interactions"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class CriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Criteria parameters"""
    config_type = "Criteria parameters"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class PerformanceMatrixConfig(ConfigFile):
    """Clase para configuracion de Performance matrix"""
    config_type = "Performance matrix"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class UseValueFunctionConfig(ConfigFile):
    """Clase para configuracion de Use value function"""
    config_type = "Use value function"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class VetoThresholdsForSupercriteriaConfig(ConfigFile):
    """Clase para configuracion de Veto thresholds for supercriteria"""
    config_type = "Veto thresholds for supercriteria"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)

class WeightsConfig(ConfigFile):
    """Clase para configuracion de Weights"""
    config_type = "Weights"

    @classmethod
    def save_file(cls, algorithm: ExecAlgorithm, data: str) -> None:
        _write_config_file(algorithm, cls.config_type, data)

    @classmethod
    def load_file(cls, algorithm: ExecAlgorithm) -> str:
        return _read_config_file(algorithm, cls.config_type)
