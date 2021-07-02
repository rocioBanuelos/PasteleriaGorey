# Proyecto final de programación para internet D13

## Nombre del Proyecto: **Pastelería Gorey**

### Objetivo del Proyecto
Crear una página para la Pastelería Gorey, donde los usuarios puedan ver y seleccionar los productos, añadiendo los deseados
a un carrito de compras, que posteriormente al intentar comprarlo, permite al cliente registrar su nombre y correo para después mostrar un resumen del pedido, simular un pago con tarjeta y enviar un correo al usuario donde se describe el pedido realizado.

También permite mediante un formulario de contacto recibir las dudas de los clientes.

Y por último que permita al administrador iniciar sesión, editar, crear y eliminar diferentes aspectos y ver el apartado de "Pedidos" donde se muestra a detalle todos los pedidos realizados en el sitio web.

### Integrante: Rocio Bañuelos

### Framework utilizado: Django

## Intrucciones de Instalación

Para instalar este proyecto se requiere tener instalado en el equipo:

* Python 3.7 o superior
* Pip 20 o superior
* MySQL 4.3 o superior
* PHPMyAdmin (opcional)

Para comenzar con la instalación ejecute los siguientes pasos:

1. Descargue el repositorio en su equipo
1. Dentro de MYSQL cree una Base de Datos con el nombre 'gorey', deberá estar en codificación UTF-8. Sólo es necesario crear la BD, las tablas se generan automáticamente con Django. 
1. Cree un usuario de BD que tenga permisos totales sobre la base de datos recien creada.
1. Abra una terminal dentro del proyecto en el mismo directorio que se encuentra este instructivo y el archivo `manage.py`
1. Instale los paquetes necesarios con el comando:
    ```python
        pip install django, mysqlclient, django-mathfilters
    ```
1. Acceda al archivo `settings.py` dentro del directorio Proyecto/gorey/settings.py
1. Dentro de `settings.py` busque el apartado DATABASES y reemplace la información existente con los datos de la BD y el usuario creados para el proyecto, al terminar, guarde los cambios en el archivo
1. Ahora puede crear las migraciones mediante el comando:
    ```python
        python manage.py makemigrations
    ```
1. Despues deberá ejecutar estas migraciones
    ```python
        python manage.py migrate
    ```
1. El paso anterior crea todas las tablas necesarias para la BD, pero se necesitan cargar algunos catalagos:

    En la carpeta bd en este proyecto, se encuentran 3 archivos .sql 
    
    Estos se necesitan importar a la tabla correspondiente, en el siguiente orden:

    1. El archivo cake.sql se debe importar a la tabla cake.
    1. El archivo type_of_product.sql se debe importar a la tabla type of product
    1. El archivo product.sql se debe importar a la tabla product. 


1. Ahora deberá crear el usuario administrador del sistema, esto se hace mediante el comando:
    ```python
        python manage.py createsuperuser
    ```

    Esta operación pedira un username, email y contraseña. Este paso es importante porque desde la sección del sitio web Administrador podra ingresar sesión con este usuario y contraseña.
1. Finalmente, para ejecutar el servidor utilice el comando:
    ```python
        python manage.py runserver
    ```
    El servidor se debe ejecutar en la dirección `127.0.0.1:8000`

1. Cabe destacar algunos aspectos:
    1. En la sección del sitio web Administrador se podrá iniciar sesión con el username y contraseña creados en el paso 11. En esta sección se pueden modificar la información de la base de datos. 
    2. Con la sesión iniciada si accede a `127.0.0.1:8000` nuevamente o recarga la página aparecerá un nuevo menú con la opción Pedidos, sólo disponible para el administrador.

*Nota:* El correo que se encuentra en el proyecto es únicamente de pruebas, por si lo desea utilizar. 