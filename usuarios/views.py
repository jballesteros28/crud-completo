from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .form import UsuarioForm
from .models import Usuario

# Create your views here.
def nuevo_usuario(request, template_name: str= 'usuarios/usuario_form.html'):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect('usuarios')
  else:
    form = UsuarioForm()
  data = {'form': form}
  return render(request, template_name, data)


def lista_usuarios(request, template_name: str='usuarios/usuarios.html'):
  list_usuarios = Usuario.objects.all()
  data = {'form': list_usuarios}
  return render(request, template_name, data)


def eliminar_usuario(request, id_usuario: int ,template_name: str='eliminar_registro.html'):
  usuario_seleccionado = Usuario.objects.get(id=id_usuario)
  if request.method == 'POST':
    usuario_seleccionado.delete()
    return redirect('usuarios')
  data = {'objeto': usuario_seleccionado.nombre}
  return render(request,template_name, data)

def modificar_usuario(request, id_usuario: int,template_name: str='usuarios/usuario_form.html'):
  usuario_seleccionado = Usuario.objects.get(id=id_usuario)
  form = UsuarioForm(request.POST or None, instance=usuario_seleccionado)
  if request.method =='POST':
    if form.is_valid():
      form.save(commit=True)
      return redirect('usuarios')
  data = {'form': form}
  return render(request,template_name,data)

def mostrar_usuario(request, id_usuario: int,template_name: str='usuarios/usuario.html'):
  usuario = Usuario.objects.get(id=id_usuario)
  data = {'form': usuario}
  return render(request, template_name, data)