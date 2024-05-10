## Otra base de datos


Este archivo `mysite/settings.py` es un módulo normal de Python con variables de nivel de módulo que representan la configuración de Django.

Por defecto la configuración de Django utiliza **SQLite** como motor de base de datos. Esta es la opción más fácil ya que **SQLite** está incluido en Python por lo que no se requiere instalar nada más para soportar este motor de base de datos. Sin embargo, al iniciar un proyecto real, nos conviene utilizar bases de datos más potente como **PostgreSQL** para evitar dolores de cabeza a futuro.


Si queremos cambiar de motor de base de datos, abrá el archivo `mysite/settings.py`, y buscamos el item **`DATABASES`** en la clave **`default`** :


=== ":octicons-file-code-16: `my_project/settings.py`"

    ```{ .python  }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

### Configurar Postgres

Lo primero que debemos hacer es instalar la biblioteca [psycopg2](https://pypi.org/project/psycopg2/){: target='_blank' }:

```bash
pip install psycopg2-binary
```

=== ":octicons-file-code-16: `my_project/settings.py`"

    ```py hl_lines="3"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2,
            'NAME': 'project_db',
            'USER': 'postgres' # 👈 tu usuario para postgres,
            'PASSWORD': 'postgres' # 👈 tu password para postgres,
            'HOST': 'localhost',
            'PORT': ''
        }
    }
    ```

En este caso la base de datos tiene por nombre **project_db**, el usuario y password es **postgres**.