from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    Registro = models.CharField()
    Nome = models.CharField()
    CPF = models.CharField(max_length=100)
    Email = models.EmailField()
    NomeDeUsuario = models.CharField()
    Senha = models.CharField()
    Perfil = models.CharField()
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
    Credito = models.CharField()
    Debito = models.CharField()
    Status = models.BooleanField()
    Aprovador = models.Id()
    DataAprovacao = models.DateTimeField

    def __str__(self):
        return str(self.id)