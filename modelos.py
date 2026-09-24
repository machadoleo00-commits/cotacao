import requests
import os


class ColetorDeCotacoes:
    def __init__(self, moeda):
        self.moeda = moeda
        self.date = {}
        self.bid = {}


    def buscar_cotacao(self):
        resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/{','.join(self.moeda)}')
        dados = resposta.json()
        for moeda in self.moeda:
            chave = moeda.replace('-','')
            self.bid[moeda] = dados[chave]['bid']
            self.date[moeda] = dados[chave]['create_date']
            if not os.path.exists('cotação.csv'):
                with open('cotação.csv', 'a') as arquivo:
                    arquivo.write('data,moeda,valor\n')
            with open('cotação.csv', 'a') as arquivo:
                arquivo.write(f'{self.date[moeda]},{moeda},{self.bid[moeda]}\n')
