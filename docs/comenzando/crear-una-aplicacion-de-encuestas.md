# Crea tu primera aplicación con Django

Aquí vamos realizar una aplicación que está basada en un artículo de la documentación de Django; [Escribiendo su primera aplicación en Django](https://docs.djangoproject.com/en/5.0/intro/){:target='_blank'}, la diferencia es que aquí se incluyen otros temas relacionados como la configuración de un entorno de desarrollo y conceptos que serán de mucha ayuda para el entendimiento a lo largo del tutorial.


## Puesta en marcha de un entorno de desarrollo

Cuando instalamos [Python3](https://www.python.org/){:target='blank'} obtenemos un único entorno global que es compartido por todos los proyectos y todo el código de Python. Si bien podríamos instalar **Django** y otros paquetes en el entorno global. Sin embargo sólo puedes instalar una versión en particular de cada paquete.

???+ note "Nota"

    Las aplicaciones Python instaladas en el entorno global pueden entrar en conflicto potencialmente unas con otras (Ej. si dependen de diferentes versiones del mismo paquete).

Si instalamos Django dentro del entorno por defecto/global sólo podrás apuntar a una sóla versión de Django en la computadora. Esto puede ser un problema si quieres crear en el futuro nuevos sitios (usando las útilmas versiones de Django) pero manteniendo los sitios web que dependen de versiones más antiguas.

Como resultado, los desarrolladores experimentados en Python/Django normalmente configuran y ejecutan las aplicaciones Python dentro de [entornos virtuales Python](https://docs.python.org/es/3/tutorial/venv.html){:target='blank'} independientes.


<script src="https://kit.fontawesome.com/6b8f0c7049.js" crossorigin="anonymous"></script>


<div style="text-align:center">
```mermaid
graph TD
    B("<img src='https://w7.pngwing.com/pngs/234/329/png-transparent-python-logo-thumbnail.png'; width='30' align='center'/><br>Python 3.9")
    B-->C("<img src='https://w7.pngwing.com/pngs/234/329/png-transparent-python-logo-thumbnail.png'; width='30' align='center'/><br>Python 3.6")
    B-->D("<img src='https://w7.pngwing.com/pngs/234/329/png-transparent-python-logo-thumbnail.png'; width='30' align='center'/><br>Python 3.7")
    B-->E("<img src='https://w7.pngwing.com/pngs/234/329/png-transparent-python-logo-thumbnail.png'; width='30' align='center'/><br>Python 3.8")
```
</div>

## Crear un nuevo proyecto

Una vez tenemos a nuestra disposición Django, se nos habilitará un script para la gestión de proyectos.

Desde la línea de comando, nos vamos al directorio donde vamos a trabajar y usamos el script `django-admin` de la siguiente manera para crear un nuevo proyecto:

```shell
django-admin startproject misitio
```

## Ejecutar el servidor de desarrollo

Para verificar que nuestro proyecto funcione. Cambiamos al directorio del proyecto generado, y dentro ejecutamos el siguiente comando:

```shell
python manage.py runserver
```

???+ note "Nota"

    De forma predeterminada, cuando lanzamos el servidor de desarrollo se utiliza el puerto 8000.

    Si deseamos cambiar el puerto del servidor, lo pasamos como argumento al comando `runserver`:

    ```shell
    python manage.py runserver 8080
    ```

???+ abstract "Recarga automática"

    El servidor de desarrollo recarga automáticamente el código Python para cada solicitud según sea necesario. Sin embargo, algunas cosas como agregar nuevos archivos no activan el reinicio, por lo que tendríamos que reiniciar el servidor.

---

## Crear una aplicación

Cada aplicación que se crea en Django consta de un paquete Python que sigue una determinada convención. Django incluye una utilidad que crea automáticamente la estructura básica de una aplicación.

???+ abstract "Diferencia entre Proyecto y Aplicación"
    Una aplicación es una aplicación web que sirve para algo (Ej: Blog, aplicación de encuestas, etc.).

    Un proyecto es una colección de aplicaciones para un sitio web en particular.

Para crear una aplicación, desde la línea de comandos ejecutamos lo siguiente (asegúrate de estar en el mismo directorio que el script `manage.py`):

```
python manage.py startapp encuestas
```

---

## Definir una primera vista

Abrimos el archivo **encuestas/views.py**

=== ":octicons-file-code-16: `encuestas/views.py`"

    ```{ .python  }
    from django.http import HttpResponse


    def index(request):
        return HttpResponse("Hola mundo.")
    ```

    
Estamos remplazando el contenido del archivo para ver el tipo de vista más simple en Django. Para poder llamar a la vista y mostrarla, se requiere asignarla a una URL.


Para ello creamos un nuevo archivo dentro del directorio **encuestas** llamado `urls.py`:

=== "Linux - Bash"

    ```shell
    touch encuestas/urls.py
    ```
=== "Windows - CMD"

    ```bat
    type nul > encuestas/urls.py
    ```
Luego abrimos ese archivo creado para incluir el siguiente código:

=== ":octicons-file-code-16: `encuestas/urls.py`"

    ```{ .python  }
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```

Cumplido lo anterior, el siguiente paso es configurar el **URLconf** raíz para añadir el módulo `encuestas.urls`.

Ahora en el archivo `misitio_django/urls.py` lo añadimos de la siguiente forma:

=== ":octicons-file-code-16: `misitio/urls.py`"

    ```py hl_lines="5"
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("encuestas/", include("encuestas.urls")),
        path("admin/", admin.site.urls),
    ]
    ```