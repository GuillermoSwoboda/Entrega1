from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    # path("",inicio, name="inicio"),
    path("",views.index, name="index")    
    # # URLS de Entrega1App
    # path("profesores/", profesores, name="profesores"),
    # path("estudiantes/", estudiantes, name="estudiantes"),
    # path("cursos/", cursos, name="cursos"),
    # path("entregables/", entregables, name="entregables"),
    # # path("base/",base),
]