"""Modulo que continue la funcionalidad para correr el ejecutable"""

from subprocess import CalledProcessError, TimeoutExpired, run

from fastapi import HTTPException

from modules.base_algorithm import ExecAlgorithm

COMMAND = "java -jar executable.jar"

def run_executable(algorithm: type[ExecAlgorithm]) -> str:
    """Ejecuta el algoritmo"""
    try:
        command = f"{COMMAND} {algorithm.exec_param}"
        print(command) #TODO loggign
        result = run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except CalledProcessError as exc:
        raise HTTPException(status_code=500, detail=exc.stderr) from exc
    except TimeoutExpired as exc:
        error_msg = "timeout en la ejecucion del algoritmo"
        raise HTTPException(status_code=500, detail=error_msg) from exc
