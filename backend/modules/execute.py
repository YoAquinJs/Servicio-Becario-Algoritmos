"""Modulo que continue la funcionalidad para correr el ejecutable"""

from subprocess import CalledProcessError, TimeoutExpired, run
from fastapi import HTTPException

COMMAND = "java -jar executable.jar 4"

def run_executable() -> dict[str, str]:
    """Ejecuta el ejecutable"""
    try:
        result = run(COMMAND, shell=True, capture_output=True, text=True, check=True)
        return {"response":result.stdout}
    except CalledProcessError as exc:
        raise HTTPException(status_code=500, detail=exc.output) from exc
    except TimeoutExpired as exc:
        error_msg = "timeout en la ejecucion del algoritmo"
        raise HTTPException(status_code=500, detail=error_msg) from exc
