from django.db import models

# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Paises'
    
    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome