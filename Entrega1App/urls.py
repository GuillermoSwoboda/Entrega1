from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
        path("",index, name="inicio"),    
    path("marcas/", marcas, name="marcas"),
    path("productos/", productos, name="productos"),
    path("locales/", locales, name="locales"),
    path("base/",base),
]