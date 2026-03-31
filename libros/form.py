from django.forms import ModelForm
from .models import Libros

class LibrosForm(ModelForm):
  class Meta:
    model = Libros
    fields = '__all__'