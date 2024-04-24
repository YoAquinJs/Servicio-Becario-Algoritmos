"""Este modulo contiene el Enum de ExecAlgorithm y su funcionalidad para pasarlo a string"""

from __future__ import annotations

from enum import EnumMeta
from typing import cast
from fastapi import HTTPException

class ParseableEnum(EnumMeta):
    """Makes a string parseable to the specified enum type
    """
    def __getitem__(cls, item: str) -> ParseableEnum:
        """This method parse from a string to the Enum object

        Args:
            item (str): The string to be parsed

        Returns:
            ParseableEnum: This enum
        """
        if item not in cls.__members__.keys():
            raise HTTPException(status_code=404, detail=f"Algoritmo {item} no encontrado")

        found = cls.__members__.get(item)
        return cast(ParseableEnum, found)


class ExecAlgorithm(ParseableEnum):
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
