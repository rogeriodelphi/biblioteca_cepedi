from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'descricao', 'foto')
    search_fields = ['autor',]
