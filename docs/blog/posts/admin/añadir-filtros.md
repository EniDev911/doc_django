---
date: 2024-05-14
title: "Añadir Filtros al Panel Administrativo de Django"
tags: ["admin", "filtros"]
---

## **Filtrar por Campos Existentes**

Django permite añadir filtros por campos del modelo de forma muy sencilla. Para hacerlo, basta con usar la opción `list_filter` en el **Admin** de tu modelo.

<!-- more -->


```py
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
```

Para añadir los filtros en el panel administrativo, debes usar `list_filter` en el archivo `admin.py`:

```py title="admin.py"
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')  # Añadir los filtros aquí

admin.site.register(Post, PostAdmin)
```

**¿Qué hace esto?**

`lister_filter` añade filtros en el panel administrativo para los campos que especifiques. En este caso, podrás filtrar los posts por el autor y la fecha de publicación en la interfaz del administrador.


## **Búsqueda por un Campo de Texto**

