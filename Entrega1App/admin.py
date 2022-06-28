from django.contrib import admin
from .models import *


class MarcasAdmin(admin.ModelAdmin):
    list_display = ("marca","categoria","cantidad_productos")
    search_fields = ("marca","categoria")

# admin, admin --> python manage.py createsuperuser

class ProductosAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'categoria',"precio","stock")
    search_fields = ("nombre","categoria")
    
    
class LocalesAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'localidad',"rubro_principal","horario_apertura","horario_cierre")
    search_fields = ("nombre","localidad","rubro_principal")
    
    
admin.site.register(Marcas, MarcasAdmin)    
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Locales, LocalesAdmin)