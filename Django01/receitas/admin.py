from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):

    #lista dois items que iram aparecer no admin
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_de_preparo')

    #lista de valores que pode ser usado para abrir a tabela
    list_display_links = ('id', 'nome_receita')

    #criando um campo de pesquisa
    search_fields = ('nome_receita', )

    #filtros rápidos
    list_filter = ('categoria', )

    #paginação da aréa do admin
    list_per_page = 2


admin.site.register(
    Receita,
    ListandoReceitas
)


# Register your models here.
