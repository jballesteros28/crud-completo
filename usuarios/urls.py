from django.urls import path
from . import views

urlpatterns = [
  path('nuevo_usuario', views.nuevo_usuario, name='nuevo_usuario'),
  path('usuarios', views.lista_usuarios, name='usuarios'),
  path('eliminar_usuario/<int:id_usuario>', views.eliminar_usuario, name='eliminar_usuario'),
  path('modificar_usuario/<int:id_usuario>', views.modificar_usuario, name='modificar_usuario'),
  path('ver_usuario/<int:id_usuario>', views.mostrar_usuario, name='ver_usuario')
]