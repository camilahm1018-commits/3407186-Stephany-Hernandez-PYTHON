from fastapi import FastAPI
from .modelos.cliente import Cliente
from .enrutador import clientes, factura, transacciones
from .listas_app import lista_clientes,lista_factura
from .conexion_bd import crear_tablas

app= FastAPI(lifespan=crear_tablas)

app.include_router(clientes.ruta_clientes, tags=["Clientes"])
app.include_router(factura.rutas_factura, tags=["Factura"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])

#lista de clientes en BD


#actividad 2 en casa

#Factura





#Transacciones 



