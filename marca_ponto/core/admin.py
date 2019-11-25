from django.contrib import admin
from .models import registro_ponto

@admin.register(registro_ponto)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'entrada', 'intervalo', 'retorno', 'saida', 'hora_extra', 'hora_negativa']