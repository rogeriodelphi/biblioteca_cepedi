from django.db import models
from datetime import date

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    matricula = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Data de última modificação automática
    ultima_modificacao = models.DateTimeField(auto_now=True)
    # Data de um evento específico (padrão pode ser alterado)
    data_evento = models.DateField(default=date.today)


    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'Aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']

