# Datos Personales

Nombre: Stephany Camila Hernández Morales
Ficha:3407186

# Pasos Realizados

Se creó el repositorio nuevo ya que el repositorio inicial quedó vinculado a la cuenta de otro aprendiz. Se clonó lo trabajado en clase y se subió a este nuevo repositorio.

## 1 commit:

En este commit se realizó:

- Creación del modelo `Cliente` con sus diferentes clases las cuales tienen sus atributos (nombre, edad, descripcion)
- Creación del archivo `main.py` como punto central de la aplicación
- Importación de FastAPI y del modelo Cliente
- Creación de la lista `lista_clientes` donde se almacenan los clientes creados
- Implementación del CRUD completo para clientes:
- GET /clientes → listar todos los clientes
- GET /clientes/{id} → obtener un cliente por id
- POST /clientes → crear un cliente - PUT /clientes/{id} → editar un cliente
- DELETE /clientes/{id} → eliminar un cliente
- El id del cliente se genera automáticamente con `len(lista_clientes) + 1`
- Se probó cada endpoint en `/docs` al finalizar cada paso

## 2 commit:

En este commit se realizó:

- Creación de los modelos `Factura` y `Transacciones` con con sus diferentes clases y atributos
  -Factura: lista de transacciones, cliente, id, total y el metodo de calcular total
  -`Transacciones`: Descripccion, cantidad y vr_unitario
- Importación de los modelos `Factura` y `Transacciones` con los nombres de las clases en `main.py`
- creación de la lista `lista_factura` donde se guardan todas las facturas
- se realizo el crud Factura:
  - `GET /factura` → listar todas las facturas
  - `GET /factura/{id}` → obtener una factura por id
  - `POST /factura` → crear una factura
  - `PUT /factura/{id}` → editar una factura
  - `DELETE /factura/{id}` → eliminar una factura

  - se realizo el crud de transacciones:
    - `GET /factura/{id}/transacciones` → listar transacciones de una factura
    - `POST /factura/{id}/transacciones` → agregar una transacción a una factura
    - `PUT /factura/{id}/transacciones/{transaccion_id}` → editar una transacción
    - `DELETE /factura/{id}/transacciones/{transaccion_id}` → eliminar una transacción
- se importo JSONResponse para mostrar mensajes de error con su código de estado cuando no se encuentra un cliente o una factura

- Las transacciones van dentro de la factura, por lo tanto no se crea una 
  lista separada para transacciones sino que se accede a ellas a través 
  de la factura con `factura.transacciones`
- 
- Se probó cada endpoint en `/docs` al finalizar cada pas

## 3 commit:

En este commit se realizó:

-Se agregó el campo `fecha` en la clase `FacturaBase` del modelo `Factura` 
  para que se registre automáticamente en tiempo real al crear una factura

- Se importó la librería `datetime` en el modelo `Factura` para generar la fecha automáticamente
