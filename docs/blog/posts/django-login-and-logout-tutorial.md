---
date: 2024-04-14
---

{% raw %}

# Django login y logout

En este artículo, aprenderemos a configurar el [sistema completo de autenticación de usuarios](https://docs.djangoproject.com/en/5.0/topics/auth/) en Django que consta de inicio de sesión, cierre de sesión, registro, cambio de contraseña y restablecimiento de contraseña.

<!-- more -->

El módulo `contrib` de Django ofrece aplicaciones integradas para ayudar con el desarrollo. En el archivo `settings.py` buscaremos la lista de `INSTALLED_APPS` y vas a encontrar que `auth` ya se encuentra disponible para nosotros:


```py hl_lines="3" title="settings.py"
NSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Para usar la aplicación `auth`, debemos agregarla a nuestro `urls.py` a nivel del proyecto. En la parte superior, importamos `include` y agregamos una nueva URL en `account/` ya que este nombre es una práctica estándar y requiere menos personalización más adelante:

```python title="urls.py" hl_lines="2 6"
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path("admin/", admin.site.urls),
	path("accounts/", include("django.contrib.auth.urls"))
]
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

Luego de crear el archivo, añadimos lo siguiente:

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
