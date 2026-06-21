
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

class TransaccionesBase(SQLModel):
    descripcion: str
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)

class crearTransacciones(TransaccionesBase):
    pass

class editarTransacciones(TransaccionesBase):
    pass

class Transacciones(TransaccionesBase, table= True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id : int | None = Field(default=None, foreign_key="factura.id")