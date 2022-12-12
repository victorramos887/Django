from django.contrib import admin
from .models import Pessoa

class FiltrandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('nome', 'email')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Pessoa, FiltrandoPessoas)

# Register your models here.
