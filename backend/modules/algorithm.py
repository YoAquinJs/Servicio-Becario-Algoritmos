"""Este modulo contiene el Enum de ExecAlgorithm y su funcionalidad para pasarlo a string"""
# pylint:disable=undefined-variable

from enum import Enum, EnumMeta, auto
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
        option = [opt[0] for opt in EXECUTABLE_CONFIG_DIR.items() if opt[1] == item]
        if len(option) == 0:
            raise HTTPException(status_code=404, detail=f"Algoritmo {item} no encontrado")

        return cast(T, option[0])


class ExecAlgorithm(Enum, metaclass=ParseableEnum):
    """Enum de las diferentes carpetas para la ejecucion del algoritmo"""

    SORTING=auto()
    CREDIBILITY_MATRIX=auto()

EXECUTABLE_CONFIG_DIR: dict[ExecAlgorithm, str] = {
    ExecAlgorithm.SORTING: "Calculate sorting",
    ExecAlgorithm.CREDIBILITY_MATRIX: "Calculate credibility matrix",
}

EXECUTABLE_OUTPUT_DIR: dict[ExecAlgorithm, str] = {
    ExecAlgorithm.SORTING: "Sorting",
    ExecAlgorithm.CREDIBILITY_MATRIX: "Credibility matrices",
}

EXECUTABLE_PARAMS: dict[ExecAlgorithm, int] = {
    ExecAlgorithm.SORTING: 3,
    ExecAlgorithm.CREDIBILITY_MATRIX: 4,
}
