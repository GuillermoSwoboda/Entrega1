from tabnanny import verbose
from django.db import models

# Create your models here.

class Marcas(models.Model):
    marca = models.CharField("Marca",max_length=30)
    CATEGORIAS = (
        (1, "Bazar"),
        (2, "Camping"),
        (3, "Rodados"),
        (4, "Deportes"),
        (5, "Ferretería"),
    )
    categoria = models.PositiveSmallIntegerField("Categoría",choices=CATEGORIAS)
    cantidad_productos = models.IntegerField("Cantidad de productos")
    class Meta:
        verbose_name_plural = "Marcas"

class Productos(models.Model):
    nombre = models.CharField(max_length=30) 
    CATEGORIAS = (
        (1, "Bazar"),
        (2, "Camping"),
        (3, "Rodados"),
        (4, "Deportes"),
        (5, "Ferretería"),
    )
    categoria = models.PositiveSmallIntegerField("Categoria",choices=CATEGORIAS)
    precio = models.FloatField("Precio $")
    stock = models.IntegerField("Stock")
    class Meta:
        verbose_name_plural = "Productos"