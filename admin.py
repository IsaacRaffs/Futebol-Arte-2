from django.contrib import admin
from core.models import Clube, Jogador, Campeonatos
# Register your models here.
@admin.register(Clube)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_de_fundacao', 'divisao', 'genero', 'campeonato']

@admin.register(Jogador)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'clube', 'posicao', 'numero', 'genero', 'foto']

@admin.register(Campeonatos)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['nome']