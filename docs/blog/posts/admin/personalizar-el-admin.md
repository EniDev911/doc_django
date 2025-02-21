---
date: 2024-08-14
title: Personalizar el Panel Administrativo de Django
tags: ["admin", "customizar"]
---

Django es conocido por su rapidez en el desarrollo y su potente sistema de administración listo para usarse. Desde el momento en que creas un nuevo proyecto con Django, el panel de administración se configura automáticamente, ofreciendo una interfaz para gestionar modelos, usuarios, permisos y mucho más. Sin embargo, es común que, a medida que avanzamos en el desarrollo de nuestra aplicación, necesitemos personalizar este panel para adaptarlo a las necesidades específicas de nuestro proyecto. Afortunadamente, Django facilita esta personalización tanto en términos de apariencia como de funcionalidad.

<!-- more -->

## **Prepararando el Escenario**

Antes de acceder al panel administrativo, debemos contar con un proyecto de Django. Para ello debemos seguir los siguientes pasos:

{% set project = "custom-admin-django" %}
{% include "includes/new-project.html" %}

## **Configurar el Panel Administrativo**

Una vez que hayas creado tu proyecto, Django ya incluye un panel administrativo listo para usarse, pero para poder acceder a él debes asegurarte de haber realizado algunos pasos previos:

### **1. Ejecutar Migraciones**


```bash title="terminal"
python manage.py migrate
```

### **2. Crear un superusuario**

El superusuario es el usuario con privilegios administrativos que podrás utilizar para iniciar sesión en el panel. Para crear uno, ejecuta el siguiente comando:

```bash title="terminal"
python manage.py createsuperuser
```

### **3. Iniciar el servidor**

Ahora debemos ejecutar el servidor de desarrollo con el comando `python manage.py runserver`:

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

???+ info
    El comando anterior lanza el servidor de desarrollo en el puerto 8080.

## **Acceder al Panel de Administración**

Una vez que el servidor esté en funcionamiento, puedes abrir la URL <http://127.0.0.1:8080/> y se mostrará la página predeterminada de Django:

![Página por defecto de Django]({{ get_image_url('assets/images/django-project-start.webp') }}){:.bordered-image}

Sin realizar ningún otro paso, podemos acceder a <http://127.0.0.1:8080/admin> y se mostrará la página de iniciar sesión del panel de administración:

![Página de login de Django admin]({{ get_image_url('assets/images/django-admin-login.webp') }}){:.bordered-image}

Esto se debe a que un proyecto creado con el comando `startproject` ya viene correctamente configurado y tiene habilitado el panel administrativo. Esto implica que las aplicaciones `django.contrib.admin`, `django.contrib.auth` y `django.contrib.contenttypes` están habilitadas por defecto en el archivo `settings.py`:

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

Ahora podemos acceder al panel administrativo iniciando sesión con el superusuario. Al hacerlo, se nos mostrará la siguiente interfaz:
    
![Página de login de Django admin]({{ get_image_url('assets/images/django-admin-login-success.png') }}){:.bordered-image}

De forma predeterminada, Django incluye los modelos **Users** y **Groups** como parte de su sistema de autenticación y autorización. Estos modelos están definidos en la aplicación `django.contrib.auth`, que es una de las aplicaciones incluidas de forma predeterminada en la configuración de Django.

## **Personalización Básica**

### **1. Cambiar el Idioma del Panel Administrativo**

Django viene con soporte para múltiples idiomas. En nuestro caso si deseamos cambiar el idioma del panel administrativo al español, debemos realizar los siguientes pasos:

1. **Abrir el archivo `_site/settings.py`**.
2. **Configurar el idioma**. En el archivo settings.py, encontrarás la opción `LANGUAGE_CODE`. Aquí puedes especificar el idioma que deseas utilizar en el panel administrativo.

Por ejemplo, para cambiar el idioma a **español (Chile)**, debes establecer `LANGUAGE_CODE` a `'es-cl'`:

```python title="settings.py" linenums="106"
LANGUAGE_CODE = 'es-cl'
```

Ahora, cuando accedes al panel administrativo, deberías ver todos los textos traducidos al idioma que has configurado. Esto incluye todas las etiquetas de los formularios, menús y otros elementos del panel.

![Panel administrativo, en español]({{ get_image_url('assets/images/django-admin-es-cl.webp') }}){:.bordered-image}

### **2. Personalizar el título del panel administrativo**

Puedes cambiar el título del panel administrativo (que aparece en la parte superior) para que coincida con el nombre de tu proyecto o tu marca. Esto se puede hacer editado el archivo `_site/urls.py` o en un archivo de configuración similar, utilizando las propiedades e `admin.site`:

```py title="urls.py" hl_lines="8 9 10"
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Mi sitio web" # (1)!
admin.site.site_title = "Portal de mi web" # (2)!
admin.site.index_title = "Bienvenidos al portal de administración"
```

1. `site_header`: Título en la parte superior del panel de administración.
2. `site_title`: Título en la pestaña del navegador.

![Panel administrativo, personalizar títulos]({{ get_image_url('assets/images/django-admin-set-titles.webp') }}){:.bordered-image}

### **3. Cambiar Estilos con CSS Pesonalizado**

Aunque el panel de administración de Django es funcional desde el principio, su apariencia es bastante simple. Si deseas darle un toque más personalizado, puedes hacerlo de varias maneras, desde cambiar los estilos CSS hasta usar un tema de terceros.

Para cambiar estilos con CSS personalizado, sigue estos pasos:

#### **1. Configurar los archivos estáticos**

Django proporciona configuraciones específicas para gestionar los archivos estáticos. Vamos a configurarlos correctamente. En el archivo `_site/settings.py`, asegúrate de tener las siguientes configuraciones para los archivos estáticos:

```py title="setting.py"  linenums="119"
# Directorio donde se encuentran los archivos estáticos en desarrollo
STATIC_URL = '/static/'

# En desarrollo, Django sirve archivos estáticos desde la carpeta definida aquí
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Carpeta en la que se almacenarán los archivos estáticos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# en producción se utiliza el comando `python manage.py collectstatic` para recopilar todos los archivos estáticos.
```

#### **2.Crear el archivo CSS**

Crea un archivo CSS en el directorio estático de tu proyecto, en nuestro caso en la raíz en un directorio `static/css/custom_admin.css`. Dentro de este archivo, puedes añadir los estilos que desees para modificar la apariencia del panel. Ejemplo:


```css title="custom_admin.css"
body {
    background-color: #f4f4f4;
}

#content-main {
    background-color: #fff;
    border-radius: 8px;
    padding: 20px;
}

.module h2 {
    color: #1e73be;
}
```

Para identificar los elementos que deseas manipular, abre las **devtools** del navegador:

![devtools del navegador, para identificar los elementos del panel administrativo]({{ get_image_url('assets/images/django-admin-devtools-css.webp') }}){: .bordered-image }

#### **3. Sobrescribir la Plantilla Base**

Para que Django cargue el archivo CSS creado anteriormente, debes sobrescribir la plantilla base del panel administrativo. Crea un directorio llamado `templates/admin` en la raíz y coloca un archivo llamado `base_site.html`, el contenido lo podemos copiar de la plantilla base de administración de Django.

{% raw %}
```html title="templates/admin/base_site.html" hl_lines="2 5"
{% extends "admin/base.html" %}
{% load static %} <!-- (1)! -->

{% block extrahead %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/custom_admin.css' %}">
{% endblock %}


{% block title %}{% if subtitle %}{{ subtitle }} | {% endif %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></div>
{% if user.is_anonymous %}
  {% include "admin/color_theme_toggle.html" %}
{% endif %}
{% endblock %}
```

1. Esto es un tag de Django que se utiliza para cargar la funcionalidad que Django pueda cargar correctamente el tag `{% static %}`.
{% endraw %}


### **Crear un modelo personalizado que replique la funcionalidad del modelo Group**

Podemos crear un modelo de ejemplo llamado `Comite` que funcione de manera similar a `Group`, y luego asociarlo con los usuarios. Esto nos permite personalizar completamente el comportamiento y los nombres en nuestra aplicación, sin alterar el comportamiento de la aplicación de autenticación predeterminada.

```py title="myapp/models.py"
from django.contrib.auth.models import User, Permission
from django.db import models

class Comite(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
```

#### **Crear una relación muchos a muchos con User**

Luego, añadimos un campo de relación muchos a muchos en el modelo `User` que vincule a los usuarios con los comités, al igual que se hace con el modelo `Group` de manera predeterminada. Una opción es **extender el modelo** `User` y crear un modelo llamado por ejemplo `Profile` que este relacionado con `User`, y dentro de este agregar el campo de relación `Comite`:

```py title="myapp/models.py"
from django.contrib.auth.models import User
from django.db import models
from .models import Comite  # Asegúrate de importar el modelo Comite

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comites = models.ManyToManyField(Comite, related_name="miembros", blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
```

## **Usar Temas de Tercero**

## **Formularios Personalizados**

Puedes crear formularios personalizados para tus modelos


