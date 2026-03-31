from django.urls import path
from . import views


urlpatterns = [
  path('nuevo_libro', views.nuevo_libro, name='nuevo_libro'),
  path('libros', views.lista_libros, name='libros'),
  path('modificar_libro/<int:id_libro>', views.modificar_libro, name='modificar_libro'),
  path('ver/<int:id_libro>', views.mostrar_libro, name='ver'),
  path('eliminar/<int:id_libro>', views.eliminar_libro, name='eliminar'),
  
]