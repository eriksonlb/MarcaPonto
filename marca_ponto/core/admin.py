from django.contrib import admin
from .models import RegistroPonto, Colaboradores, ChamadosSuporte

@admin.register(RegistroPonto)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['id', 'colaborador', 'data', 'hora']
    
@admin.register(Colaboradores)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'numero_registro', 'cargo', 'setor', 'entrada', 'intervalo', 'retorno', 'saida', 'dias']