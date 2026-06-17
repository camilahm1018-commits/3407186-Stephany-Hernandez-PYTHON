from ..listas_app import lista_clientes
from app.modelos.cliente import Cliente,ClienteCrear,ClienteEditar
from fastapi import APIRouter, status
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select
from fastapi.responses import JSONResponse


ruta_clientes = APIRouter()

@ruta_clientes.get("/clientes")
async def listar_clientes(sesion: Sesion_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli


@ruta_clientes.get("/clientes/{id}")
async def listar_cliente(id: int, mi_sesion: Sesion_dependencia): # type: ignore

    cliente = mi_sesion.get(Cliente, id)
    if not cliente:
        return JSONResponse (
            status_code= status.HTTP_400_BAD_REQUEST,
            content={"error": "Cliente no encontrado"}
        )

    return {"mensaje": "Se encontro correctamente el cliente","cliente":cliente}


@ruta_clientes.post("/clientes")
async def crear_clientes(datos_cliente: ClienteCrear,  mi_sesion: Sesion_dependencia): # type: ignore
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return {"mensaje": "Se creo correctamente el cliente","cliente":cliente_val}


@ruta_clientes.patch("/clientes/{id}")
async def editar_clientes(id: int,datos_cliente: ClienteEditar,mi_sesion: Sesion_dependencia):

    cliente = mi_sesion.get(Cliente, id)

    if not cliente:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Cliente no encontrado"}
        )

    # # cliente.nombre = datos_cliente.nombre
    # # cliente.email = datos_cliente.email
    # # cliente.descripcion = datos_cliente.descripcion

    cliente_dict = datos_cliente.model_dump(exclude_unset=True)
    cliente.sqlmodel_update(cliente_dict)

    mi_sesion.add(cliente)
    mi_sesion.commit()
    mi_sesion.refresh(cliente)

    return {"mensaje": "Cliente actualizado correctamente","cliente": cliente}
        

@ruta_clientes.delete("/clientes/{id}")
async def listar_cliente(id:int, mi_sesion: Sesion_dependencia):

    cliente= mi_sesion.get(Cliente, id)

    if not cliente:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Cliente no encontrado"}
        )
    
    mi_sesion.delete(cliente)
    mi_sesion.commit()
    
    return {"mensaje" : "se elmino correctamente","Clientes":cliente}