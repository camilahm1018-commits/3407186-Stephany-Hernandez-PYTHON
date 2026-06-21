from pydantic import BaseModel
from app.modelos.transacciones import Transacciones
from app.modelos.cliente import Cliente
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #transacciones: list[Transacciones] = []
    
    # def calcular_total(self):
    #     return sum(t.cantidad * t.vr_unitario for t in self.transacciones)

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