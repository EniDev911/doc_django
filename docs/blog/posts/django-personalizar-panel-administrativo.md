---
date: 2024-08-14
draft: true 
---

Django viene con un panel administrativo **muy potente** y **fácil** de usar, pero a menudo se desea modificar su apariencia, las vistas de los modelos o incluso la funcionalidad para que se ajuste a las necesidades del proyecto.

Primero, debemos tener un proyecto correctamente configurado y tener habilitado el panel administrativo. Para ello, debes tener las aplicaciones `django.contrib.admin`, `django.contrib.auth`, y `django.contrib.contenttypes` en el archivo `settings.py`:

```py title="settings.py"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Otras aplicaciones
]
```

El diseño de la interfaz administrativa de Django es bastante básico por defecto, pero se puede personalizar fácilmente para ajustarse a la identidad visual de tu proyecto.