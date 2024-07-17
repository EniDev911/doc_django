---
icon: material/application
---

Django distingue entre proyectos y aplicaciones. Una aplicación es un paquete de Python con una estructura determinada (modelos, vistas, plantillas, etc). Un proyecto es (además de un paquete de Python) un conjunto de aplicaciones con una configuración común.

## Crear una nueva aplicación

```bash title="bash"
python3 manage.py startapp myapp
```

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
