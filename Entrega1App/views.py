from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def index(request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            
        return render(request,"Entrega1App/index.html",{"url":url})
        
    return render(request,"Entrega1App/index.html",{})

def base(request):
   
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            
        return render(request,"Entrega1App/base.html",{"url":url})
    
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

@staff_member_required
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

@login_required
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

@staff_member_required
def eliminar_producto(request,producto_id):
    
    producto = Productos.objects.get(id=producto_id)
    producto.delete()
    
    return redirect("productos")

@login_required
def editar_producto(request,producto_id):
    
    producto = Productos.objects.get(id=producto_id)
    
    if request.method == "POST":
        
        formulario = NuevoProducto(request.POST)
        
        if formulario.is_valid():
            
            info_producto = formulario.cleaned_data
                        
            producto.nombre = info_producto["nombre"]
            producto.categoria = info_producto["categoria"]
            producto.precio = info_producto["precio"]
            producto.stock = info_producto["stock"]
            producto.save()
            
            return redirect("productos")
    
    formulario = NuevoProducto(initial={"nombre":producto.nombre,"categoria":producto.categoria,"precio":producto.precio,"stock":producto.stock})
    
    return render(request,"Entrega1App/formularioProductoeditar.html",{"form":formulario})

@login_required 
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
    
    
def buscar_producto(request):
    
    if request.method == "POST":
        
        nombre = request.POST["nombre"]
        
        nombres = Productos.objects.filter(nombre__icontains=nombre)

        return render(request,"Entrega1App/busqueda_producto.html",{"nombres":nombres})
    
    else:

        nombres = [] 
        
        return render(request,"Entrega1App/busqueda_producto.html",{"nombres":nombres})        

def buscar_local(request):
    
    if request.method == "POST":
        
        nombre = request.POST["nombre"]
        
        nombres = Locales.objects.filter(nombre__icontains=nombre)

        return render(request,"Entrega1App/busqueda_local.html",{"nombres":nombres})
    
    else:

        nombres = [] 
        
        return render(request,"Entrega1App/busqueda_local.html",{"nombres":nombres})        

@staff_member_required
def eliminar_local(request,local_id):
    
    local = Locales.objects.get(id=local_id)
    local.delete()
    
    return redirect("locales")

@login_required
def editar_local(request,local_id):
    
    local = Locales.objects.get(id=local_id)
    
    if request.method == "POST":
        
        formulario = NuevoLocal(request.POST)
        
        if formulario.is_valid():
            
            info_local = formulario.cleaned_data
                        
            local.nombre = info_local["nombre"]
            local.localidad = info_local["localidad"]
            local.rubro_principal = info_local["rubro_principal"]
            local.direccion = info_local["direccion"]          
            local.dias = info_local["dias"]
            local.horario_apertura = info_local["horario_apertura"]
            local.horario_cierre = info_local["horario_cierre"]
            local.save()
            
            return redirect("locales")
    
    formulario = NuevoLocal(initial={"nombre":local.nombre,"localidad":local.localidad,"rubro_principal":local.rubro_principal,"direccion":local.direccion,"horario_apertura":local.horario_apertura,"horario_cierre":local.horario_cierre})
    
    return render(request,"Entrega1App/formularioLocaleditar.html",{"form":formulario})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")

    form = AuthenticationForm()

    return render(request,"Entrega1App/login.html",{"form":form})

def register_request(request):
    
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            
            
            form.save()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
                    
        return render(request,"Entrega1App/register.html",{"form":form})
    
    # form = UserCreationForm()
    form = UserRegisterForm()
        
    return render(request,"Entrega1App/login.html",{"form":form})

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == "POST":
       
        form = UserEditform(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info ["email"]
            user.first_name = info ["first_name"]
            user.last_name = info ["last_name"]

            # user.password1 = info["password1"]
            
            user.save()
            
            return redirect ("inicio")
                
    else:
       form = UserEditform(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})
        
    return render(request, "Entrega1App/editar_perfil.html",{"form":form})


def logout_request(request):
    
    logout(request)
    return redirect("inicio")

def nuestros_valores(request):
        
    return render(request,"Entrega1App/nuestros_valores.html",{})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            user = User.objects.get(username=request.user.username)
            
            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])
            
            avatar.save()
            
            return redirect("inicio")
    
    else:
        form = AvatarForm()
    
    return render(request,"Entrega1App/agregar_avatar.html",{"form":form})

def about_me(request):
        
    return render(request,"Entrega1App/about_me.html",{})



    # if request.method == "POST":

    #     categoria = request.POST["categoria"]
        
    #     categorias = Productos.objects.filter(categoria__icontains=categoria)
    
    #     return render(request,"Entrega1App/busqueda_producto.html",{"categoria":categorias})
    
    # else: #get y otros
        

    #     return render(request,"Entrega1App/busqueda_producto.html",{"categoria":categorias})    