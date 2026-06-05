from fastapi.responses import JSONResponse
from ..listas_app import lista_factura
from app.modelos.transacciones import Transacciones,crearTransacciones,editarTransacciones
from fastapi import APIRouter

rutas_transacciones = APIRouter ()


@rutas_transacciones.get("/factura/{id}/transacciones")
async def listar_transacciones(id: int):
    factura = next((f for f in lista_factura if f.id == id), None)
    
    if factura is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Factura no encontrada"}
        )
    
    return {"transacciones": factura.transacciones}

@rutas_transacciones.post("/factura/{id}/transacciones")
async def agregar_transaccion(id: int, datos_transaccion: crearTransacciones):
    factura = next((f for f in lista_factura if f.id == id), None)
    
    if factura is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Factura no encontrada"}
        )
    
    transaccion_val = Transacciones(
        id=len(factura.transacciones) + 1,
        cantidad=datos_transaccion.cantidad,
        vr_unitario=datos_transaccion.vr_unitario,
        descripcion=datos_transaccion.descripcion
    )
    
    factura.transacciones.append(transaccion_val)
    factura.total = factura.calcular_total()
    
    return {"mensaje": "Transaccion agregada", "factura": factura}


@rutas_transacciones.put("/factura/{id}/transacciones/{transacciones_id}")
async def editar_transacciones(id: int,transacciones_id: int, datos_transaccion: editarTransacciones):
    factura = next((f for f in lista_factura if f.id == id), None)
    
    if factura is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Factura no encontrada"}
        )

    for t in factura.transacciones:
        if t.id == transacciones_id:
            t.cantidad = datos_transaccion.cantidad
            t.vr_unitario = datos_transaccion.vr_unitario
            t.descripcion = datos_transaccion.descripcion

            factura.total = factura.calcular_total()
            return {"mensaje": "Transaccion actualizada", "factura": factura}
        
    return {"mensaje": "Transaccion no encontrada"}
    
@rutas_transacciones.delete("/factura/{id}/transacciones/{transacciones_id}")
async def eliminar_transacciones(id: int, transacciones_id: int):
    factura = next((f for f in lista_factura if f.id == id), None)
    
    if factura is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Factura no encontrada"}
        )

    for t in factura.transacciones:
        if t.id == transacciones_id:
            factura.transacciones.remove(t)
            factura.total = factura.calcular_total()
            return {"mensaje": "Transaccion eliminada", "factura": factura}
        
    return {"mensaje": "Transaccion no encontrada"}
