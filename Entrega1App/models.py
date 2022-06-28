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
        
class Locales(models.Model):
    nombre = models.CharField(max_length=50) 
    LOCALIDAD = (
        (1, "Córdoba"),
        (2, "Capital Federal"),
        (3, "Rosario"),
        (4, "Mendoza"),
        (5, "Salta"),
    )
    localidad = models.PositiveSmallIntegerField("Localidad",choices=LOCALIDAD)
    RUBROS = (
        (1, "Especialista en Bazar"),
        (2, "Especialista en Camping"),
        (3, "Especialista en Rodados"),
        (4, "Especialista en Deportes"),
        (5, "Especialista en Ferretería"),
    )
    rubro_principal = models.PositiveSmallIntegerField("Rubro",choices=RUBROS)
    horario_apertura = models.TimeField("Apertura")
    horario_cierre = models.TimeField("Apertura")
    class Meta:
        verbose_name_plural = "Locales"