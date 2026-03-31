from django.db import models

# Create your models here.
class Usuario(models.Model):
  nombre = models.CharField(max_length=50)
  edad = models.IntegerField()
  email = models.EmailField(max_length=120, unique=True)
  
  def __str__(self) -> str:
    return f"{self.nombre}"