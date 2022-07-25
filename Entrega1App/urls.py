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
    path("buscar_producto/", buscar_producto, name="buscar_producto"),
    path("buscar_local/", buscar_local, name="buscar_local"),
    path("eliminar_local/<local_id>", eliminar_local, name="eliminar_local"),
    path("editar_local/<local_id>", editar_local, name="editar_local"), 
    path("eliminar_producto/<producto_id>", eliminar_producto, name="eliminar_producto"),
    path("editar_producto/<producto_id>", editar_producto, name="editar_producto"),
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('nuestros_valores', nuestros_valores, name="nuestros_valores"),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    path('about_me', about_me, name="about_me"),
    path("base/",base),
]