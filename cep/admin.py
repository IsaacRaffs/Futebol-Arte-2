from django.contrib import admin
from cep.models import Pais, Estado, Cidade

# Register your models here.

class EstadoInline(admin.StackedInline):
    model = Estado
    extra = 0

class CidadeInline(admin.StackedInline):
    model = Cidade
    extra = 0

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [EstadoInline]

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [CidadeInline]
