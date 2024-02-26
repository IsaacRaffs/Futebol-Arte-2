from django.db import models


DIVISAO_CHOICES = (
    ('A', 'Série A'),
    ('B', 'Série B'),
    ('C', 'Série C'),
)
COMPETICAO_CHOICES = (
    ('Municipal', 'M'),
    ('E', 'Estadual'),
    ('N', 'Nacional'),
    ('G', 'Global'),
)

GENERO_CHOICES = (
    ('M', 'masculino'),
    ('F', 'Feminino'),
)
POSICAO_CHOICES = (
    ('Atac', 'Atacante'),
    ('Zag', 'Zagueiro'),
)

class Campeonatos(models.Model):
    nome = models.CharField(choices=COMPETICAO_CHOICES, max_length=40)
    
    def __str__(self):
        return self.nome

class Clube(models.Model):
    nome = models.CharField( max_length=50)
    ano_de_fundacao = models.PositiveIntegerField(default=1970)
    divisao = models.CharField(max_length=50, choices=DIVISAO_CHOICES, default='A')
    genero = models.CharField(choices=GENERO_CHOICES, max_length=30)
    campeonato = models.ForeignKey(Campeonatos, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True)
    posicao = models.CharField(choices=POSICAO_CHOICES, max_length=20)
    numero = models.IntegerField(default=0)
    foto = models.FileField()
    genero = models.CharField(choices=GENERO_CHOICES, max_length=30)
    
    
    def __str__(self):
        return self.nome

