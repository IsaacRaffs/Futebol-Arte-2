from django.contrib import admin
from core.models import Time, Jogador, Competição, Titulos
from django.utils.html import format_html
# Define os inlines

class JogadorInline(admin.StackedInline):
    model =  Jogador
    extra  = 0

class TitulosInline(admin.StackedInline):
    model = Titulos
    extra  = 0

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    def image(self, obj):
        if obj.foto:
            return format_html(f'<img src="{obj.foto.url}" width="60"; heigth="60"/>')
        
    list_display = ['nome', 'image', 'estado','ano_de_fundacao', 'divisao', 'genero', 'competição']

    inlines = [JogadorInline, TitulosInline]

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    def image(self, obj):
        if obj.foto:
            return format_html(f'<img src="{obj.foto.url}" width="60"; height="60" />')

    list_display = ['nome', 'time', 'posicao', 'numero', 'genero', 'image']

@admin.register(Titulos)
class TitulosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_conquista', 'colocacao']

@admin.register(Competição)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'tipo']