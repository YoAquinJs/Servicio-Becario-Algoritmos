"""Modulo para la funcionalidad de carga de matrices de credibilidad"""

import csv
from os import path
from fastapi import HTTPException

ENCODING = "utf-8"
MATRIX_SUFIX = "-CredibilityMatrix.txt"
MATRIX_DIRECTORY = path.join("Files", "Calculate credibility matrix", "Credibility matrices")

def load_credibility_matrix(matrix_type: str) -> list[list[float]]:
    """Carga el archivo de matriz de credibilidad correspondiente"""
    try:
        matrix_path = path.join(MATRIX_DIRECTORY, matrix_type+MATRIX_SUFIX)
        with open(matrix_path, "r", encoding=ENCODING) as file:
            matrix = []
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                matrix.append(row)
            return matrix
    except FileNotFoundError as exc:
        error_msg = f"matriz de credibilidad '{matrix_type}' no encontrada"
        raise HTTPException(status_code=404, detail=error_msg) from exc
