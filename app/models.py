from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Local(models.Model):
    nome = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome

class Distribuidora(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    local = models.ManyToManyField(Local)
    
    def __str__(self):
	    return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Gêneros'
    
    def __str__(self):
	    return self.nome

class ClassificacaoIndicativa(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta():
        verbose_name_plural = 'Classificação indicativa'

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    classificacao_indicativa = models.ForeignKey(ClassificacaoIndicativa, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    def __str__(self):
	    return self.nome

class JogoGratuito(Jogo):

    class Meta():
        verbose_name_plural = 'Jogos gratuitos'

class JogoPago(Jogo):
    preco = models.FloatField()

    class Meta():
        verbose_name_plural = 'Jogos pagos'