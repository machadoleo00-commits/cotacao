import requests
import os


class ColetorDeCotacoes:
    def __init__(self, moeda):
        self.moeda = moeda
        self.date = None
        self.bid = None


    def buscar_cotacao(self):
        resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/{self.moeda}')
        dados = resposta.json()
        print(dados['USDBRL']['bid'])
        self.bid = dados['USDBRL']['bid']
        self.date = dados['USDBRL']['create_date']
        if not os.path.exists('cotação.csv'):
                with open('cotação.csv', 'a') as arquivo:
                    arquivo.write('data,valor\n')
        with open('cotação.csv', 'a') as arquivo:
            arquivo.write(f'{dados['USDBRL']['create_date']},{dados['USDBRL']['bid']}\n')

coletor_dolar = ColetorDeCotacoes('USD-BRL')
coletor_dolar.buscar_cotacao()