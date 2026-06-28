from app.modelos.factura import Factura,FacturaCrear,FacturaEditar
from fastapi import APIRouter, HTTPException, status
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select
from app.modelos.cliente import Cliente


rutas_factura = APIRouter()

@rutas_factura.get("/factura", response_model=list[Factura])
async def listar_factura(sesion: Sesion_dependencia):
    #Hacer una consulta con select : Select * from factura 
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas

@rutas_factura.get("/factura/{factura_id}", response_model=Factura)
async def listar_factura_id(factura_id: int, sesion: Sesion_dependencia):
    
    factura= sesion.get(Factura,factura_id)
    if not factura:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Factura no encontrado"
        )
    return factura

@rutas_factura.post("/factura/{cliente_id}", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear, cliente_id: int, sesion: Sesion_dependencia):
    # buscar el cliente
    cliente =  sesion.get(Cliente, cliente_id)
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cliente con id: {cliente_id}, no exite."
        )


    #Validar los datos- json, pero debemos pasar a un diccionario
    factura_dict = datos_factura.model_dump()
    factura_dict ["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    
    #guardar en la bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val



@rutas_factura.patch("/factura/{id}/{cliente_id}", response_model=Factura)
async def editar_factura(factura_id: int,cliente_id: int, datos_factura: FacturaEditar, sesion: Sesion_dependencia):
    
    cliente = sesion.get(Cliente, cliente_id)
    factura= sesion.get(Factura,factura_id)
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente no encontrado"
        )

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Factura no encontrado"
        )
    
    factura_dict = datos_factura.model_dump(exclude_unset=True)
    factura.sqlmodel_update(factura_dict)
    
    factura.cliente_id = cliente_id 

    sesion.add(factura) 
    sesion.commit() 
    sesion.refresh(factura)

    return factura


@rutas_factura.delete("/factura/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int, sesion: Sesion_dependencia):
    
    factura= sesion.get(Factura, factura_id)
    
    if not factura:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Factura no encontrado"
        )
        
    factura_eliminada = Factura.model_validate(factura)

    sesion.delete(factura)
    sesion.commit()

    return factura_eliminada
    