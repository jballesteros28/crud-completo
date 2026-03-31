from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Libros(models.Model):
  nombre = models.CharField(max_length=120)
  autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)