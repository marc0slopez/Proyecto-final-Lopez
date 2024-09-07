from django.contrib import admin
from .models import Receta, Perfil

# Define el modelo de administración para Receta
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    list_filter = ('autor', 'fecha_creacion')
    search_fields = ('titulo', 'cuerpo')

# Verifica que no estés registrando el modelo más de una vez
admin.site.register(Receta, RecetaAdmin)

# Registrar el modelo Perfil en el admin
admin.site.register(Perfil)