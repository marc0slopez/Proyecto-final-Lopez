from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=100, default='Sin subtitulo')
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
