---
date: 2024-08-14
title: Personalizar el Panel Administrativo de Django
---

Una de las características de Django es que cuenta con un panel de administración listo para usarse, con funciones básicas como crear, leer, editar y eliminar modelos, usuarios, grupos y permisos. Todo listo con tan solo generar un nuevo proyecto. Pero a menudo se desea modificar su apariencia, las vistas de los modelos o incluso la funcionalidad para que se ajuste a las necesidades del proyecto.

<!-- more -->

## **Accediendo al Panel Administrativo de Django**

Antes de acceder al panel administrativo, debemos contar con un proyecto de Django. Para ello debemos seguir los siguientes pasos:

{% set project = "custom-admin-django" %}
{% include "includes/new-project.html" %}

Ahora tenemos que ejecutar el servidor de desarrollo con el comando `python manage.py runserver` y visitamos la URL <http://127.0.0.1:8000/>:

=== "Comando"
    ```bash title="terminal"
    python manage.py runserver 8080
    ```
=== "Salida"
    ```plaintext hl_lines="1 11"
    $ python manage.py runserver 8080
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    January 09, 2025 - 23:41:14
    Django version 5.1.4, using settings '_site.settings'
    Starting development server at http://127.0.0.1:8080/
    Quit the server with CONTROL-C.
    ```

Como resultado al abrir la URL, veremos la página por defecto de Django:

![Página por defecto de Django](/assets/images/django-project-start.png){style="border: 1px solid #ccc"}

Sin hacer nada más, podemos ir a <http://127.0.0.1:8080/admin> y veremos la página de login:

![Página de login de Django admin](/assets/images/django-admin-login.png){style="border: 1px solid #ccc"}

Todo esto se debe que un proyecto creado con el comando `startproject` ya viene correctamente configurado y trae habilitado el panel administrativo. Significa que ya trae las aplicaciones `django.contrib.admin`, `django.contrib.auth`, y `django.contrib.contenttypes` por defecto en el archivo `settings.py`:

```py title="settings.py"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Otras aplicaciones
]
```

Y también vienen ya configurada las URLs de administración en el archivo `urls.py` en el proyecto:

```py title="urls.py" hl_lines="5"
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Hasta ahora solo hemos podido visualizar la página de login, pero para acceder tenemos que ejecutar las migraciones y luego crear a un **superusuario** administrador.

**Ejecutar Migraciones**

```bash title="terminal"
python manage.py migrate
```

**Crear superusuario**

```bash title="terminal"
DJANGO_SUPERUSER_PASSWORD=123456 python manage.py createsuperuser --username=admin --email=admin@example.com --noinput
```

???+ info
    El comando anterior permite la creación desatendida del superusuario para ingresar como al panel administrativo.

Ahora podemos iniciar sesión con el superusuario en el panel adminsitrativo y al iniciar la sesión se nos muestra la siguinte interfaz:
    
![Página de login de Django admin](/assets/images/django-admin-login-success.png){style="border: 1px solid #ccc"}

De forma predeterminada, Django incluye los modelos **Users** y **Groups**


El diseño de la interfaz administrativa de Django es bastante básico por defecto, pero se puede personalizar fácilmente para ajustarse a la identidad visual de tu proyecto.