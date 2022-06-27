from django.contrib import admin
from .models import *


class MarcasAdmin(admin.ModelAdmin):
    list_display = ("marca","categoria","cantidad_productos")
    search_fields = ("marca","categoria")

# admin, admin --> python manage.py createsuperuser

class ProductosAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'categoria',"precio","stockdisponible")
    
    
admin.site.register(Marcas, MarcasAdmin)    
admin.site.register(Productos, ProductosAdmin)