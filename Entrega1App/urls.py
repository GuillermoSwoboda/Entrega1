from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
        path("",index, name="inicio"),    
    path("marcas/", marcas, name="marcas"),
    path("productos/", productos, name="productos"),
    path("locales/", locales, name="locales"),
    path("crear_marca/", crear_marca, name="crear_marca"),
    path("crear_producto/", crear_producto, name="crear_producto"),
    path("crear_local/", crear_local, name="crear_local"),
    path("base/",base),
]