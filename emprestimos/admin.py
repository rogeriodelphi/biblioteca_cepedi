from django.contrib import admin
from .models import Livro, Aluno, Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'livro_id', 'data_emprestimo', 'status')
    search_fields = ['data_emprestimo', 'status']
