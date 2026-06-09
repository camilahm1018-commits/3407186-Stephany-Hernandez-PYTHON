from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from fastapi import Depends

#Nombre BD
nombre_bd = "bd_clientes_3407186.sqlite3"

#Conexion BD, con una url (direccion)
url_bd = f"sqlite:///{nombre_bd}"

#motor de BD
motor_bd = create_engine(url_bd)

#obtener sesion en la BD sqlite
def obtener_sesion():
    with Session(motor_bd) as mi_sesion:
        yield mi_sesion

#Definir la dependencia, y esto registra mi sesion
sesion_dependencia = Annotated(Session, Depends(obtener_sesion))