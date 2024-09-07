from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from .forms import RecetaForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Perfil  # Importar el modelo Perfil
from .forms import EditarPerfilForm, PerfilForm  # Importar el formulario del perfil
from django.contrib import messages

def inicio(request):
    return render(request, 'blog/inicio.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'blog/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_recetas')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'blog/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'blog/detalle_receta.html', {'receta': receta})

def acerca_de_mi(request):
    return render(request, 'blog/acerca_de_mi.html')

@login_required
def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'blog/agregar_receta.html', {'form': form})

@login_required
def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if receta.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta receta.")
    
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'blog/editar_receta.html', {'form': form, 'receta': receta})

@login_required
def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if receta.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta receta.")
    
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'blog/eliminar_receta.html', {'receta': receta})

@login_required
def editar_perfil(request):
    # Obtener el perfil asociado al usuario actual
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)  # Nuevo formulario para el avatar
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid() and password_form.is_valid() and perfil_form.is_valid():
            user = form.save()
            password_form.save()
            perfil_form.save()  # Guardar el avatar
            update_session_auth_hash(request, user)  # Mantiene la sesión iniciada después de cambiar la contraseña
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('inicio')
    else:
        form = EditarPerfilForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)  # Mostrar el formulario del avatar
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'blog/editar_perfil.html', {
        'form': form,
        'perfil_form': perfil_form,  # Pasamos el formulario del avatar
        'password_form': password_form
    })