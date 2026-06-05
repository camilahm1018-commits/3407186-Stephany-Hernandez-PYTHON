from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.modelos.cliente import Cliente, ClienteCrear, ClienteEditar
from app.modelos.transacciones import crearTransacciones,editarTransacciones,Transacciones
from app.modelos.factura import  Factura, FacturaCrear, FacturaEditar
from .enrutador import clientes, factura, transacciones
from .listas_app import lista_clientes,lista_factura

app= FastAPI()

app.include_router(clientes.ruta_clientes, tags=["Clientes"])
app.include_router(factura.rutas_factura, tags=["Factura"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])

#lista de clientes en BD


#actividad 2 en casa

#Factura





#Transacciones 



