from encodings import search_function
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
from pessoas.models import Pessoa
# from django.http import HttpResponse
# Create your views here.


def index(request):

    receitas = Receita.objects.order_by('-date_receita').filter(publicado=True)

    dados = {
        'receitas':receitas
    }
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita':receita
    }
    return render(request, 'receita.html', receita_a_exibir)

def buscar(request):  # sourcery skip: merge-nested-ifs, move-assign
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas':lista_receitas
    }


    return render(request, 'buscar.html', dados)