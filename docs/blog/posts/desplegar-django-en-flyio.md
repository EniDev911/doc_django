---
date: 2024-05-14
title: "Desplegar Django en Fly.io"
---


Desplegar una aplicación de Django en **Fly.io** es un proceso relativamente sencillo, pero requiere seguir varios pasos clave para configurar tanto la aplicación como la infraestructura en **Fly.io**. **Fly.io** es una plataforma que permite desplegar aplicaciones globalmente, ofreciendo facilidad para escalar y administrar aplicaciones en contenedores Docker.

<!-- more -->

## **Preparar la aplicación Django**


De forma predeterminada, Django está configurado para el desarrollo local.


- `BASE_URL` y `ALLOWED_HOSTS`: Agregar los dominios donde estará desplegada la aplicación.
- `BASE_DIR`: Verifica que las rutas y archivos estáticos estén bien configurado.

```py title="_site/setting.py"
APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]
```

En segundo lugar, instalar [Gunicorn](https://gunicorn.org/) como nuestro servidor de producción:

{% set package = "gunicorn" %}
{% include "includes/install-package.html" %}

En tercer lugar, creamos el archivo **requirements.txt** para que enumere todos los paquetes en el entorno virtual de Python:

=== ":octicons-terminal-16: pip"
	```bash
	pip freeze > requirements.txt
	```
=== ":octicons-terminal-16: pipenv"
	```bash
	pipenv requirements > requirements.txt
	```

Hasta aquí, estamos listos para comenzar la implemtación en Fly.io

### **Configurar e implementar la aplicación en Fly**

Para configurar e iniciar la aplicación, ejecutamos el comando `fly launch` y seguimos las instrucciones del asistente:

- **Nombre para la aplicación**: establece el nombre que tendrá la aplicación en Fly.io
- **Región principal**: la región donde actuan los servidores, es detectado automáticamente en la mayoría de los casos.


Esto crea dos nuevos archivos en el proyecto que se configuran automáticamente en un archivo 

- **Archivos estáticos y de media**: Los archivos estáticos y de media, debemos asegurarnos de configurarlos para que se sirvan correctamente en producción, usando servicios como `whitenoise` para servir los archivos estáticos de manera eficiente.


{% set package = "whitenoise" %}
{% include "includes/install-package.html" %}

---

{% set package = "psycopg-binary" %}
{% include "includes/install-package.html" %}

Finalmente para implementar la aplicación utilizamos el siguiente comando:

```bash title="terminal"
fly deploy
```

Esto tardará unos segundos o minutos mientras carga la aplicación:

```bash title="terminal"
Validating ~/project-django/fly.toml
✓ Configuration is valid
--> Verified app config
==> Building image
==> Building image with Depot
--> build:  (​)
[+] Building 16.4s (14/15)   
```