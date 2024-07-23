---
icon: material/application-cog-outline
---

Django distingue entre proyectos y aplicaciones. Una aplicación es un paquete de Python con una estructura determinada (modelos, vistas, plantillas, etc). Un proyecto es (además de un paquete de Python) un conjunto de aplicaciones con una configuración común.

## Crear una nueva aplicación

Una vez generado el proyecto con django-admin abrimos la terminal a la altura del archivo `manage.py` y ejecutamos el siguiente comando:

```bash title="bash"
python3 manage.py startapp myapp
```

???+ tree "Explorador"
	```plaintext hl_lines="4-12"
	 .
	├──  db.sqlite3
	├──  manage.py
	├──  myapp
	│   ├──  __init__.py
	│   ├──  admin.py
	│   ├──  apps.py
	│   ├──  migrations
	│   │   └──  __init__.py
	│   ├──  models.py
	│   ├──  tests.py
	│   └──  views.py
	└──  mysite
    	├──  __init__.py
    	├──  asgi.py
    	├──  settings.py
    	├──  urls.py
    	└──  wsgi.py
	```

Luego debemos abrir el archivo `mysite/settings.py` y registrar la app generada:

!!! tree inline end "Explorador"

	```plaintext hl_lines="8"
	 .
	├──  db.sqlite3
	├──  manage.py
	├──  myapp
	└──  mysite
    	├──  __init__.py
    	├──  asgi.py
    	├──  settings.py
    	├──  urls.py
    	└──  wsgi.py
	```
```py title="settings.py" hl_lines="8" linenums="33"
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'myapp'
]
```
