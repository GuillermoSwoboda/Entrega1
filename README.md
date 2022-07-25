# **Entrega Proyecto Final**

## **URL DE LA PAGINA:**
http://127.0.0.1:8000/app/


### OBJETIVO:
Crear una página que nuclée varios comercios. En ella los comercios pueden indicar los productos con los que cuentan y la información de sus locales. Los usuarios en un futuro pueden acceder y ver los productos, marcas, locales y efectuar una compra (esto último a desarrollar)


### FUNCIONAMIENTO:
Cuando se ingrese a la página se pueden ver las marcas que existen, los productos y los comercios que forman parte de estar red


### FUNCIONALIDADES:

**MARCAS:**
- Generar una nueva marca:
Esto permite generar una marca nueva, donde se va a indicar el nombre de la marca, en un desplegable seleccionar la categoría a la que pertenece y la cantidad de productos que tiene dicha marca.
La creación de una nueva marca solo puede ser realizada por un usuario con perfil Administrador.

- Ver las marcas:
En la opción de Marcas se puede observar el nombre de la marca y la categoría a la que pertenece


**PRODUCTOS:**
- Crear un nuevo producto:
Esto permite crear un nuevo producto, donde se va a indicar el nombre del producto, en un desplegable seleccionar la categoría a la que pertenece, cual es el precio de venta y cuantas unidades hay en stock.
La creación de un nuevo producto puede ser realizado por un usuario registrado.

- Ver los productos:
En la opción de Productos se puede observar toda la información del producto y en la columna final figura si el producto tiene stock disponible o quedan pocas unidades o está agotado. Esto se generó con un if en el html de productos. El color de la palabra también sirve de indicador del nivel de stock disponible

- Buscar un producto:
Se puede buscar un producto y va a figurar la información del mismo

Si el usuario se loguea puede acceder a lo siguiente:
- Editar un producto:
Se puede editar un producto ya creado. Esta función la puede realizar cualquier usuario que se haya registrado previamente.

- Eliminar un producto:
Se puede eliminar un producto ya creado. Esta función la puede realizar solo un usuario con permiso de Administrador.


**LOCALES:**
- Añadir un nuevo locar:
Esto permite añadir un nuevo locar, donde se va a indicar el nombre del local, en un desplegable seleccionar la ciudad en la que se encuentra, el rubro principal que comercializa, la dirección del lugar, que días está abierto y el horario de apertura y de cierre.
La creación de un nuevo local puede ser realizado por un usuario registrado.

- Ver los locales:
En la opción de Locales se puede observar toda la información del local

- Buscar un local:
Se puede buscar un local y va a figurar la información del mismo

Si el usuario se loguea puede acceder a lo siguiente:
- Editar un local:
Se puede editar un local ya creado. Esta función la puede realizar cualquier usuario que se haya registrado previamente.

- Eliminar un local:
Se puede eliminar un local ya creado. Esta función la puede realizar solo un usuario con permiso de Administrador.


**INICIAR SESIÓN:**
El usuario puede ingresar con su nombre de usuario y contraseña


**REGISTRATE:**
El usuario puede registrarse y formar parte de la red de comercios


**HOLA, usuario!:**
Va a figurar la imagen que subió el usuario a su perfil


**CERRAR SESIÓN:**
Sirve para que el usuario haga un logout


**INICIO Y BIENVENIDO:**
Te llevan a la página principal


### PAGINA PRINCIPAL

**NUESTROS VALORES Y OBJETIVO:**
Figura la información sobre la empresa y lo que se busca a través de esta red de comercios


**BUSCA LO QUE NECESITES, QUE ACÁ LO VAS A ENCONTRAR:**
Te indica lo que podes navegar dentro de la página: Marcas Disponibles, Productos Disponibles y Donde Encontrarnos
Haciendo click en cada uno, te lleva a la página correspondiente


**QUERES FORMAR PARTE DE NUESTRA RED DE LOCALES? ADHERÍTE Y SUMÁ TU COMERCIO:**
Acá se van a poder ver dos cosas:
- Si no estás logueado: te da la posibilidad de Iniciar Sesión o de Registrarte
- Si ya estás logueado: te da la posibilidad de actualizar tus datos o subir una imagen a tu perfil


**FORMULARIO DE CONTACTO:**
- Se pueden completar el formulario de contacto con los datos según los requerimientos de cada campo


**PIE DE PÁGINA:**
- Figura mi nombre y apellido
- About me: te redirecciona a la página sobre mí


### DETALLES EXTRAS

**NOMBRES:**
- En cada una de las páginas se modificó el nombre que figura en la pestaña


**IMAGEN PÁGINA:**
- En el ícono de la pestaña figura la imagen de unatienda


### PAGINA WEB EN HEROKU
Pude subir la página a Heroku, pero no me funcionan todas las pestañas y las páginas.
Dejo el link para la página web https://lit-basin-97364.herokuapp.com/app/