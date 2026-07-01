from ..modelos.transacciones import Transacciones,crearTransacciones,editarTransacciones
from ..modelos.factura import Factura
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select
from fastapi import APIRouter, HTTPException, status

rutas_transacciones = APIRouter ()


@rutas_transacciones.get("/transacciones", response_model=list[Transacciones])
async def listar_transacciones(sesion:Sesion_dependencia):
    consulta = select(Transacciones)
    lista_transacciones = sesion.exec(consulta).all()
    return lista_transacciones

    #Resumindo en una linea
    #return sesion.exec(select(Transacciones)).all()

@rutas_transacciones.get("/factura/{factura_id}/transacciones", response_model=list[Transacciones])
async def listar_transacciones(factura_id: int, sesion: Sesion_dependencia):
    
    
    Factura_encontrada= sesion.get(Factura, factura_id)

    
    if not Factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Factura con id: {factura_id}, no exite."
        )
        
    consulta = select(Transacciones).where(Transacciones.factura_id == factura_id)
    id_transaccion = sesion.exec(consulta).all()
    
    return id_transaccion

@rutas_transacciones.post("/factura/{factura_id}/transacciones", response_model=Transacciones)
async def agregar_transaccion(factura_id: int, datos_transaccion: crearTransacciones, sesion: Sesion_dependencia):
    
    Factura_encontrada= sesion.get(Factura, factura_id)

    
    if not Factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Factura con id: {factura_id}, no exite."
        )
    
    
    #Validar datos de la transacion - json y pasamos a un diccionario
    
    transacciones_dict = datos_transaccion.model_dump()
    transacciones_dict["factura_id"] = factura_id
    transacciones_val = Transacciones.model_validate(transacciones_dict)
    
    #Guardar en la bd
    
    sesion.add(transacciones_val)
    sesion.commit()
    sesion.refresh(transacciones_val)
    
    return transacciones_val


@rutas_transacciones.patch("/transacciones/{transacciones_id}", response_model=Transacciones)
async def editar_transacciones(transacciones_id: int, datos_transaccion: editarTransacciones, sesion:Sesion_dependencia):
    
    transacciones = sesion.get(Transacciones, transacciones_id)
    
    if not transacciones:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Transaccion con id: {transacciones_id}, no exite."
        )

    transacciones_dict = datos_transaccion.model_dump(exclude_unset=True)
    transacciones.sqlmodel_update(transacciones_dict)
    

    sesion.add(transacciones) 
    sesion.commit() 
    sesion.refresh(transacciones)
    
    return transacciones
    
@rutas_transacciones.delete("/transacciones/{transacciones_id}", response_model=Transacciones)
async def eliminar_transacciones(transacciones_id: int, sesion: Sesion_dependencia):
    
    transacciones = sesion.get(Transacciones, transacciones_id)
    
    
    if not transacciones:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Transaccion con id: {transacciones_id}, no exite."
        )


    transaccion_eliminada = Transacciones.model_validate(transacciones)

    sesion.delete(transacciones)
    sesion.commit()

    return transaccion_eliminada
    
