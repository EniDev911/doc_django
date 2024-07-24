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

Asumiendo que ya tenemos el proyecto generado, continuamos con la configuración de una aplicación usando el archivo `manage.py`:

```bash title="bash"
python manage.py startapp fruits
```

Ahora podemos definir un modelo abriendo el archivo `fruits/models.py`:


=== "Modelo"
	```py title="fuits/models.py"
	from django.db import models
	
	class FruitsInfo(models.Model):
	
		name = models.CharField(max_length=30)
		origin = models.CharField(max_length=60)
		price = models.DecimalField(max_digits=4, null=False, decimal_places=2)
		availabitily = models.IntegerField(default=0)
	
		def __str__(self):
			return self.origin + " " + self.name
	```

=== "Explorador"
	
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

Luego debemos abrir el archivo `mysite/settings.py` y registrar la app generada:

!!! tree inline end "Explorador"

	```plaintext hl_lines="7"
	 .
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
	'fruits'
]
```


Luego ejecutamos una nueva migración y corremos las migraciones pendientes con el comando `migrate`:

```bash title="bash"
python manage.py makemigrations #(1)!
python manage.py migrate #(2)!
```

1. Genera una nueva migración que incluirá al modelo `FruitsInfo` definido anteriormente.
2. Ejecuta las migraciones pendiente y crea las tablas en la base de datos.

### Insertar datos en la base de datos

En Django, una clase modelo representa una tabla de base de datos y una instancia de esa clase representa un registro particular dentro de la base de datos. Esto es análogo a usar una sentencia [`INSERT` en SQL](https://en.wikipedia.org/wiki/Insert_(SQL)). Se puede crear un registro simplemente instanciando la clase definida en el modelo usando los argumentos de palabras clave definidos para luego llamar al método `save()` y así confirmar el nuevo registro en la base de datos.

En el siguiente ejemplo, veremos que sencillo es agregar un nuevo registro a la clase del modelo:


=== "Python"

	```py  hl_lines="2 3"
	from fruits.models import FruitInfo
	record = FruitsInfo(name="apple", origin="USA", price=2.5, availability=1000)
	record.save()
	record2 = FruitsInfo(name="banana", origin="USA", price=3.63, availability=500)
	record2.save()
	```
=== "Shell"

	```plaintext
	(InteractiveConsole)
	>>> from fruits.models import FruitInfo
	>>> record = FruitsInfo(name="apple", origin="USA", price=2.5, availability=1000)
	>>> record1.save()
	>>> record2 = FruitsInfo(name="banana", origin="USA", price=3.63, availability=500)
	>>> record2.save()
	```

!!! info "Nota"
	Si no recibimos mensajes de errores indicados en la consola de Django, podemos suponer que el registro se agregó correctamente

Otra forma de insertar un registro en una clase modelo es usar el método `create()`. Esto elimina la necesidad de llamar al método `save()` para confirmar el registro en la base de datos;

=== "Python"

	```py  hl_lines="1"
	FruitsInfo.objects.create(name="pineapple", origin="USA", price=2.2, availabitily=50)
	```
=== "Shell"

	```plaintext  hl_lines="2"
	(InteractiveConsole)
	>>> FruitsInfo.objects.create(name="pineapple", origin="USA", price=2.2, availabitily=50)
	<FruitsInfo: USA pineapple>
	```

### Mostrar registros

Verificaremos esto utilizando el método `all()`. El `QuerySet` que nos retorna el método `all()` describe todos los objetos de la tabla en la base de datos:

=== "Python"

	```py  hl_lines="1"
	FruitsInfo.objects.all()
	```
=== "Shell"

	```plaintext  hl_lines="2"
	(InteractiveConsole)
	>>> FruitsInfo.objects.all()
	<QuerySet [<FruitsInfo: USA apple>, <FruitsInfo: USA banana>]>
	```

Debido a que hemos definido un método `__str__()` para mostrar un objeto en un formato legible para nosotros los humanos 😎, el método `all()` mostrará solo el valor definido en el método `__str__()`.

El método `values()` permite extraer los valores de un objeto determinado como se muestra a continuación:

=== "Python"

	```py  hl_lines="1"
	FruitsInfo.objects.all().values()
	```
=== "Shell"

	```plaintext  hl_lines="2"
	(InteractiveConsole)
	>>> FruitsInfo.objects.all(),values()
	<QuerySet [{'id': 1, 'name': 'apple', 'origin': 'USA', 'price': Decimal('3.50'), 'availabitily': 0}, {'id': 2, 'name': 'banana', 'origin': 'USA', 'price': Decimal('3.50'), 'availabitily': 40}, {'id': 3, 'name': 'pineapple', 'origin': 'USA', 'price': Decimal('2.20'), 'availabitily': 50}]>
	```

### Insertar múltiples registros

Ahora veremos cómo insertar varios registros en una clase específica. Creamos una nueva clase `FruitsVendor` dentro de `models.py` en la aplicación:

```py title="models.py"
class FruitsVendor(models.Model):

	vendor_id = models.CharField(max_length=4, null=False, primary_key=True)
	vendor_name = models.CharField(max_length=60)
	vendor_location = models.CharField(max_length=40)

	def __str___(self):
		return f"{self.vendor_id} - {self.vendor_name} - {self.vendor_location}"
```

En la nueva clase `FruitsVendors`, hemos definido un campo con llave primaria llamado `vendor_id`. Luego, definimos el método `__str__()` para mostrar todos los datos dentro de la clase en una cadena con formato.

Generamos una nueva migración y las ejecutamos con el comando `migrate`:

=== "Migraciones"

	```bash title="bash"
	python manage.py makemigrations
	python manage.py migrate
	```

=== "Salida"

	```plaintext
	Migrations for 'fruits':
  	fruits/migrations/0002_fruitsvendor.py
    	- Create model FruitsVendor
	Operations to perform:
  	Apply all migrations: admin, auth, contenttypes, fruits, sessions
	Running migrations:
  	Applying fruits.0002_fruitsvendor... OK
	```

Ahora podemos volver al shell e insertar múltiples registros en la clase `FluitsVendors` a la vez usando el método `bulk_create()` y el shell de Django:

=== "Python"

	```py hl_lines="6"
	from fruits.models import FruitsVendor
	
	fruit_vendor1 = FruitsVendor(vendor_id="V001", vendor_name="Fresh Fruits", vendor_location = "New York")
	fruit_vendor2 = FruitsVendor(vendor_id="V002", vendor_name="Direct Delivery", vendor_location = "Sao Paulo")
	fruit_vendor3 = FruitsVendor(vendor_id="V003", vendor_name="Fruit Mate", vendor_location = "Sydney")
	FruitsVendor.objects.bulk_create([fruit_vendor1, fruit_vendor2, fruit_vendor3])
	```

=== "Django shell"

	```plaintext
	>>> from fruits.models import FruitsVendor
	>>> fruit_vendor1 = FruitsVendor(vendor_id="V001", vendor_name="Fresh Fruits", vendor_location = "New York")
	>>> fruit_vendor2 = FruitsVendor(vendor_id="V002", vendor_name="Direct Delivery", vendor_location = "Sao Paulo")
	>>> fruit_vendor3 = FruitsVendor(vendor_id="V003", vendor_name="Fruit Mate", vendor_location = "Sydney")
	>>> FruitsVendor.objects.bulk_create([fruit_vendor1, fruit_vendor2, fruit_vendor3])
	[<FruitsVendor: FruitsVendor object (V001)>, <FruitsVendor: FruitsVendor object (V002)>, <FruitsVendor: FruitsVendor object (V003)>]
	```

Ahora si pensamos en insertar registros a partir de otro módulo de python, tendríamos que solo crear ese archivo en la raíz del proyecto o en una subcarpeta de ejemplo y agregar todas las instrucciones anteriores para luego importar el módulo en la sesión interactiva en el shell, aunque hay formas mejores de hacer la carga de datos a partir de archivos externos, no tiene desperdicio estar en conocimiento.

### Obtener un solo registro - get()

Si quisieramos recuperar un solo registro, podemos usar el método `get()`. Sin embargo, si hay más de un registro que coincida con la consulta que especificamos dentro del método `get()`, esto dará como resultado un error `MultipleObjectsReturned`.

El método `get()` es más viable cuando buscamos utilizando campos con índices únicos, como llave primaria. El siguiente ejemplo muestra el método `get()` utilizando el campo **id**:

=== "Python"

	```python
	from fruits.models import FruitsInfo
	FruitsInfo.objects.get(id=3)
	```
=== "Shell"

	```plaintext
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.get(id=3)
	<FruitsInfo: USA pineapple>
	```
