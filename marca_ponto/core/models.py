from django.db import models

# Create your models here.
class Usuario(models.Model):
    Registro = models.CharField(max_length=6)
    Nome = models.CharField(max_length=30)
    CPF = models.CharField(max_length=11)
    Email = models.EmailField()
    NomeDeUsuario = models.CharField(max_length=12)
    Senha = models.CharField(max_length=12)
    Perfil = models.CharField(max_length=12)
    UltimoLogin = models.DateTimeField()
    RecCreatedOn = models.DateTimeField()
    RecCreatedBy = models.DateTimeField()
    RecModifiedOn = models.DateTimeField()
    RecModifiedBy = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class Ponto(models.Model):    
    Usuario = models.CharField(max_length=30)
    Entrada = models.TextField()
    Almoco = models.TextField()
    Retorno = models.TextField()
    Saida = models.TextField()
    DataHora = models.DateTimeField(auto_now_add=True)
    Credito = models.FloatField()
    Debito = models.FloatField()
    Status = models.BooleanField()
    Aprovador = models.CharField(max_length=30)
    DataAprovacao = models.DateTimeField()

    def __str__(self):
        return str(self.id)        