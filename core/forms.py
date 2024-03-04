from django import forms
from .models import Jogador

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'time', 'posicao', 'numero', 'foto', 'genero']
        