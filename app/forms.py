from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, SolicitudArticulo, StockRequest, Post, Proveedor
class RegistroClienteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'apellidos', 'username', 'password1', 'password2', 'tipo_de_cuenta']
        widgets = {
            'tipo_de_cuenta': forms.HiddenInput(attrs={'value': 'cliente'})
        }

class RegistroAdministradorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'apellidos', 'username', 'password1', 'password2', 'tipo_de_cuenta']
        widgets = {
            'tipo_de_cuenta': forms.HiddenInput(attrs={'value': 'administrador'})
        }

class RegistroTrabajadorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'apellidos', 'username', 'password1', 'password2', 'tipo_de_cuenta']
        widgets = {
            'tipo_de_cuenta': forms.HiddenInput(attrs={'value': 'trabajador'})
        }
        
        
class InicioSesionForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class SolicitudArticuloForm(forms.ModelForm):
    class Meta:
        model = SolicitudArticulo
        fields = '__all__'  
        
        
        

class StockRequestForm(forms.ModelForm):
    class Meta:
        model = StockRequest
        fields = ['producto', 'cantidad_necesaria']
        widgets = {
            'producto': forms.HiddenInput()
        }

class EditStockForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['stock']
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'numero_telefono','correo', 'especialidad']        