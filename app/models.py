from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    local = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.local

class Servidor(models.Model):
    local = models.OneToOneField(Local, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return str(self.local)

class Distribuidora(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    local = models.ManyToManyField(Local)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    def __str__(self):
	    return self.nome

class ClassificacaoIndicativa(models.Model):
    classificacao_indicativa = models.CharField(max_length=100)
    
    class Meta():
        verbose_name_plural = 'Classificação indicativa'

    def __str__(self):
        return self.classificacao_indicativa

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'Gêneros'
    
    def __str__(self):
	    return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    genero = models.OneToOneField(Genero, on_delete=models.CASCADE)
    classificacao_indicativa = models.OneToOneField(ClassificacaoIndicativa, on_delete=models.CASCADE)
    distribuidora = models.OneToOneField(Distribuidora, on_delete=models.CASCADE)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)

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