# Playground

## URL DE LA PAGINA:
http://127.0.0.1:8000/App
http://127.0.0.1:800/admin

## LINK AL VIDEO EXPLICATIVO:
https://drive.google.com/file/d/1mYXzb2lUsM_kXzMZHYYjhVl94k7YW44H/view?usp=sharing

## OBJETIVO
Crear una página que nuclee varios comercios de venta de celulares. En ella los comercios pueden indicar cuáles son las marcas con las que trabajan y los productos con los que cuentan. Los usuarios, que son los vendedores, pueden acceder y ver los productos, las marcas y los locales.
Quienes ingresen con nombre de usuario y contraseña, pueden editar los nuevos productos.

## FUNCIONAMIENTO
Los comercios pueden ingresar a la página, ver qué marcas tienen, cuáles son los productos que están vendiendo y su stock, así como también y los comercios que forman parte de estar red.

## FUNCIONALIDADES
###### STORES
*	Stores: Se puede observar el nombre de fantasía del local, la ciudad donde está, la dirección, el número de local y los días de atención.
*	Add a new store: Esto permite generar un nuevo comercio. Al hacerlo, se pide llenar un formulario, indicando el nombre del local, la localidad, la dirección, el número de local y los horarios de atención.
*	Search for a store: Se puede buscar un local y va a figurar toda la información del mismo. Además, en esta página, se puede elegir volver a la sección “Malls”.

###### SALESMAN
*	Salesman: Se puede observar el nombre y apellido del vendedor, así como su e-mail, fecha de nacimiento y el local donde trabaja.
*	Add a new salesman: Esto permite añadir un nuevo vendedor. Al hacerlo, se pide llenar un formulario, en el que se debe completar el número del local en el cual trabaja, el nombre, apellido, email y fecha de nacimiento.
*	Edit a new salesman: En esta vista se muestra el listado de vendedores y se puede editar alguno de ellos o eliminarlo.

###### PRODUCTS
*	Products: En esta opción se puede observar toda la información del producto y en la columna final figura si el producto tiene stock disponible, quedan pocas unidades o está agotado. Esto se generó con un if en el html de productos. El color de la palabra también sirve de indicador del nivel de stock disponible
*	Add a new product: Esto permite crear un nuevo producto. Al hacerlo, se pide llenar un formulario, en el que se debe completar el nombre del producto, el precio, en un desplegable para seleccionar la marca y el stock disponible. Además, en esta página, se puede elegir volver a la sección “Products”.
*	Search for a product: Se puede buscar un producto específico, para ver, por ejemplo, si queda stock disponible. Además, en esta página, se puede elegir volver a la sección “Products”.
*	Product description: En esta sección se pueden ver las principales características de los productos que están en venta. Además, se agregó un botón para volver a la sección principal de productos.

###### WHAT’S NEW?
Esta sección solo es visible cuando el usuario está logueado, es decir, para poder agregar, modificar o eliminar un nuevo producto, que aún no salió a la venta, el usuario debe estar registrado. 
*	New products: después de haber ingresado su usuario y contraseña, verá un listado de productos nuevos, que aún no están a la venta, con datos del nombre del producto. 
*	Update: haciendo click, podrá editar un producto
*	Delete: haciendo click, podrá eliminar un producto
*	New: puede agregar nuevos productos.

###### LOG IN
Como se mencionó antes, para acceder al botón de nuevos productos, el usuario debe ingresar un nombre de usuario y una contraseña. 
*	Log In: Si tiene usuario y contraseña ya creado, los ingresa y luego de registrarse, se deriva a la página principal donde un mensaje de bienvenida lo espera (un Emoji en forma de estrella y un Welcome). 
Cuando está conectado como usuario, el botón del “Log in” no es más visible, y ahora aparecen tres botones adicionales:
-	What’s new?
-	Log out
-	Edit profil
Al mismo tiempo, cuando no está conectado, estos tres botones desaparecen y solo se puede ver el botón Log In.
*	Register: si no está registrado, debe hacerlo, completando un formulario en el que se le piden los datos personales (nombre de usuario, email, contraseña, repetir contraseña, apellido y nombre)

###### LOG OUT
Si el usuario está registrado, entonces aparece un botón arriba a la derecha, donde puede cerrar su sesión.
Cuando hace click en el enlace, se cierra la sesión y lo lleva a una vista en la que le dice que está desconectado (se agregó un Emoji de una mano saludando) y le da la opción de volverse a conectar.

###### EDIT PROFILE
Si el usuario está registrado, abajo del link al “Log out”, aparece otro link, al final de la hoja, donde puede editar su usuario.
Cuando hace click en el enlace, se abrirá una página en donde podrá cambiar su email y su contraseña.

###### ABOUT US
En la última parte de página de inicio, hay un link que se llama “About us”. Haciendo click en el mismo, se podrá llegar a una página, con los datos de las personas que hicieron la aplicación.
El trabajo lo hicimos entre Felipe Aramburu García y Carolina Swoboda. Hicimos el trabajo en conjunto, definimos la idea de página web y le fuimos agregando y cambiando puntos, hasta llegar a esta versión, que es la que hoy presentamos.

## CONSIGNAS DEL TRABAJO
*	Se generó un template base. El resto de los templates heradaron la información de dicho template
*	Se crearon 4 clases: Vendedores, Productos, Locales y Nuevos Productos
*	Se creó un formulario para cada una de las clases
*	Además, se generó un formulario para buscar en la base de Locales y de Productos
*	Se generó un acceso visible a la vista de "About us"
*	Cuenta con un log in, log out y editar perfil
*	Tiene contenido tipo blog, en la sección “Products description” ya que ahí se cuenta con información de cada uno de los productos que están a la venta
*	Tiene aplicado el CRUD (Create, Retrieve, Update, Delete) en funciones basadas en vistas
*	Cuenta con un admin en route admin/ donde se pueden manejar las apps y los datos en las mismas
*	En la parte superior de la web, en la pestaña, al lado del ícono, se muestra el nombre de la página que se está viendo (es decir, va cambiando el nombre según la vista)
*	Se trabajó todo generando el commit en GitHub
######	NOTAS: 
-	cada botón que se agregó en las páginas, para ir de una vista a otra, es un botón editado y diferente, según lo que se desee hacer
-	los links en las vistas de agregar nuevo producto tienen un color diferente, según lo que se desea hacer: 
-  para más información (“More info”), se eligió el celeste
     -  para editar (“Update”), el amarillo
     -  para eliminar (“Delete”), el rojo
     -  para agregar un nuevo producto (“Add a new product”), el verde
-	se agregaron Emojis en algunas vistas
-	se trabajó un poco en la estética también
######	PRÓXIMOS PASOS:
-	publicar la página web en un host que no sea el local
