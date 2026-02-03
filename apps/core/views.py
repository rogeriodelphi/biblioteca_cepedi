from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.alunos.models import Aluno
from apps.livros.models import Livro
from apps.emprestimos.models import Emprestimo
from django.db.models.functions import TruncMonth
from django.db.models import Count

@login_required(login_url='usuarios:login')
def index(request):
    total_alunos =  Aluno.objects.all().count()
    total_livros = Livro.objects.all().count()
    total_emprestimos = Emprestimo.objects.filter(status='E').count()

    emprestimos_por_mes = (
        Emprestimo.objects
        .filter(data_emprestimo__isnull=False)
        .annotate(mes=TruncMonth('data_emprestimo'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    meses = [e['mes'].strftime('%m/%Y') for e in emprestimos_por_mes]
    totais = [e['total'] for e in emprestimos_por_mes]

    # return render(request, 'index.html', {
    #     'meses': meses,
    #     'totais': totais
    # })




    context = {
        'total_alunos': total_alunos,
        'total_livros': total_livros,
        'total_emprestimos': total_emprestimos,
        'meses': meses,
        'totais': totais,

    }
    return render(request, 'index.html', context)