from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from Entrega1App.models import Avatar

class NuevaMarca(forms.Form):
    
    marca = forms.CharField(max_length=30, label="Nombre de la Marca")
    CATEGORIAS = (
        (0, "Seleccione"),
        (1, "Bazar"),
        (2, "Camping"),
        (3, "Rodados"),
        (4, "Deportes"),
        (5, "Ferretería"),
    )
    categoria = forms.ChoiceField(choices=CATEGORIAS, required=True, label="¿A qué categoría pertenece?",initial=0)
    cantidad_productos = forms.IntegerField(min_value=0, label="¿Cuántos productos tiene la marca?")
    
    
class NuevoProducto(forms.Form):
    
    nombre = forms.CharField(max_length=30, label="Nombre del Producto")
    CATEGORIAS = (
        (0, "Seleccione"),
        (1, "Bazar"),
        (2, "Camping"),
        (3, "Rodados"),
        (4, "Deportes"),
        (5, "Ferretería"),
    )
    categoria = forms.ChoiceField(choices=CATEGORIAS, required=True, label="¿A qué categoría pertenece?",initial=0)
    precio = forms.FloatField(min_value=0, label="¿Cuál es el precio?")
    stock = forms.IntegerField(min_value=0, label="¿Cuál es el stock disponible?")


class NuevoLocal(forms.Form):
    
    nombre = forms.CharField(max_length=50, label="Nombre del Local")
    LOCALIDAD = (
        (0, "Seleccione"),
        (1, "Córdoba"),
        (2, "Capital Federal"),
        (3, "Rosario"),
        (4, "Mendoza"),
        (5, "Salta"),
    )
    localidad = forms.ChoiceField(choices=LOCALIDAD, required=True, label="¿En que ciudad se encuentra?",initial=0)
    RUBROS = (
        (0, "Seleccione"),
        (1, "Especialista en Bazar"),
        (2, "Especialista en Camping"),
        (3, "Especialista en Rodados"),
        (4, "Especialista en Deportes"),
        (5, "Especialista en Ferretería"),
    )
    rubro_principal = forms.ChoiceField(choices=RUBROS, required=True, label="¿Cuál es el rubro principal?",initial=0)
    direccion = forms.CharField(max_length=150, label="Ingrese la dirección del Local")
    DIAS = (
        (0, "Seleccione"),
        (1, "Lunes a Viernes"),
        (2, "Lunes a Sábados"),
        (3, "Lunes a Domingos"),
    )
    dias = forms.ChoiceField(choices=DIAS, required=True, label="¿Qué días abre?",initial=0)
    horario_apertura = forms.TimeField(label="¿Cuál es el horario de apertura?")
    horario_cierre = forms.TimeField(label="¿Cuál es el horario de cierre?")
    
    
class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        

class UserEditform(UserCreationForm):
    
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    
    imagen = forms.ImageField(label="Imagen", required=False)
    
    class Meta:
        model = Avatar
        fields = ["imagen"]