from django.urls import path
from . import views

urlpatterns = [
  path('nuevo_usuario', views.nuevo_usuario, name='nuevo_usuario'),
  path('usuarios', views.lista_usuarios, name='usuarios'),
  path('eliminar/<int:id_usuario>', views.eliminar_usuario, name='eliminar'),
  path('modificar/<int:id_usuario>', views.modificar_usuario, name='modificar'),
  path('ver/<int:id_usuario>', views.mostrar_usuario, name='ver')
]