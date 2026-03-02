from apps.autores import forms
from apps.autores.models import Autor
from django.forms import ModelForm, DateInput


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        exclude = ('data_criacao', 'ultima_modificacao')
