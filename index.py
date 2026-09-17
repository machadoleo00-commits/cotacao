from modelos import ColetorDeCotacoes
import time


coletor_dolar = ColetorDeCotacoes('USD-BRL')
while True:
    coletor_dolar.buscar_cotacao()
    time.sleep(30*60)
