from django import forms
from .models import Receta, Perfil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class EditarPerfilForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Agregamos los campos en español
        labels = {
            'username': 'Usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']  # Solo el campo avatar
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
