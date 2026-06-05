from ..listas_app import lista_factura,lista_clientes
from app.modelos.factura import Factura,FacturaCrear,FacturaEditar
from fastapi.responses import JSONResponse
from fastapi import APIRouter

rutas_factura = APIRouter()

@rutas_factura.get("/factura")
async def listar_factura():
    return {"Factura": lista_factura}

@rutas_factura.get("/factura/{id}")
async def listar_factura_id(id: int):
    for factura in lista_factura:
        if factura.id == id:
            return factura
    return {"mensaje": "Factura no encontrada"}

@rutas_factura.post("/factura", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    # buscar el cliente
    cliente = next((c for c in lista_clientes if c.id == datos_factura.cliente_id), None)
    
    if cliente is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Cliente no encontrado"}
        )

    factura_val = Factura(
        id=len(lista_factura) + 1,
        cliente=cliente,
        transacciones=datos_factura.transacciones,
        total=0
    )
    factura_val.total = factura_val.calcular_total()
    lista_factura.append(factura_val)
    return factura_val



@rutas_factura.put("/factura/{id}")
async def editar_factura(id: int, datos_factura: FacturaEditar):
    cliente = next((c for c in lista_clientes if c.id == datos_factura.cliente_id), None)
    factura = next((f for f in lista_factura if f.id == id), None)
    
    if cliente is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Cliente no encontrado"}
        )

    if factura is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Factura no encontrada"}
        )
    
    for i, obj_factura in enumerate(lista_factura):  
        if obj_factura.id == id:
            factura_val = Factura(
                id=id,
                cliente=cliente,
                transacciones=datos_factura.transacciones,
                total=0
            )
            factura_val.total = factura_val.calcular_total()  
            lista_factura[i] = factura_val 
            return {"mensaje": "Se actualizó la factura correctamente", "Factura": factura_val}


@rutas_factura.delete("/factura/{id}")
async def eliminar_factura(id: int):
    for i, obj_factura in enumerate(lista_factura):  
        if obj_factura.id == id:
            factura_val = Factura.model_validate(obj_factura.model_dump())
            factura_val.id = id
            lista_factura.pop(i) 
            return {"mensaje" : "Se eliminó correctamente","Factura":factura_val}
    return {"mensaje": "Factura no encontrada"}