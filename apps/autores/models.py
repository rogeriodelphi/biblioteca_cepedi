from django.db import models

class Autor(models.Model):
    autor = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField()
    foto = models.ImageField('Foto', upload_to='fotos_autores', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.autor


    class Meta:
        db_table = 'Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['autor']
