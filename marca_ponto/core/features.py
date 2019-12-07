from datetime import datetime
import random

def comparar_periodo(hora):
    hora_registro = hora
    entrada_min = hora_registro.replace(hour=7)
    entrada_max = hora_registro.replace(hour=10)
    intervalo_min = hora_registro.replace(hour=11)
    intervalo_max = hora_registro.replace(hour=13)
    retorno_min = hora_registro.replace(hour=13, minute=30)
    retorno_max = hora_registro.replace(hour=15)
    saida_min = hora_registro.replace(hour=16)
    saida_max = hora_registro.replace(hour=19)

    if hora_registro >= entrada_min and hora_registro < entrada_max:
        return "entrada"
    if hora_registro >= intervalo_min and hora_registro < intervalo_max:
        return "intervalo"
    if hora_registro >= saida_min and hora_registro < saida_max:
        return "retorno"
    if hora_registro >= saida_min and hora_registro < saida_max:
        return "saida"
    else:
        return "divergencia"


