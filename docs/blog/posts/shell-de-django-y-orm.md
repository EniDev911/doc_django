---
date: 2024-05-15
title: Shell de Django, ORM y QuerySets
---

El shell de Django nos permite escribir declaraciones de Python desde la línea de comandos para interactuar con el proyecto de Django.

<!-- more -->

!!! tip Django
	El shell de Django es muy potente, pero muchos desarrolladores principiantes subestiman su utilidad en el proceso de desarrollo y depuración.

## **¿Qué es esto de Django Shell?**

El __shell de Django__ es una interfaz de línea de comandos interactivo que combina la funcionalidad del framework Django con el shell de Python, iPython, bPython (estos dos últimos, se deben instalar por aparte en la mayoría de los casos). El shell de Django carga los parámetros y las configuraciones específicas del proyecto, lo que permite aislar el entorno de trabajo y centrarse en el proyecto en particular.

Una de las principales funciones que ofrece este shell es el fácil acceso al mapeador relacional de objetos (ORM), que permite al desarrollador interactuar directamente con la base de datos. El ORM es responsable de realizar consultas a la base de datos dentro de un proyecto de Django. El mapeador relacional de objetos reduce la necesidad de un amplio conocimiento de las bases de datos relacionales y elimina la necesidad de utilizar consultas SQL dentro del proyecto en la mayoría de los casos.

## **Accediendo al Shell de Django**

Se puede acceder al shell de Django mediante el comando `shell` en un proyecto de Django. Por ende es necesario tener un proyecto Django.

### **Crear un nuevo proyecto**

Si no tienes un proyecto creado y aún no tienes Django instalado, podemos realizar los siguietes pasos para generar uno nuevo:

**1. Crear un nuevo directorio para el proyecto**

Elige un destino para tu proyecto y luego crea un nuevo directorio con el nombre para el proyecto:

```bash
mkdir prueba-shell-django && cd prueba-shell-django
```

???+ info
	Modifica el nombre por el que desees, el comando anterior simplemente está creando un nuevo directorio y entrando en ese directorio a la vez. En distribuciones basadas en Linux, el comando anterior se puede abreviar con `take prueba-shell-django`

**2. Crear un entorno virtual**

Existen muchas maneras de crear un entorno virtual, para efectos prácticos haremos uso del paquete **venv** incluido en la mayoría de instalaciones de Python:

```bash title="terminal"
python3 -m venv venv
```

**3. Activar entorno virtual**

Una vez se crea el entorno virtual, observarás que se creó una nueva carpeta con el nombre de **venv** y dentro se encuentra una instalación limpia de Python que tenemos que activar para empezar a instalar los paquetes. Para ello debemos ejecutar el comando que corresponda según el sistema operativo que utilices:

=== ":octicons-terminal-16: Linux, macOS"
	```bash
	source venv/bin/activate
	```
=== ":octicons-terminal-16: Windows"
	```cmd
	.venv\Scripts\activate
	```

**4. Instalar Django**

Ahora que ya tenemos el entorno virtual creado y activado, podemos instalar django usando pip:

```bash title="terminal"
pip install django
```

**5. Generar un nuevo proyecto de django**

Una vez instalado django, procedemos a generar un nuevo proyecto en el directorio actual:

```bash title="terminal"
django-admin startproject _site .
```

Una vez generado el proyecto, tendrás disponible el archivo `manage.py` en el proyecto:

```plaintext hl_lines="3" title="Archivos del proyecto"
 prueba-shell-django
├──  venv
├──  manage.py
└──  mysite
    ├──  __init__.py
    ├──  asgi.py
    ├──  settings.py
    ├──  urls.py
    └──  wsgi.py
```

Ahora podemos ejecutar el siguiente comando para ingresar al shell de Django:

```bash title="terminal"
python manage.py shell
```


???+ info
	Si tenemos [`ipython`](https://pypi.org/project/ipython/) o [`bpython`](https://pypi.org/project/bpython/) instalado, se ingresa de la siguiente manera:
	```bash title="ipython"
	python manage.py shell -i ipython
	```
	```bash title="bpython"
	python manage.py shell -i bpython
	```

Ahora podemos observar que la terminal entra en modo interactivo, invitandonos a escribir nuevas instrucciones:


=== ":octicons-terminal-16: shell python"
	```plaintext
	Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
	[GCC 10.2.1 20210110] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> 
	```

=== ":octicons-terminal-16: shell bpython"
	```bpython
	>>>
	Welcome to bpython! Press <F1> for help.
	```

=== ":octicons-terminal-16: shell ipython"
	```ipython
	Python 3.9.2 (default, Feb 28 2021, 17:03:44)
	Type 'copyright', 'credits' or 'license' for more information
	IPython 8.18.1 -- An enhanced Interactive Python. Type '?' for help.
	
	In [1]:
	```

Antes de profundizar más en el shell de Django y los QuerySets del ORM, debemos crear una aplicación para poder definir un modelo y realizar operaciones en la base de datos.

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
		protein = models.DecimalField(max_digits=4, null=False, decimal_places=2)
		energy = models.IntegerField(default=0)
	
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

Luego generamos una nueva migración con el comando `makemigrations` y corremos las migraciones pendientes con el comando `migrate`:

=== "Bash"
	```bash
	python manage.py makemigrations #(1)!
	python manage.py migrate #(2)!
	```
	
	1. Genera una nueva migración que incluirá al modelo `FruitsInfo` definido anteriormente.
	2. Ejecuta las migraciones pendiente y crea las tablas en la base de datos.

=== "Output"

	```plaintext hl_lines="1 5"
	(venv) ➜  django_project python manage.py makemigrations
	Migrations for 'fruits':
		fruits/migrations/0001_initial.py
			- Create model FruitsInfo
	(venv) ➜ django_project python manage.py makemigrations
	Operations to perform:
		Apply all migrations: admin, auth, contenttypes, fruits, sessions
	Running migrations:
		Applying contenttypes.0001_initial... OK
		Applying auth.0001_initial... OK
		Applying admin.0001_initial... OK
		Applying admin.0002_logentry_remove_auto_add... OK
		Applying admin.0003_logentry_add_action_flag_choices... OK
		Applying contenttypes.0002_remove_content_type_name... OK
		Applying auth.0002_alter_permission_name_max_length... OK
		Applying auth.0003_alter_user_email_max_length... OK
		Applying auth.0004_alter_user_username_opts... OK
		Applying auth.0005_alter_user_last_login_null... OK
		Applying auth.0006_require_contenttypes_0002... OK
		Applying auth.0007_alter_validators_add_error_messages... OK
		Applying auth.0008_alter_user_username_max_length... OK
		Applying auth.0009_alter_user_last_name_max_length... OK
		Applying auth.0010_alter_group_name_max_length... OK
		Applying auth.0011_update_proxy_permissions... OK
		Applying auth.0012_alter_user_first_name_max_length... OK
		Applying fruits.0001_initial... OK
		Applying sessions.0001_initial... OK
	(venv) ➜ django_project
	```


## Conceptos de  ORM de Django

### ¿Qué es Django ORM?

Django ORM (Object-Relational Mapping) es una potente herramienta que permite interactuar con una base de datos relacional mediante código Python. Con Django ORM, podemos crear, recuperar, actualizar y eliminar registros en la base de datos mediante objetos y métodos Python.

### ¿Qué son los QuerySets?

Un QuerySet es una colección de objetos de base de datos que se pueden filtrar, ordenar y segmentar para limitar los resultados a un subconjunto específicos

## Operaciones ORM en el shell

### Insertar :octicons-diff-added-16:

En Django, una clase modelo representa una tabla de base de datos y una instancia de esa clase representa un registro particular dentro de la base de datos. Esto es análogo a usar una sentencia [`INSERT` en SQL](https://en.wikipedia.org/wiki/Insert_(SQL)).


#### método save()

Se puede crear un registro simplemente instanciando la clase definida en el modelo usando los argumentos de palabras claves, luego debemos llamar al método `save()` y así confirmar el nuevo registro en la base de datos.

En el siguiente ejemplo, veremos que sencillo es agregar un nuevo registro a la clase del modelo:

=== ":octicons-code-16: python"

	```py  hl_lines="3"
	from fruits.models import FruitsInfo #(1)!
	record = FruitsInfo(name="banana", origin="USA", protein=1.09, energy=371) #(2)!
	record.save() # (3)!
	```

	1. Importamos la clase del modelo
	2. Instanciamos la clase y la almacenamos en una variable
	3. invocamos al método `save()` para insertar en la base de datos

=== ":octicons-terminal-16: shell python"

	```plaintext
	(InteractiveConsole)
	>>> from fruits.models import FruitsInfo
	>>> record = record = FruitsInfo(name="banana", origin="USA", protein=1.09, energy=371)
	>>> record.save()
	```

=== ":octicons-terminal-16: shell ipython"
	
	```plaintext
	In [1]: from fruits.models import FruitsInfo
	In [2]: record = FruitsInfo(name="banana", origin="USA", protein=1.09, energy=371)
	In [3]: record.save()
	```


!!! info "Nota"
	Si no recibimos mensajes de errores indicados en la consola de Django, podemos suponer que el registro se agregó correctamente

#### método create()

Otra forma de insertar un registro en una clase modelo es usar el método `create()`. Esto elimina la necesidad de llamar al método `save()` para confirmar el registro en la base de datos. El siguiente ejemplo muestra su uso:

=== ":octicons-code-16: python"

	```py hl_lines="2"
	from fruits.models import FruitsInfo
	FruitsInfo.objects.create(name="apple", origin="USA", protein=0.26, energy=218)
	```
=== ":octicons-terminal-16: shell python"

	```plaintext
	(InteractiveConsole)
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.create(name="apple", origin="USA", protein=0.26, energy=218)
	>>> <FruitsInfo: USA apple>
	```
=== ":octicons-terminal-16: shell ipython"

	```plaintext
	In [1]: from fruits.models import FruitsInfo
	In [2]: FruitsInfo(name="banana", origin="USA", protein=1.09, energy=371)
	Out[2]: <FruitsInfo: USA apple>
	```

???+ info
	Si observamos el resultado en el shell, el método `create()` nos retorna un **QuerySet** con el objeto que acabamos de insertar.

### Insertar múltiples registros

Ahora veremos cómo insertar varios registros en una clase específica. Creamos una nueva clase `FruitsVendor` dentro de :octicons-file-code-16: `models.py` en la aplicación:

```py title="fruits/models.py"
class FruitsVendors(models.Model):

	vendor_id = models.CharField(max_length=4, null=False, primary_key=True)
	vendor_name = models.CharField(max_length=60)
	vendor_location = models.CharField(max_length=40)

	def __str__(self):
		return f"{self.vendor_id} - {self.vendor_name} - {self.vendor_location}"
```

En la nueva clase `FruitsVendors`, hemos definido un campo con llave primaria llamado `vendor_id`. Luego, definimos el método `__str__()` para mostrar todos los datos dentro de la clase en una cadena con formato.

Generamos una nueva migración y las ejecutamos con el comando `migrate`:

=== "bash"

	```bash
	python manage.py makemigrations
	python manage.py migrate
	```

=== "output"

	```plaintext
	Migrations for 'fruits':
  	fruits/migrations/0002_fruitsvendor.py
    	- Create model FruitsVendor
	Operations to perform:
  	Apply all migrations: admin, auth, contenttypes, fruits, sessions
	Running migrations:
  	Applying fruits.0002_fruitsvendor... OK
	```

#### método bulk_create()

Ahora podemos volver al shell e insertar múltiples registros en la clase `FluitsVendors` a la vez usando el método `bulk_create()`. El siguiente ejemplo muestra su uso:

=== ":octicons-code-16: python"

	```py
	from fruits.models import FruitsVendors
	FruitsVendors.objects.bulk_create(
		[
			FruitsVendors(vendor_id="V001", vendor_name="Fresh Fruits", vendor_location = "New York"),
			FruitsVendors(vendor_id="V002", vendor_name="Direct Delivery", vendor_location = "Sao Paulo"),
			FruitsVendors(vendor_id="V003", vendor_name="Fruit Mate", vendor_location = "Sydney")
		]
	)
	```

=== ":octicons-terminal-16: shell python"

	```plaintext
	(InteractiveConsole)
	>>> from fruits.models import FruitsVendors
	>>> FruitsVendors.objects.bulk_create(
	...     [
	...         FruitsVendors(vendor_id="V001", vendor_name="Fresh Fruits", vendor_location = "New York"),
	...         FruitsVendors(vendor_id="V002", vendor_name="Direct Delivery", vendor_location = "Sao Paulo"),
	...         FruitsVendors(vendor_id="V003", vendor_name="Fruit Mate", vendor_location = "Sydney")
	...     ]
	... )
	[<FruitsVendors: FruitsVendors object (V001)>,
	 <FruitsVendors: FruitsVendors object (V002)>,
	 <FruitsVendors: FruitsVendors object (V003)>]
	```

=== ":octicons-terminal-16: shell ipython"

	```ipython
	In [1]: from fruits.models import FruitsVendors
	   ...: FruitsVendors.objects.bulk_create(
	   ...:     [
	   ...:         FruitsVendors(vendor_id="V001", vendor_name="Fresh Fruits", vendor_location = "New York"),
	   ...:         FruitsVendors(vendor_id="V002", vendor_name="Direct Delivery", vendor_location = "Sao Paulo"),
	   ...:         FruitsVendors(vendor_id="V003", vendor_name="Fruit Mate", vendor_location="Sydney")
	   ...:     ]
	   ...: )
	Out[1]:
	[<FruitsVendors: FruitsVendors object (V001)>,
	 <FruitsVendors: FruitsVendors object (V002)>,
	 <FruitsVendors: FruitsVendors object (V003)>]
	```


### Listar :octicons-list-unordered-16:

#### método all()

Verificaremos esto utilizando el método `all()` que nos retorna un QuerySet que describe todos los objetos de la tabla en la base de datos:

=== ":octicons-code-16: python"

	```py hl_lines="2"
	from fruits.models import FruitsVendors
	FruitsVendors.objects.all()
	```
=== ":octicons-terminal-16: shell python"

	```bpython
	(InteractiveConsole)
	>>> from fruits.models import FruitsVendors
	>>> FruitsVendors.objects.all()
	<QuerySet [<FruitsVendors: V001 - Fresh Fruits - New York>, <FruitsVendors: V002 - Direct Delivery - Sao Paulo>, <FruitsVendors: V003 - Fruit Mate - Sydney>]>
	```

=== ":octicons-terminal-16: shell ipython"

	```ipython
	In [1]: from fruits.models import FruitsVendors
	In [2]: FruitsVendors.objects.all()
	Out[2]: <QuerySet [<FruitsVendors: V001 - Fresh Fruits - New York>, <FruitsVendors: V002 - Direct Delivery - Sao Paulo>, <FruitsVendors: V003 - Fruit Mate - Sydney>]>
	```

Debido a que hemos definido un método `__str__()` para mostrar un objeto en un formato legible para nosotros los humanos 😎, el método `all()` mostrará solo el valor definido en el método `__str__()`.

El método `values()` permite extraer los valores de un objeto determinado como se muestra a continuación:

=== ":octicons-code-16: python"

	```py
	FruitsVendors.objects.all().values()
	```
=== ":octicons-terminal-16: shell python"

	```plaintext
	(InteractiveConsole)
	>>> FruitsVendors.objects.all(),values()
	<QuerySet [{'vendor_id': 'V001', 'vendor_name': 'Fresh Fruits', 'vendor_location': 'New York'}, {'vendor_id': 'V002', 'vendor_name': 'Direct Delivery', 'vendor_location': 'Sao Paulo'}, {'vendor_id': 'V003', 'vendor_name': 'Fruit Mate', 'vendor_location': 'Sydney'}]>
	```

=== ":octicons-terminal-16: shell ipython"

	```ipython
	In [2]: FruitsVendors.objects.all().values()
	Out[2]: <QuerySet [{'vendor_id': 'V001', 'vendor_name': 'Fresh Fruits', 'vendor_location': 'New York'}, {'vendor_id': 'V002', 'vendor_name': 'Direct Delivery', 'vendor_location': 'Sao Paulo'}, {'vendor_id': 'V003', 'vendor_name': 'Fruit Mate', 'vendor_location': 'Sydney'}]>
	```

#### método get()

Si quisieramos recuperar un solo registro, podemos usar el método `get()`. Sin embargo, si hay más de un registro que coincida con la consulta que especificamos dentro del método `get()`, esto dará como resultado un error `MultipleObjectsReturned`.

El método `get()` es más viable cuando buscamos utilizando campos con índices únicos, como llave primaria. El siguiente ejemplo muestra el método `get()` utilizando el campo **id**:

=== ":octicons-code-16: python"

	```python
	from fruits.models import FruitsInfo
	FruitsInfo.objects.get(id=2)
	```
=== ":octicons-terminal-16: shell python"

	```bpython
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.get(id=2)
	<FruitsInfo: USA apple>
	```

=== ":octicons-terminal-16: shell ipython"

	```ipython
	In [1]: from fruits.models import FruitsInfo
   	In [2]: FruitsInfo.objects.get(id=2)
	Out[2]: <FruitsInfo: USA apple>
	```

### Búsquedas :octicons-search-16:

En el ORM de Django, podemos especificar operadores para filtrar un conjunto. Esto es análogo a los operadores que se pueden especificar dentro de una declaración [`WHERE` de SQL](https://es.wikipedia.org/wiki/SQL#:~:text=Cl%C3%A1usula%20WHERE%20(Donde)). Algunos ejemplos de búsquedas de campos y sus operadores SQL correspondientes son:

|ORM|SQL|
|:--|:--|
|`contains`|`LIKE`|
|`range`|`BETWEEN`|
|`gte` (mayor o igual que)|`>=`|
|`lte` (menor o igual que)|`<=`|

Los siguientes ejemplos demuestran cómo podemos utilizar las búsquedas por atributos dentro de Django shell.

#### operador - contains

Busquemos nombres de proveedores que incluyan la palabra "Fruits" en la clase `FruitsVendor`:

=== ":octicons-code-16: python"

	```python
	from fruits.models import FruitsVendors
	FruitsVendors.objects.filter(vendor_name__contains="Fruit")
	```

=== ":octicons-terminal-16: shell python"

	```plaintext
	>>> from fruits.models import FruitsVendors
	>>> FruitsVendors.objects.filter(vendor_name__contains="Fruit")
	<QuerySet [<FruitsVendor: FruitsVendor object (V001)>, <FruitsVendor: FruitsVendor object (V003)>]
	```

=== ":octicons-terminal-16: shell ipython"

	```ipython
	In [1]: from fruits.models import FruitsVendors
	In [2]: FruitsVendors.objects.filter(vendor_name__contains="Fruit")
	Out[2]: <QuerySet [<FruitsVendors: V001 - Fresh Fruits - New York>, <FruitsVendors: V003 - Fruit Mate - Sydney>]>
	```

#### operador - gte y lte

En los siguientes ejemplos, buscaremos registros usando los operadores de mayor y menor que:

=== ":octicons-code-16: python"
	```py
	from fruits.models import FruitsInfo
	FruitsInfo.objects.filter(protein__gte=1)
	FruitsInfo.objects.filter(energy__lte=250)
	```
=== ":octicons-terminal-16: shell python"
	```
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.filter(protein__gte=1)
	<QuerySet [<FruitsInfo: USA banana>]>
	>>> FruitsInfo.objects.filter(energy__lte=250)
	<QuerySet [<FruitsInfo: USA apple>]>
	```
=== ":octicons-terminal-16: shell ipython"
	```
	In [1]: from fruits.models import FruitsInfo
	In [2]: FruitsInfo.objects.filter(protein__gte=1)
	Out[2]: <QuerySet [<FruitsInfo: USA banana>]>
	In [3]: FruitsInfo.objects.filter(energy__lte=250)
	Out[3]: <QuerySet [<FruitsInfo: USA apple>]>
	```

### Actualizar :octicons-sync-16:

La operación de actualización se puede realizar junto con el método `filter()` para especificar el registro que se puede actualizar. Actualicemos el atributo `origin` al registro (`id=1`) en la tabla `FruitsInfo`:

=== ":octicons-code-16: python"
	```python hl_lines="3"
	from fruits.models import FruitsInfo
	FruitsInfo.objects.get(id=1).origin #(1)!
	FruitsInfo.objects.filter(id=1).update(origin='australia') #(2)!
	FruitsInfo.objects.get(id=1).origin #(3)!
	```

	1. Mostramos el valor actual del atributo origin
	2. Actualizamos el atributo origin
	3. Mostramos el valor actualizado del atributo origin

=== ":octicons-terminal-16: shell python"

	```bpython
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.get(id=1).origin
	'USA'
	>>> FruitsInfo.objects.filter(id=1).update(origin='australia')
	1
	>>> FruitsInfo.objects.get(id=1).origin
	'australia'
	```

=== ":octicons-terminal-16: shell ipython"

	```bpython
	In [1]: from fruits.models import FruitsInfo
	In [2]: FruitsInfo.objects.get(id=1).origin
	Out[2]: 'USA'
	In [3]: FruitsInfo.objects.filter(id=1).update(origin='australia')
	Out[3]: 1
	In [4]: FruitsInfo.objects.get(id=1).origin
	Out[4]: 'australia'
	```

### Eliminar :octicons-x-circle-16:

El ORM nos ofrece el método `delete()` para eliminar registros de una clase específica. Esto es análogo a la instrucción [`DELETE` en SQL](https://en.wikipedia.org/wiki/Delete_(SQL))

#### Eliminar un registro

Al eliminar un solo registro, debemos utilizar el método `get()`, ya que devuelve directamente el objeto especificado. En el siguiente ejemplo eliminamos un registro (`id=3`) de la clase `FruitsInfo()`:

=== "Python"
	```python
	from fruits.models import FruitsInfo
	
	FruitsInfo.objects.all() #(1)!
	FruitsInfo.objects.get(id=3).delete() #(2)!
	FruitsInfo.objects.all() #(3)!
	```

	1. Mostramos todos los objetos
	2. Eliminamos el objeto
	3. Mostramos todos los objetos nuevamente

=== "Shell"

	```
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.all().values()
	<QuerySet [<FruitsInfo: australia apple>, <FruitsInfo: USA banana>, <FruitsInfo: USA pineapple>]>
	>>> FruitsInfo.objects.get(id=3).delete()
	(1, {'fruits.FruitsInfo': 1})
	>>> FruitsInfo.objects.all()
	<QuerySet [<FruitsInfo: australia apple>, <FruitsInfo: USA banana>]>
	```

#### Eliminar varios registros

El método `delete()` se puede utilizar para eliminar todos los registros de una clase determinada, simplemente especificando la operación de eliminación con el método `all()` para eliminar todos o `filter()` para eliminar un conjunto que cumpla una determinada condición. En el siguiente ejemplo, eliminaremos todos los registros:


=== "Python"
	```python
	from fruits.models import FruitsInfo
	
	FruitsInfo.objects.all() #(1)!
	FruitsInfo.objects.all().delete() #(2)!
	FruitsInfo.objects.all() #(3)!
	```

	1. Mostramos todos los objetos
	2. Eliminamos todos los objetos
	3. Comprobamos, mostrando todos los objetos

=== "Shell"

	```
	>>> from fruits.models import FruitsInfo
	>>> FruitsInfo.objects.all()
	<QuerySet [<FruitsInfo: australia apple>, <FruitsInfo: USA banana>]>
	>>> FruitsInfo.objects.all().delete()
	(2, {'fruits.FruitsInfo': 2})
	>>> FruitsInfo.objects.all()
	<QuerySet []>
	```