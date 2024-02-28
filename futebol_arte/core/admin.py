from django.contrib import admin
from core.models import Time, Jogador, Competição, Titulos

# Define os inlines
class JogadorInline(admin.StackedInline):
    model = Jogador
    extra = 0

class TituloInline(admin.StackedInline):
    model = Titulos
    extra = 0

# Registra os modelos no admin
@admin.register(Competição)
class CompetiçãoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_de_fundacao', 'divisao', 'genero', 'competição']
    inlines = [JogadorInline, TituloInline]

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'Time', 'posicao', 'numero', 'genero', 'foto']

@admin.register(Titulos)
class TitulosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_conquista', 'colocacao']
