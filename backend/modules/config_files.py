"""Modulo de las clases que especifican el formato de los archivos de configuracion"""

from __future__ import annotations

from abc import ABC, abstractmethod
from fastapi import HTTPException

class ConfigFile(ABC):
    """Clase base para los archivos de configuracion"""
    FILE_EXTENSION = '.txt'

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

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class CredibilityCriteriaConfig(ConfigFile):
    """Clase para configuracion de Credibility criteria"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class CriteriaDirectionsConfig(ConfigFile):
    """Clase para configuracion de Criteria directions"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class CriteriaHierarchyConfig(ConfigFile):
    """Clase para configuracion de Criteria hierarchy"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class CriteriaInteractionsConfig(ConfigFile):
    """Clase para configuracion de Criteria interactions"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class CriteriaParametersConfig(ConfigFile):
    """Clase para configuracion de Criteria parameters"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class PerformanceMatrixConfig(ConfigFile):
    """Clase para configuracion de Performance matrix"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class UseValueFunctionConfig(ConfigFile):
    """Clase para configuracion de Use value function"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class VetoThresholdsForSupercriteriaConfig(ConfigFile):
    """Clase para configuracion de Veto thresholds for supercriteria"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass

class WeightsConfig(ConfigFile):
    """Clase para configuracion de Weights"""

    @classmethod
    def save_file(cls, data: str) -> None:
        pass

    @classmethod
    def load_file(cls) -> str:
        pass
