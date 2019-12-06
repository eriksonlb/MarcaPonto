from django.db import models
from django.contrib.auth.models import User

class Colaboradores(models.Model):  
    nome_completo = models.CharField(max_length=50)
    numero_registro = models.CharField(max_length=9)
    cargo = models.CharField(max_length=12)
    setor = models.CharField(max_length=12)
    entrada = models.CharField(max_length=5)
    intervalo = models.CharField(max_length=5)
    retorno = models.CharField(max_length=5)
    saida = models.CharField(max_length=5)
    dias = models.CharField(max_length=16)
    gerente = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
      return str(self.id)

class RegistroPonto(models.Model):
    colaborador = models.ForeignKey(Colaboradores, db_column="nome_completo", on_delete=models.CASCADE, default=0)
    data = models.DateField(auto_now_add=True)
    dia = models.CharField(max_length=3, null=True)
    hora = models.CharField(max_length=20, null=True)
    tipo_registro = models.CharField(max_length=9, default=0)

    def __str__(self):
      return str(self.id)

class ChamadosSuporte(models.Model):
    titulo = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    descricao = models.TextField(max_length=200)

    def __str__(self):
      return str(self.titulo)
