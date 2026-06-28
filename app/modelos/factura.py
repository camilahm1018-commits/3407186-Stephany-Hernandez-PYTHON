from pydantic import BaseModel, computed_field
from app.modelos.transacciones import Transacciones
from app.modelos.cliente import Cliente, ClienteLeer
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)
    #transacciones: list[Transacciones] = []
    
    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        if self.transacciones == None:
            return total_factura
        #Recorre la lista de transacciones, segun el factura_id
        for transacciones in self.transacciones:
            total_factura += transacciones.vr_unitario * transacciones.cantidad
        return total_factura

class FacturaCrear(FacturaBase):
    # cliente_id: int  
    pass

class FacturaEditar(FacturaBase):
    # cliente_id: int
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # cliente: Cliente | None = None  
    # total: float | None = None
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #Crear las relaciones virtuales con Cliente, no en la Bd
    cliente : Cliente = Relationship(back_populates="factura")
    #Crear las relaciones virtuales con Transacciones, no en la Bd
    transacciones: list[Transacciones] = Relationship(back_populates="factura")
    
#Crear un modelo para mostrar al usuario

class FacturaLeer(FacturaBase):
    id: int 
    cliente: ClienteLeer
    #No es recomendable para buena practica
    #transacciones: list [Transacciones] = []
    
class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transacciones]= []