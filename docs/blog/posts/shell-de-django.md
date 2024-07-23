---
date: 2024-05-15
---

El shell de Django nos permite escribir declaraciones de Python desde la línea de comandos para interactuar con el proyecto de Django.

<!-- more -->

!!! tip Django
	El shell de Django es muy potente, pero muchos desarrolladores principiantes subestiman su utilidad en el proceso de desarrollo y depuración.

## ¿Qué es esto de Django Shell?

El __shell de Django__ es una interfaz de línea de comandos interactivo que combina la funcionalidad del framework Django con el shell de Python normal. El shell de Django carga los parámetros y las configuraciones específicas del proyecto, lo que permite aislar el entorno de trabajo y centrarse en el proyecto en particular.

Una de las principales funciones que ofrece este shell es el fácil acceso al mapeador relacional de objetos (ORM), que permite al desarrollador interactuar directamente con la base de datos. El ORM es responsable de realizar consultas a la base de datos dentro de un proyecto de Django. El mapeador relacional de objetos reduce la necesidad de un amplio conocimiento de las bases de datos relacionales y elimina la necesidad de utilizar consultas SQL dentro del proyecto en la mayoría de los casos.

### Accediendo al Shell de Django

Se puede acceder al shell de Django mediante el comando `shell` en un proyecto de Django. Por ende es necesario tener un proyecto Django generado para tener disponible el archivo `manage.py` y ejecutar lo siguiente:

```bash title="bash"
python manage.py shell
```

Vamos a ver que la terminal queda en modo interactivo, invitandonos a escribir nuevas instrucciones:

```title="bash" hl_lines="4 5"
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

Antes de profundizar más en el shell de Django, debemos crear una aplicación para poder definir un modelo y realizar operaciones en la base de datos.

Asumiendo que ya tenemos el proyecto generado, continuemos con aplicación usando el archivo `manage.py`:

```bash
python manage.py startapp fruits
```

Ahora podemos definir un modelo abriendo el archivo `fruits/models.py`:

!!! tree inline end "Explorador"

	```plaintext hl_lines="9"
	 .
	├──  manage.py
	├──  fruits
	│   ├──  __init__.py
	│   ├──  admin.py
	│   ├──  apps.py
	│   ├──  migrations
	│   │   └──  __init__.py
	│   ├──  models.py
	│   ├──  tests.py
	│   └──  views.py
	└──  mysite
	```
```py
from django.db import models

class FruitsInfo(models.Model):

	name = models.CharField(max_length=30)
	origin = models.CharField(max_length=60)
	price = models.DecimalField(max_digits=4, null)
	availabitily = models.IntegerField(default=0)

	def __str__(self):
		return self.origin + " " + self.name
```




