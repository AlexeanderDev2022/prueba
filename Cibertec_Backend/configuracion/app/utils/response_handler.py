from http import HTTPStatus
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any

class GenericResponse(BaseModel):
    mensaje: str
    status: int
    data: Any


def handle_response(data: Any, mensaje: str = "Operación exitosa", status: int = HTTPStatus.OK):
    """
    Genera una respuesta estándar para respuestas exitosas.
    """
    return {
        "mensaje": mensaje,
        "status": status,
        "data": data
    }


def handle_exception(e: Any):
    """
    Maneja excepciones y devuelve un response estructurado según el status_code.
    """
    print("error =============================> ",vars(e))
    error_message = str(e)
    # status_code = HTTPStatus.INTERNAL_SERVER_ERROR  # Código por defecto
    status_code = getattr(e, "status_code", HTTPStatus.INTERNAL_SERVER_ERROR)
    if isinstance(e, HTTPException):
        status_code = e.status_code
    if isinstance(e, ValueError):
        status_code = HTTPStatus.BAD_REQUEST
    elif isinstance(e, PermissionError):
        status_code = HTTPStatus.FORBIDDEN
    elif isinstance(e, RequestValidationError):  # Captura errores de validación de FastAPI
        status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        error_message = e.errors()

    return JSONResponse(
        status_code=status_code,
        content={
            "mensaje": error_message,
            "status": status_code,
            "data": {}
        }
    )
