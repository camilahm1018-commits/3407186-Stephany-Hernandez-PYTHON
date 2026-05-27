from pydantic import BaseModel
from modelo.transacciones import Transacciones
from modelo.cliente import Cliente



class FacturaBase(BaseModel):
    transacciones: list[Transacciones] = []  
    
    def calcular_total(self):
        return sum(t.cantidad * t.vr_unitario for t in self.transacciones)

class FacturaCrear(FacturaBase):
    cliente_id: int 

class FacturaEditar(FacturaBase):
    cliente_id: int

class Factura(FacturaBase):
    id: int | None = None
    cliente: Cliente | None = None  
    total: float | None = None