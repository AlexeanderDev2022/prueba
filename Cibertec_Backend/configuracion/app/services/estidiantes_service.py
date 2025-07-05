from sqlalchemy.orm import Session
from models.estudiante import Estudiante
from schemas.estudiante_shemas import EstCreateSchema
# from events.event_publisher import publish_event
import datetime


def registrar_estudiante(db: Session, data: EstCreateSchema):
    # if db.query(Mesa).filter(Mesa.numero == data.mesa.numero).first():
    # print("Error: El nombre ya existe")
    # return {"error": f"El nuemero de mesa {data.mesa.numero} ya existe"}
    nuevo_estudiante = Estudiante(
        nombre=data.estudiante.nombre,
        apellido=data.estudiante.apellido,
        dni=data.estudiante.dni,
        email=data.estudiante.email,
        estado=data.estudiante.estado)

    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)


# Publicamos un evento cuando se crea un permiso
# publish_event("permiso_creado", {"idModulo": nueva_mesa.idModulo, "nombre": nueva_mesa.nombre})
    print('nueva mesa =================> ', vars(nuevo_estudiante))
    return {
        "Estdiante": {
            "IdEstudiante": nuevo_estudiante.id_estudiante,
            "nombre": nuevo_estudiante.nombre,
            "apellido": nuevo_estudiante.apellido,
            "DNI": nuevo_estudiante.dni,
            "correo": nuevo_estudiante.email,
            "estado": nuevo_estudiante.estado

        },
        # "auditoria": {
        #     "idUsuaCrea": nueva_mesa.idUsuaCrea,
        #     "noUsuaCrea": nueva_mesa.noUsuaCrea,
        # }
    }



def consulta_mesa(db):
    estudiante = db.query(Estudiante).all()
    if estudiante == []:
        return "No hay Estudantes registrados"
    return estudiante



# def consulta_mesa_Id(id, db):
#     consult = db.query(Mesa).filter(Mesa.idMesas == id).first()
#     if consult == None:
#         return (f'No hay la permiso con el id {id}')
#     return consult


# def eliminar_mesa(id, db):
#     consult = db.query(Mesa).filter(Mesa.idMesas == id).first()
#     if consult is None:
#         return (f"No hay  permiso con el id {id}")
#     db.delete(consult)
#     db.commit()
#     return {"mensaje": "Eliminado correctamente"}


# def update_mesa(id, data: UpdateMesa, db):
#     # if data.capacidad <= 3 or data.capacidad >= 50:
#     #     return {"msg": "El nombre contener entre 3 y 50 caracteres"}
#     db.query(Mesa).filter(Mesa.idMesas == id).update({
#         "nombre": data.mesa.nombre,
#         'numero': data.mesa.numero,
#         "capacidad": data.mesa.capacidad,
#         "feModi": datetime.datetime.now().isoformat()
#     })
#     db.commit()
#     return ('Actualizado')
