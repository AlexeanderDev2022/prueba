from pydantic import BaseModel, EmailStr, constr
from enum import Enum
from datetime import datetime
from typing import Optional

# 🛠️ Esquema de Permiso (entrada de datos)


class EstadoEstudiante(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    egresado = "Egresado"
    suspendido = "Suspendido"
    retirado = "Retirado"


class EstSchema(BaseModel):
    nombre: str
    apellido: str
    dni: int
    email: EmailStr 
    estado: EstadoEstudiante


class EstResponse(BaseModel):
    IdEstudiante: int
    nombre: str


# 🛠️ Esquema de Auditoría


class AuditoriaSchema(BaseModel):
    idUsuaCrea: int
    noUsuaCrea: str

# 🛠️ Esquema que agrupa los datos de permiso y auditoría


class EstCreateSchema(BaseModel):
    estudiante: EstSchema
    # auditoria: AuditoriaSchema


class UpdateDoc(BaseModel):
    nombre: str
    logitud: int


class EstResponse(EstResponse):
    mensaje: str
    permiso: EstResponse
    # auditoria: AuditoriaSchema

    class Config:
        from_attributes = True




