from ..listas_app import lista_clientes
from app.modelos.cliente import Cliente,ClienteCrear,ClienteEditar
from fastapi import APIRouter

ruta_clientes = APIRouter()

@ruta_clientes.get("/clientes")
async def listar_clientes():
    return {"Cliente": lista_clientes}

@ruta_clientes.get("/clientes/{id}")
async def listar_cliente(id:int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente


@ruta_clientes.post("/clientes", response_model = Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes)+1
    
    lista_clientes.append(cliente_val)
    return cliente_val


@ruta_clientes.put("/clientes/{id}")
async def editar_clientes(id:int, datos_cliente:ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):  
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val 
            return {"mensaje": "Se actualizo el cliente correctamente", "Cliente": cliente_val}
    

    
@ruta_clientes.delete("/clientes/{id}")
async def listar_cliente(id:int):
    for i, obj_cliente in enumerate(lista_clientes):  
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(obj_cliente.model_dump())
            cliente_val.id = id
            lista_clientes.pop(i) 
            return {"mensaje" : "se elmino correctamente","Clientes":cliente_val}