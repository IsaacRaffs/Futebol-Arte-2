from django.db import models
from cep.models import Pais, Estado, Cidade

class Competição(models.Model):
    TIPO_CHOICES = (
        ('Estadual', 'Estadual'),
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional')
    )
    
    CATEGORIA_CHOICES = (
        ('COPA', 'copa'),
        ('CAMPEONATO', 'campeonato')
    )

    nome = models.CharField(max_length=40)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    
    class Meta:
        verbose_name_plural = 'Competições'
    
    def __str__(self):
        return self.nome


class Time(models.Model):
    GENERO_CHOICES = (
    ('M', 'masculino'),
    ('F', 'Feminino'),
    )
            
    DIVISAO_CHOICES = (
        ('A', 'Série A'),
        ('B', 'Série B'),
        ('C', 'Série C'),
    )

    nome = models.CharField( max_length=50)
    ano_de_fundacao = models.PositiveIntegerField(default=1970)
    divisao = models.CharField(max_length=50, choices=DIVISAO_CHOICES, default='A')
    genero = models.CharField(choices=GENERO_CHOICES, max_length=30)
    competição = models.ForeignKey(Competição, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(null=True, blank=True)

    estado = models.ForeignKey(Estado, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nome


class Jogador(models.Model):

    GENERO_CHOICES = (
    ('M', 'masculino'),
    ('F', 'Feminino'),
    )
    POSICAO_CHOICES = (
        ('Atac', 'Atacante'),
        ('Zag', 'Zagueiro'),
    )

    nome = models.CharField(max_length=50)
    time = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True)
    posicao = models.CharField(choices=POSICAO_CHOICES, max_length=20)
    numero = models.IntegerField(default=0)
    foto = models.ImageField(null=True, blank=True)
    genero = models.CharField(choices=GENERO_CHOICES, max_length=30)
    
    class Meta:
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return self.nome

class Titulos(models.Model):
    COLOCACAO_CHOICES = (
        ('Campeão', 'Campeão'),
        ('Vice-Campeão', 'Vicee-Campeão'),
    )

    nome = models.CharField(max_length=50, blank=False, null=False)
    ano_conquista = models.IntegerField(blank=False, null=False)
    colocacao = models.CharField(max_length=20, choices=COLOCACAO_CHOICES)
    time =  models.ForeignKey(Time, on_delete=models.CASCADE, null=True)    
    
    class Meta:
        verbose_name_plural = 'Titulos'

    def __str__(self):
        return self.nome
    
