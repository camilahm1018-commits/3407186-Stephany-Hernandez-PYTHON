from pydantic import BaseModel

class Factura (BaseModel):
    #atribitos
    id: int
    fecha: date
    total: float
    cliente: str
    