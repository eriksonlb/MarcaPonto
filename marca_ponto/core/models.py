from django.db import models
from django.contrib.auth.models import User

class registro_ponto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    entrada = models.TimeField()
    intervalo = models.TimeField()
    retorno = models.TimeField()
    saida = models.TimeField()
    hora_extra = models.TimeField()
    hora_negativa = models.TimeField()  

    def __str__(self):
      return str(self.id)

