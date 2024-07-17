---
date: 2024-01-13
---

Recuerda que cada aplicación web que desarrolles, probablemente se va a ejecutar en más de un entorno (tanto locales, como en producción). Y necesitarás cambiar algunos parámetros para que funcione correctamente. Por ejemplo, cuando estas desarrollando localmente necesitas que los parámetros de base de datos estén vinculados a la base de datos local y que el `DEBUG` este en `True`. Pero cuando vas a desplegarlo necesitas cambiar, otra vez, estos parámetros. Cambiar el `DEBUG` a `False` y cambiar los valores de la base de datos.

<!-- more -->

## Crear variables de entorno

Crea un archivo `.env` en la raíz del proyecto. Ahí agregaremos nuestras variables de entorno y añadir el archivo al `.gitignore`

=== ":octicons-file-code-16: `.env`"

	```{ .bash }
	SECRET_KEY=django-in$%..$%...
	DEBUG=True
	DB_NAME=tiendaonline
	DB_USER=postgres
	DB_PASSWORD=post123
	DB_HOST=localhost
	ALLOWED_HOSTS=127.0.0.1, localhost
	```

=== ":octicons-file-code-16: `.gitignore`"

	```{ .bash }
	.env
	```

## Instalación de Python Decouple

Primero se instala la biblioteca con pip:

```bash
pip install python-decouple
```
