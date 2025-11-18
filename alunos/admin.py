from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'matricula', 'email', 'telefone')
    search_fields = ['nome', 'matricula']