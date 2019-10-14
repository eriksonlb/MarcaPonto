from django.contrib import admin
from .models import Usuario, Ponto

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Registro', 'Nome', 'NomeDeUsuario', 'UltimoLogin']

@admin.register(Ponto)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Usuario', 'Entrada', 'Almoco', 'Retorno', 'Saida']
