from django.db import models
from alunos.models import Aluno
from livros.models import Livro
from datetime import date

class Emprestimo(models.Model):
    aluno_id = models.ForeignKey(Aluno, verbose_name='Aluno', on_delete=models.CASCADE)
    livro_id = models.ForeignKey(Livro, verbose_name='Livro',on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(verbose_name='Data Empréstimo', auto_now_add=True)
    data_devolucao = models.DateField(verbose_name='Data Devolução', default=date.today)
    data_prevista_devolucao = models.DateField(verbose_name='Previsão devolução')
    status = models.CharField(max_length=1, choices=[('E','Emprestado'), ('D','Devolvido')])

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'Emprestimo'
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['status']
        managed = True