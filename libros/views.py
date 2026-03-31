from django.shortcuts import render, redirect
from .form import LibrosForm
from .models import Libros

# Create your views here.
def nuevo_libro(request, template_name: str= 'libros/libros_form.html'):
  if request.method == 'POST':
    form = LibrosForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect('libros')
  else:
    form = LibrosForm()
  data = {'form': form}
  return render(request, template_name, data)


def lista_libros(request, template_name: str='libros/libros.html'):
  list_libros = Libros.objects.all()
  data = {'form': list_libros}
  return render(request, template_name, data)

def mostrar_libro(request, id_libro: int,template_name: str='libros/libro.html'):
  libro = Libros.objects.get(id=id_libro)
  data = {'objeto': libro}
  return render(request, template_name, data)


def modificar_libro(request, id_libro: int, template_name: str='libros/libros_form.html'):
  libro = Libros.objects.get(id=id_libro)
  form = LibrosForm(request.POST or None, instance=libro)
  if request.method == 'POST':
    if form.is_valid():
      form.save(commit=True)
      return redirect('libros')
  data = {'form': form}
  return render(request, template_name, data)

def eliminar_libro(request, id_libro: int, template_name: str='eliminar_registro.html'):
  libro = Libros.objects.get(id=id_libro)
  if request.method == 'POST':
    libro.delete()
    return redirect('libros')
  return render(request, template_name)