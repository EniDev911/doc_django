---
categories:
  - mtv
---

## Modelos

Los modelos en Django forman la piedra angular de las aplicaciones y sirven como un medio sofisticado para definir las tablas de bases de datos y sus relaciones.

### Creación de modelos de Django

Los modelos en Django son básicamente planos para las tablas de tu base de datos. Cada modelo corresponde a una sola tabla y cada atributo del modelo representa un campo de la tabla.

A continuación veamos un ejemplo como se define un modelo simple en Django:

```py
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()
```

## Implementando relaciones

Las relaciones son fundamentales para reflejar las asociones del mundo real entre diferentes conjuntos de datos en su base de datos.

Los modelos de Django atienden varios tipos de relaciones:


### Uno a muchos

Se utiliza `ForeignKey` para vincular varias instancias a una única instancia de otro. Por ejemplo, se pueden vincular varios pedidos a un único cliente.


