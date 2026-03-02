from django.contrib import messages

from apps.autores.forms import AutorForm
from django.shortcuts import render, redirect, get_object_or_404
from apps.autores.models import Autor

def inserir_autor(request):
    template_name = 'autores/form_autor.html'
    if request.method == 'POST':
        form = AutorForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do autor foi realizado com sucesso!')
        return redirect('autores:listar_autores')
    form = AutorForm()
    context = {'form': form}
    return render(request, template_name, context)

