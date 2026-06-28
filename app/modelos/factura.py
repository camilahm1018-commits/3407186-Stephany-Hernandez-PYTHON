from pydantic import BaseModel, computed_field
from app.modelos.transacciones import Transacciones
from app.modelos.cliente import Cliente
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)
    #transacciones: list[Transacciones] = []
    
    @computed_field
    @property
    def vr_total(self) -> float:
        # return sum(t.cantidad * t.vr_unitario for t in self.transacciones)
        # factura_id_actual = getattr(self, "id", None)
        # total_factura = 0.0
        # if not factura_id_actual or not self.transacciones:
        #     return total_factura
        # for transacciones in self.transacciones:
        #     if transacciones.factura_id == factura_id_actual:
        #         total_factura+= transacciones.vr_unitario * transacciones.cantidad
        return 0.0

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
    