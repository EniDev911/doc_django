# Crear un nuevo proyecto

Una vez tenemos a nuestra disposición Django, se nos habilitará un script para la gestión de proyectos.

Desde la línea de comando, nos vamos al directorio donde vamos a trabajar y usamos el script `django-admin` de la siguiente manera para crear un nuevo proyecto:

```shell
django-admin startproject mi-proyecto-django
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
