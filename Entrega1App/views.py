from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime

# Create your views here.

def index(request):
    
    return render(request,"Entrega1App/index.html",{})

def base(request):
   
    return render(request,"Entrega1App/base.html",{})

def marcas(request):
    
    marcas = Marcas.objects.all()
    
    return render(request,"Entrega1App/marcas.html",{"marcas":marcas})

def productos(request):
    
    productos = Productos.objects.all()
    
    return render(request,"Entrega1App/productos.html",{"productos":productos})

def locales(request):
    
    locales = Locales.objects.all()
   
    return render(request,"Entrega1App/locales.html",{"locales":locales})

def crear_marca(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevaMarca(request.POST)
        
        if formulario.is_valid():
            
            info_marca = formulario.cleaned_data
            
            marca = Marcas(marca=info_marca["marca"],categoria=info_marca["categoria"],cantidad_productos=info_marca["cantidad_productos"])
        
            marca.save()
       
            return redirect("marcas") #render(request,"ProyectoCoderApp/formulario_curso.html",{})
        
        else:
            return render(request,"Entrega1App/formularioMarca.html",{"form":formulario})
        
    else: # get y otros
        
        formularioVacio = NuevaMarca()
        
        return render(request,"Entrega1App/formularioMarca.html",{"form":formularioVacio})        


def crear_producto(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoProducto(request.POST)
        
        if formulario.is_valid():
            
            info_producto = formulario.cleaned_data
            
            producto = Productos(nombre=info_producto["nombre"],categoria=info_producto["categoria"],precio=info_producto["precio"],stock=info_producto["stock"])
        
            producto.save()
       
            return redirect("productos") #render(request,"ProyectoCoderApp/formulario_curso.html",{})
        
        else:
            return render(request,"Entrega1App/formularioProducto.html",{"form":formulario})
        
    else: # get y otros
        
        formularioVacio = NuevoProducto()
        
        return render(request,"Entrega1App/formularioProducto.html",{"form":formularioVacio})        
    
def crear_local(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoLocal(request.POST)
        
        if formulario.is_valid():
            
            info_local = formulario.cleaned_data
            
            local = Locales(nombre=info_local["nombre"],localidad=info_local["localidad"],rubro_principal=info_local["rubro_principal"],direccion=info_local["direccion"],dias=info_local["dias"],horario_apertura=info_local["horario_apertura"],horario_cierre=info_local["horario_cierre"])
        
            local.save()
       
            return redirect("locales") #render(request,"ProyectoCoderApp/formulario_curso.html",{})
        
        else:
            return render(request,"Entrega1App/formularioLocal.html",{"form":formulario})
        
    else: # get y otros
        
        formularioVacio = NuevoLocal()
        
        return render(request,"Entrega1App/formularioLocal.html",{"form":formularioVacio})
    
    
def dia(request):
    
    hoy = datetime.datetime.now()

    return render(request,"Entrega1App/index.html",{"dia_hora":hoy})    