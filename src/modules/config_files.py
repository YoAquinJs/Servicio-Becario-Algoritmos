"""
Este módulo contiene la validación de formato, para cada implementación de archivo de configuración.
"""

from fastapi import HTTPException

from modules.base_config_file import ConfigFile


def get_config_type(config_type: str) -> type[ConfigFile]:
    """Obtiene el tipo correspondiente de archivo de configuracion"""
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
        case SortingCriteria.config_type:
            config = SortingCriteria
        case _:
            error_msg = f"archivo de configuracion '{config_type}' no encontrado"
            raise HTTPException(status_code=404, detail=error_msg)
    return config

DATA_SEPARATOR = "\t"

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

class SortingCriteria(ConfigFile):
    """Clase para configuracion de Sorting criteria"""
    config_type = "Sorting criteria"

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        return True
