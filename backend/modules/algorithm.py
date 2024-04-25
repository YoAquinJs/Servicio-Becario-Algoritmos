"""Este modulo contiene el Enum de ExecAlgorithm y su funcionalidad para pasarlo a string"""
# pylint:disable=undefined-variable

from enum import Enum, EnumMeta
from typing import cast
from fastapi import HTTPException

class ParseableEnum[T](EnumMeta):
    """Makes a string parseable to the specified enum type
    """
    def __getitem__(cls, item: str) -> T:
        """This method parse from a string to the Enum object

        Args:
            item (str): The string to be parsed

        Returns:
            ParseableEnum: This enum
        """
        option = [opt for opt in cls._member_map_.values() if opt.value == item]
        if len(option) == 0:
            raise HTTPException(status_code=404, detail=f"Algoritmo {item} no encontrado")

        return cast(T, option[0])


# The value of each enum value has to be name of the directory of that algorithm
class ExecAlgorithm(Enum, metaclass=ParseableEnum):
    """Enum de las diferentes carpetas para la ejecucion del algoritmo"""

    SORTING="Calculate sorting"
    CREDIBILITY_MATRIX="Calculate credibility matrix"

def get_executable_param(algorithm: ExecAlgorithm) -> int:
    """Retorna el valor numerico que recibe el ejecutable
       el cual corresponde al algoritmo especificado"""
    match algorithm:
        case ExecAlgorithm.SORTING:
            return 3
        case ExecAlgorithm.CREDIBILITY_MATRIX:
            return 4
        case _:
            return -1
