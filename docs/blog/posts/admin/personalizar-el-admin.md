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
admin.site.index_title = "Bienvenidos al portal de administración" # (3)!
```

1. `site_header`: Título en la parte superior del panel de administración.
2. `site_title`: Título en la pestaña del navegador.
3. `index_title`: Título en la página principal del panel administrativo.

!!! info ""

    No es necesario tocar las plantillas ni hacer ninguna otra modificación, y todo debería funcionar correctamente con estos cambios.

![Panel administrativo, personalizar títulos]({{ get_image_url('assets/images/django-admin-set-titles.webp') }}){:.bordered-image}


### **3. Personalizar la paleta de colores y estilos con CSS**

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

#### **2.Crear y editar un archivo CSS personalizado**

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
```

Para identificar los elementos específicos que desees manipular, abre las **devtools** del navegador y juega con el selector:

![devtools del navegador, para identificar los elementos del panel administrativo]({{ get_image_url('assets/images/django-admin-devtools-css.webp') }}){: .bordered-image }

El panel administrativo de Django utiliza **variables CSS** personalizables para definir una serie de colores y estilos generales. Gracias a esto, puedes sobrescribir los colores del panel de administración sin tener que modificar todo el CSS. Para ver las variables que usa Django, puedes abrir nuevamente las **devtools** del navegador, pero ahora en la pestaña **Source**:

![Cambio de colores con las variables CSS en el panel administrativo]({{ get_image_url('assets/images/django-admin-set-cariables-css.webp') }}){: .bordered-image }

Una vez que hayas elegido el color que deseas cambiar de forma definitiva, abre el archivo CSS y sobrescribe la variable correspondiente. Por ejemplo:

```css title="custom_admin.css"
:root {
    --secondary: #000 !important;
}
```

#### **3. Sobrescribir la Plantilla Base**

Para que Django cargue el archivo CSS creado anteriormente, debes sobrescribir la plantilla base del panel administrativo. Crea un directorio llamado `templates/admin` en la raíz y coloca un archivo llamado `base_site.html`, el contenido lo podemos copiar de la plantilla base de administración de Django.

{% raw %}
```html title="templates/admin/base_site.html" hl_lines="2 4 5 6"
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

Para que el template sea reconocido por Django, debes agregar la ubicación en el archivo `_site/settings.py` del proyecto:

```py title="_site/settings.py" hl_lines="5"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## **Usar Temas de Tercero**

En lugar de escribir CSS desde cero, puedes usar un tema de tercero para darle un toque moderno y atractivo al panel de administración sin necesidad de realizar ajustes complicados.

### **¿Qué es `django-admin-interface`?**

El [**django-admin-interface**](https://pypi.org/project/django-admin-interface/){:target='_blank'} es un paquete para Django que proporciona un tema visualmente atractivo y moderno para el panel de administración. Con él, puedes cambiar fácilmente el estilo de los formularios, tablas, botones y muchos otros elementos del panel administrativo sin tener que personalizar todo el CSS manualmente y es personalizable por el propio administrador. Para configurar este paquete, sigue estos pasos:

#### **Paso 1: Instalar el paquete `django-admin-interface`**

```bash title="terminal"
pip install django-admin-interface
```

#### **Paso 2: Agregar el paquete a la lista de aplicaciones**

```python title="_site/settings.py" hl_lines="2-4"
INSTALLED_APPS = [
    # Agregar django-admin-interface
    'admin_interface',
    'colorfield', # Requerido por django-admin-interface
    # Otras aplicaciones de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

#### **Paso 3: Ejecutar migraciones**

Para que todo funcione correctamente, es necesario ejecutar las migraciones del paquete `django-admin-interface`. Esto configura las tablas necesarias en la base de datos:

```bash title="terminal"
python manage.py migrate
```

!!! info "**¡Importante!**"
    Si has sobrescrito la plantilla `base_site.html`, el tema no se cargará automáticamente. La plantilla personalizada estaría anulando las configuraciones predeterminada de `django-admin-interface`. Para evitar temporalmente esto, renombra la plantilla, por ejemplo de `base_site.html` a `draft_base_site.html`. Si deseas sobrescribir el `base_site.html` usando este paquete, puedes usar [django-apptemplates](https://github.com/bittner/django-apptemplates){:target='_blank'}


Una vez que hayas instalado y configurado `django-admin-interface`, debes volver a entrar al panel de administración y verificar cambios:

![Primera vista con django-admin-interface]({{ get_image_url('assets/images/django-admin-interface-first-view.webp') }}){: .bordered-image }

#### **Paso 4: Sobrescribir base_site.html (Opcional)**

Para poder conservar los títulos que habíamos personalizado con la propiedad `admin.site.site_header`, puedes usar [django-apptemplates](https://github.com/bittner/django-apptemplates){:target='_blank'} y luego en la plantilla `base_site.html` agregar {% raw %}`{% extends "admin_interface:admin/base_site.html" %}`{% endraw %}:

**1. Instala el paquete:**

```bash title="terminal"
pip install django-apptemplates
```

**2. En el archivo `_site/settings.py` añadimos lo siguiente:**

=== "Versiones de Django superior a 1.8"

	```python title="_site/settings.py" hl_lines="9-13"
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR / 'templates',
            ],
            # 'APP_DIRS': True # Comenta esta línea, sino habrá conflicto.
            'OPTIONS': {
                'loaders': [
                    'apptemplates.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
	```

=== "Versiones de Django inferior a 1.8"

	```python title="_site/settings.py"
    TEMPLATE_LOADERS = (
        'apptemplates.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
	```

**3. En el archivo `base_site.html` agregamos lo siguiente:**

{% raw %}
```html title="templates/admin/base_site.html" hl_lines="1"
{% extends "admin_interface:admin/base_site.html" %}
{% load i18n static admin_interface_tags %}
{% block extrahead %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/custom_admin.css' %}">
{% endblock %}
{% block branding %}
{% get_admin_interface_theme as theme %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">
        {% if theme.logo_visible %}
            {% if theme.logo %}
            <img class="logo" style="display:none;" src="{{ theme.logo.url }}" {% if theme.logo.width %}width="{{ theme.logo.width }}"{% endif %} {% if theme.logo.height %}height="{{ theme.logo.height }}"{% endif %}>
            {% else %}
            <img class="logo default" style="display:none;" src="milogo.webp" width="104" height="36">
            {% endif %}
        {% endif %}
        {% if theme.title_visible %}
        <span>{% if 'Django' in theme.title %}{{ site_header|default:_('Django administration') }}{% else %}{% trans theme.title %}{% endif %}</span>
        {% endif %}
    </a>
</h1>
{% endblock %}
```
{% endraw %}

## **Formularios Personalizados**

Puedes crear formularios personalizados para tus modelos


