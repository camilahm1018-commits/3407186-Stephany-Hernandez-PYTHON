from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from fastapi import Depends
from fastapi import FastAPI

#Nombre BD
nombre_bd = "bd_clientes_3407186.sqlite3"

#Conexion BD, con una url (direccion)
url_bd = f"sqlite:///{nombre_bd}"


#motor de BD
motor_bd = create_engine(url_bd)


#Definir el metodo para crear las tablas

def crear_tablas(app: FastAPI):
    SQLModel.metadata.create_all(motor_bd)
    yield #No hay nada para retonar o ejecutar

#Definir el metodo para la sesion (obtener sesion en la BD sqlite)
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion


#Denominado inyeccion de dependencias
#Registrar la sesion como dependencia, utilizada en nuestros endpoint
#la dependencia, y esto registra mi sesion
Sesion_dependencia = Annotated[Session, Depends(obtener_sesion)]



