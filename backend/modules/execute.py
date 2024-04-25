"""Modulo que continue la funcionalidad para correr el ejecutable"""

from subprocess import CalledProcessError, TimeoutExpired, run
from fastapi import HTTPException
from modules.algorithm import ExecAlgorithm, get_executable_param

COMMAND = "java -jar executable.jar"

def run_executable(algorithm: ExecAlgorithm) -> str:
    """Ejecuta el ejecutable"""
    try:
        command = f"{COMMAND} {get_executable_param(algorithm)}"
        result = run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except CalledProcessError as exc:
        raise HTTPException(status_code=500, detail=exc.output) from exc
    except TimeoutExpired as exc:
        error_msg = "timeout en la ejecucion del algoritmo"
        raise HTTPException(status_code=500, detail=error_msg) from exc
