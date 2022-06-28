# Entrega1

URL DE LA PAGINA:
http://127.0.0.1:8000/app/

OBJETIVO
Crear una página que nuclée varios comercios. En ella los comercios pueden indicar cuales son las marcas con las que trabajan y los productos con los que cuentan. Los usuarios en un futuro pueden acceder y ver los productos, marcas, locales y efectuar una compra (esto último a desarrollar)

FUNCIONAMIENTO
Los comercios pueden ingresar a la página, ver que marcas existen, ver los productos y los comercios que forman parte de estar red

FUNCIONALIDADES:

* MARCAS
- Generar una nueva marca:
Esto permite generar una marca nueva, donde se va a indicar el nombre de la marca, en un desplegable seleccionar la categoría a la que pertenece y la cantidad de productos que tiene dicha marca

- Ver las marcas:
En la opción de Marcas se puede observar el nombre de la marca y la categoría a la que pertenece


* PRODUCTOS
- Crear un nuevo producto:
Esto permite crear un nuevo producto, donde se va a indicar el nombre del producto, en un desplegable seleccionar la categoría a la que pertenece, cual es el precio de venta y cuantas unidades hay en stock

- Ver los productos:
En la opción de Productos se puede observar toda la información del producto y en la columna final figura si el producto tiene stock disponible o quedan pocas unidades o está agotado. Esto se generó con un if en el html de productos. El color de la palabra también sirve de indicador del nivel de stock disponible

- Buscar un producto:
Se puede buscar un producto y va a figurar la información del mismo

* LOCALES
- Añadir un nuevo locar:
Esto permite añadir un nuevo locar, donde se va a indicar el nombre del local, en un desplegable seleccionar la ciudad en la que se encuentra, el rubro principal que comercializa, la dirección del lugar, que días está abierto y el horario de apertura y de cierre

- Ver los locales:
En la opción de Locales se puede observar toda la información del local

* FORMULARIO DE CONTACTO
- Se pueden completar el formulario de contacto con los datos según los requerimientos de cada campo

* NOMBRES
- En cada una de las páginas se modificó el nombre que figura en la pestaña y se modificó el ícono de la pestaña por el de una tienda

CONSIGNAS TRABAJO
- Se generó un template base. El resto de los template heradaron la info de dicho template
- Se crearon 3 clases: Marcas, Productos, Locales
- Se creó un formulario para cada una de las clases
- Se generó un formulario para buscar en la base de Productos
- Se trabajó todo generando los commit en GitHub