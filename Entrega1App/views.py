from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request,"Entrega1App/index.html",{})

def base(request):
   
    return render(request,"Entrega1App/base.html",{})

def marcas(request):
   
    return render(request,"Entrega1App/marcas.html",{})

def productos(request):
   
    return render(request,"Entrega1App/productos.html",{})

def locales(request):
   
    return render(request,"Entrega1App/locales.html",{})

