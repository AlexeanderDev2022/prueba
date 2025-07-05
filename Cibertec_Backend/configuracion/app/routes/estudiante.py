from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd.database import SessionLocal
from utils.response_handler import GenericResponse, handle_exception, handle_response
from services.estidiantes_service import registrar_estudiante, consulta_mesa
from schemas.estudiante_shemas import EstCreateSchema

documento = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@documento.post("/estudiante", tags=['Documento'])
def registrar_documento_api(permiso: EstCreateSchema, db: Session = Depends(get_db)):
    try:
        return handle_response(registrar_estudiante(db, permiso), print(EstCreateSchema))
    except Exception as e:
        # Usamos el handler para excepciones generales
        return handle_exception(e)


@documento.get("/estudiante", tags=['Documento'])
def registrar_documento_api(db: Session = Depends(get_db)):
    try:
        return handle_response(consulta_mesa(db))
    except Exception as e:
        # Usamos el handler para excepciones generales
        return handle_exception(e)


# @documento.get("/documento/{id}", tags=['Documento'])
# def consultar_documento_api(id: int, db: Session = Depends(get_db)):
#     try:
#         return handle_response(consulta_mesa(id, db),)
#     except Exception as e:
#         # Usamos el handler para excepciones generales
#         return handle_exception(e)


# @documento.delete("/documento/{id}", tags=['Documento'])
# def registrar_documento_api(id: int, db: Session = Depends(get_db)):
#     try:
#         return handle_response(eliminar_documento(id, db))
#     except Exception as e:
#         # Usamos el handler para excepciones generales
#         return handle_exception(e)


# @documento.put("/documento/{id}", tags=['Documento'])
# def update_documento_api(id: int, data: UpdateDoc, db: Session = Depends(get_db)):
#     try:
#         return handle_response(update_documento(id, data, db))
#     except Exception as e:
#         # Usamos el handler para excepciones generales
#         return handle_exception(e)
