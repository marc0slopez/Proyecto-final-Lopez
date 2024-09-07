from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),  # Acepta GET
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/agregar/', views.agregar_receta, name='agregar_receta'),
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('recetas/<int:receta_id>/editar/', views.editar_receta, name='editar_receta'),
    path('recetas/<int:receta_id>/eliminar/', views.eliminar_receta, name='eliminar_receta'),
    path('about/', views.acerca_de_mi, name='acerca_de_mi'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),  # Nueva URL para editar perfil
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
