from modelos import ColetorDeCotacoes
import time


coletor_dolar = ColetorDeCotacoes(['USD-BRL', 'EUR-BRL', 'BTC-BRL'])
while True:
    coletor_dolar.buscar_cotacao()
    time.sleep(30*60)
