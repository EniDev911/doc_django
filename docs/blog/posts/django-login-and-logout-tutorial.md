---
date: 2024-04-14
---

{% raw %}

# Django login y logout

En este artículo, aprenderemos a configurar el [sistema completo de autenticación de usuarios](https://docs.djangoproject.com/en/5.0/topics/auth/) en Django que consta de inicio de sesión, cierre de sesión, registro, cambio de contraseña y restablecimiento de contraseña.

<!-- more -->

## Crear un proyecto de Django

Con su entorno virtual configurado y activado y Django instalado, ahora puede crear un proyecto:

!!! info "Recuerda"
	Para configurar un entorno virtual y comenzar a trabajar con el framework Django, tienes el capítulo "Comenzar" en este sitio web.

```bash
django-admin startproject django_contrib_auth
```

Al ejecutarse el comando se crea una estructura de carpetas predeterminada, que incluye algunos archivos de Python y su aplicación de administración que tiene el mismo nombre que su proyecto:

```bash
 django_contrib_auth #(1)!
├──  django_contrib_auth #(2)!
│   ├──  __init__.py
│   ├──  asgy.py
│   ├──  settings.py
│   ├──  urls.py
│   └──  wsgy.py
└──  manage.py #(3)!
```

1. Es la carpeta de proyecto de nivel superior.
2. Es la carpeta de nivel inferior que representa su aplicación de administración.
3. Es un script Python que funciona como centro de comando de su proyecto.

Cuando generamos un proyecto predeterminado utilizando el comando `startproject` en Django tenemos habilitado solamente el sitio administrador que lo podemos ver visitando la URL `/admin/` una vez corremos el comando [`runserver`]().

![Página por defecto del sitio administrativo](/assets/images/site-admin-empty.png){style="border: 1px solid #ccc"}

De forma predeterminada, para iniciar sesión en el administrador es necesario que un usuario tenga el atributo `is_staff` en `True` pero no podrá realizar acciones si no tiene los permisos correspondientes para dichas acciones sobre las aplicaciones que se agreguen.

Para poder iniciar sesión, podemos utilizar el comando [`createuser`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-createsuperuser) pero antes debemos correr la migración inicial con el comando [`python manage.py migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#migrate){:target='blank'}. El siguiente ejemplo muestra como crear el superusuario:

=== "bash :octicons-terminal-16:"
	```bash
	python manage.py createsuperuser
	```
=== "output :octicons-terminal-16:"

	```bash
	Username: johndoe
	Email address: johndoe@dummymail.com
	Password:
	Password (again):
	This password is too short. It must contain at least 8 characters.
	This password is too common.
	This password is entirely numeric.
	Bypass password validation and create user anyway? [y/N]: y
	Superuser created successfully.
	```


El módulo `contrib` de Django ofrece aplicaciones integradas para ayudar con el desarrollo. En el archivo `settings.py` buscaremos la lista de `INSTALLED_APPS` y vas a encontrar que `auth` ya se encuentra disponible para nosotros:

=== "settings.py"

	```py hl_lines="3"
	INSTALLED_APPS = [
    	'django.contrib.admin',
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',
	]
	```

=== "explorador"

	```plaintext hl_lines="5"
	 django_contrib_auth
	└──  django_contrib_auth
    	├──  __init__.py
    	├──  asgi.py
    	├──  settings.py
    	├──  urls.py
    	└──  wsgi.py
	```

Para usar la aplicación `auth`, debemos agregarla a nuestro `urls.py` a nivel del proyecto. En la parte superior, importamos `include` y agregamos una nueva URL en `accounts/` ya que este nombre es una práctica estándar y requiere menos personalización más adelante:


=== "urls.py"

	```python hl_lines="2 6"
	from django.contrib import admin
	from django.urls import path, include
	
	urlpatterns = [
		path("admin/", admin.site.urls),
		path("accounts/", include("django.contrib.auth.urls"))
	]
	```

=== "explorador"

	```plaintext hl_lines="6"
	 .
	└──  mysite
    	├──  __init__.py
    	├──  asgi.py
    	├──  settings.py
    	├──  urls.py
    	└──  wsgi.py
	```

La aplicación `auth` nos proporciona multiples [vistas de autenticación](https://docs.djangoproject.com/en/5.0/topics/auth/default/#module-django.contrib.auth.views) y URL para gestionar el inicio de sesión, cierre de sesión, cambio de contraseña, restablecimiento de contraseña, etc. **Notablemente**, no incluye una vista y URL para el registro, por lo que debemos configurarlo nosotros mismos:

|Ruta|Método|Name|Descripción|
|:---|:-----|:---|:----------|
|`accounts/login/`|`GET`|`[name='login']`|Inicio de sesión Login|
|`accounts/logout/`|`GET`|`[name='logout']`|Cierre de sesión Logout|
|`accounts/password_change/`|`GET`|`[name='password_change']`|Cambio de contraseña|
|`accounts/password_change/done/`|`GET`|`[name='password_change_done']`|Página de cambio de contraseña exitoso|
|`accounts/password_reset/`|`GET`|`[name='password_reset']`|Página para resetear la contraseña|


## Página de inicio de sesión

De manera predeterminada. Django buscará dentro de un carpeta `templates` una subcarpeta llamada `registration`. La plantilla de inicio de sesión se llama `login.html`.

Como no hemos creado ninguna aplicación, vamos añadir a la configuración una línea para que se pueda buscar en la raíz del proyecto las plantillas. Buscamos en el archivo `settings.py` la variables `TEMPLATES` y modificamos lo siguiente:

```python title="settings.py" hl_lines="4"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

Luego se crean esas carpetas o directorios y el archivo, nos debe quedar la estructura de carpeta de la siguiente forma:

```plaintext hl_lines="11-13"
 auth_django_sample
├──  auth_django_sample
│   ├──  __init__.py
│   ├──  asgi.py
│   ├──  settings.py
│   ├──  urls.py
│   ├──  views.py
│   └──  wsgi.py
├──  db.sqlite3
├──  manage.py
└──  templates
    └──  registration
        └──  login.html
```

Ahora si añadimos lo siguiente, podemos renderizar la página de inicio de sesión:

```html title="login.html"
<h2>Log In</h2>
<form method="post">
  {% csrf_token %} <!--(1)!-->
  {{ form }} <!--(2)!-->
  <button type="submit">Log In</button>
</form>
```

1. Se añade por cuestiones de seguridad
2. EL contenido del formulario se almacena en `{{ form }}`

Nuestra función de inicio de sesión ahora funciona, pero debemos especificar a dónde redirigir al usuario luego de iniciar sesión correctamente mediante `LOGIN_REDIRECT_URL` en la configuración. En la parte superior del archivo `settings.py` agregamos lo siguiente:

```py hl_lines="4" title="settings.py"
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGIN_REDIRECT_URL = "/"
```

Solo podemos iniciar sesión si tenemos una cuenta de usuario. Y como todavía falta añadir un formulario de registro, el método más sencillo es crear un superusuario desde la línea de comandos.

## Botón de cerrar sesión

Uno de los cambios de Django 5.0, como se indica en las [notas de la versión](https://docs.djangoproject.com/en/5.0/releases/5.0/), es la eliminación de la compatibilidad con el cierre de sesión mediante solicitudes `GET`. En versiones anteriores de Django, se podía agregar un enlace de cierre de sesión como el siguiente ejemplo:

```html title="HTML"
<a href="{% url 'logout' %}">Log Out</a>
```

## Página de registro

Ahora que hemos resuelto el tema de inicio y cierre de sesión, podemos agregar la página de registro al sitio básico de Django. Si recordamos Django no proporciona una vista o URL integrada para esto.

Empecemos abriendo el archivo `views.py` de nuestra app. Luego importamos la clase `UserCreationForm` de la librería `django.contrib.auth.forms`.

```python
from django.contrib.auth.forms import UserCreationForm

def register(requets):
	"""
	Función que registra a a nuevos usuarios en el modelo User
	Args:
		request (HttpRequest object): solicitud HTTP desde el cliente
	Returns:
		HttpResponse:
	"""
```

{% endraw %}
