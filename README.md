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
  -Factura: lista de transacciones, cliente, id, total y el metodo de calcular total -`Transacciones`: Descripccion, cantidad y vr_unitario
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

## 4 y 5 commit:

Se creo el README para que cada vez que haga un nuevo commit se pueda registrar aqui, donde relate que ue lo que hice en cada commit

## 6 commit:

Arregle la estructura de las carpetas para obtener una mejor organización en las carpetas y una mejor proyección en el proyecto, además, para ir familiarizandome de las estructuras de los archivos

## 7 commit:

En este commit se realizo:

- Creacion del archivo ` listas_app.py`
- Creacion del archivo ` Transacciones.py` en la carpeta `enrutador`
- En el archivo ` listas_app.py` se importo solo los modelos de factura y cliente ya que transacciones no tiene lista
- En el archivo ` clientes.py` de la carpeta `enrutador` se agregaron todas los endpoints de clientes, tambien se importo la lista de clientes del archivo `listas_app.py` , el modelo de clientes con sus clases y `APIRouter` para crear la ruta de clientes y para crear esas rutas se creo una variable llamada rutas_clientes
- En el archivo ` factura.py` de la carpeta `enrutador` se agregaron todas los endpoints de factura, tambien se importo la lista de factura y clientes del archivo `listas_app.py` , el modelo de factura con sus clases, el JSONResponse para los mensajes de error con sus codigos de estado y `APIRouter` para crear la ruta de factura, para crear esas rutas se creo una variable llamada rutas_factura
- En el archivo ` transacciones.py` de la carpeta `enrutador` se agregaron todas los endpoints de transacciones, tambien se importo la lista de factura del archivo `listas_app.py` , el modelo de transacciones con sus clases, el JSONResponse para los mensajes de error con sus codigos de estado y `APIRouter` para crear la ruta de transacciones y para crear esas rutas se creo una variable llamada rutas_transacciones
- En el archivo main.py se eliminaron todos los endpoints ya que se transladaron a los archvos de la crapeta enrutador, tambien se importo la carpeta `enrutador` donde se importaron los archivos de clientes, factura y transacciones y se importo el archivo `listas_app.py` con las listas de clientes y factura y por ultimo se agruparon los endpoints con la funcion de `tag` para para agregar las dierentes categorias de las rutas como clientes, factura y transacciones

## 8 commit:

En este commit se realizó:

- Se agregaron las dependencias `fastapi` y `sqlmodel` en el archivo `requirements.txt`.
- Se utilizo el archivo `conexion_bd.py` para gestionar la conexión con la base de datos SQLite.
- Se configuró el nombre y la URL de la base de datos `bd_clientes_3407186.sqlite3`.
- Se creó el motor de conexión mediante `create_engine()`.
- Se implementó la función `obtener_sesion()` para administrar las sesiones de la base de datos.
- Se definió la dependencia `sesion_dependencia` utilizando `Depends` y `Annotated` para facilitar el acceso a la sesión de la base de datos desde los endpoints de FastAPI.

## 9 commit:

En este commit se realizo:

- Se configuró la conexión a una base de datos `SQLite` mediante `SQLModel`.
- Se agregó la función `crear_tablas()` para generar automáticamente las tablas al iniciar la aplicación.
- Se modificó el archivo `main.py` para ejecutar la creación de tablas mediante el parámetro `lifespan`.
- El modelo `Cliente` fue actualizado de Pydantic a `SQLModel` para permitir su almacenamiento en la base de datos.
- Se definió la tabla cliente utilizando `table=True`.
- Se configuró el campo `id` del modelo `Cliente` como llave primaria mediante `primary_key=True`.
- Se reemplazó el atributo `edad` por el atributo `email` en el modelo de clientes.
- Se modificó el modelo Cliente para utilizar `Field()` de SQLModel en la definición de sus atributos.
- Se definieron los campos nombre, email y descripcion como columnas de la tabla cliente.
- Se generó el archivo de base de datos `bd_clientes_3407186.sqlite3`.
- Se actualizó el endpoint de listar clientes para consultar directamente la información almacenada en la base de datos.
- Se actualizó el endpoint de consultar cliente por id utilizando `mi_sesion.get()`.
- Se modificó el endpoint de creación para almacenar los registros mediante `add(), commit() y refresh()`.
- Se actualizó el endpoint de edición para modificar registros existentes directamente en la base de datos.
- Se actualizó el endpoint de eliminación para borrar registros utilizando la sesión de SQLModel.
- Se agregaron validaciones para verificar la existencia de un cliente antes de consultar, editar o eliminar.
- Se incorporaron respuestas personalizadas utilizando `JSONResponse` y códigos de estado HTTP.

## 10 commit:

En este commit se realizo:

- Se quito el `JSONResponse` cambiado por `HTTPException`
- En los endpoints de cliente se agrego el `response_model`
- Se hizo la CRUD en la base de datos con los clientes

## 11 commit:

En este commit se realizo:

- Se eliminaron los clientes de la BD para una practica
- Se translado el `.gitignore` para que ignore los `pycache` y `env`

## 12 commit:

En este commit se realizo:

- En los modelos de `Factura` y `Transacciones` se importo `SQLModel`,`Field` y `Relationship` para crear las tablas 
- En el campo de `Fecha` se cambio por `Field(default=datetime.now())`
- Se crearon las tablas de `Factura` y `Transacciones`
- Se creo la relación de las tablas por medio de las llaves Foraneas `Foreign_Key`


## 13 commit:

En este commit se realizó:

- Se hizo el CRUD completo de Factura conectado a la base de datos:
  - Se actualizó el endpoint de listar todas las facturas utilizando `select()` y `sesion.exec()`
  - Se actualizó el endpoint de consultar factura por id utilizando `sesion.get()`
  - Se actualizó el endpoint de creación de factura, recibiendo el `cliente_id` por la URL y validando que el cliente exista antes de crear la factura
  - Se actualizó el endpoint de edición de factura para permitir cambiar el `cliente_id` (por la URL) y la `fecha` (por el body) utilizando `sqlmodel_update()`
  - Se actualizó el endpoint de eliminación de factura utilizando la sesión de SQLModel

- Se hizo el CRUD completo de Transacciones conectado a la base de datos:
  - Se actualizó el endpoint de listar todas las transacciones
  - Se creó el endpoint para listar las transacciones de una factura específica utilizando `select().where()` filtrando por `factura_id`, validando primero que la factura exista
  - Se mantuvo el endpoint de crear transacción asociado a una factura
  - Se actualizó el endpoint de edición de transacción, simplificando la ruta para que solo dependa del `transaccion_id` ya que no era necesario el `factura_id` para esta operación
  - Se actualizó el endpoint de eliminación de transacción de la misma forma

- Se cambiaron los métodos `PUT` por `PATCH` en los endpoints de edición, ya que permiten actualizar solo los campos enviados gracias a `exclude_unset=True`

- Se eliminaron las importaciones de `listas_app` que ya no eran necesarias en los archivos `clientes.py` y `transacciones.py`, al no usar más las listas en memoria

- Se ajustó el modelo `Factura`:
  - Se cambió `fecha: str = Field(default=datetime.now())` por `fecha: datetime = Field(default_factory=datetime.now)`, para que la fecha se genere de forma dinámica en cada nueva factura y no quede fija desde que se inicia el servidor
  - Se dejó preparado el campo `vr_total` como `computed_field` para implementarlo más adelante con `Relationship`

## 14 commit:

En este commit se realizó:

- Se creó el archivo `.gitignore` en la raíz del proyecto, ya que anteriormente 
  se encontraba ubicado dentro de la carpeta `mi_env` y no cumplía su función
- Se agregaron las siguientes reglas al `.gitignore`:
  - `__pycache__/` → para ignorar las carpetas de caché de Python
  - `*.pyc` → para ignorar los archivos compilados de Python
  - `mi_env/` → para ignorar el entorno virtual
- Se eliminaron del rastreo de Git las carpetas `__pycache__` que ya estaban 
  subidas anteriormente, utilizando `git rm -r --cached`

## 15 commit:

En este commit se realizó:

- Se agregaron las relaciones virtuales entre los modelos utilizando `Relationship`:
- Se crearon modelos de lectura para mostrar la información al usuario sin exponer 
  directamente los modelos de la base de datos:
  - `ClienteLeer`
  - `FacturaLeer` (incluye el cliente con `ClienteLeer`)
  - `FacturaLeerCompuesta` (incluye también las transacciones)
  - `TransaccionesLeer`
- Se actualizó el `computed_field` `vr_total` en el modelo `Factura` para calcular 
  el total recorriendo la lista de `transacciones` obtenida mediante la relación virtual
- Se actualizó el endpoint `GET /factura` para utilizar `response_model=list[FacturaLeerCompuesta]`