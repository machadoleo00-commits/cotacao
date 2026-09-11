import requests

resposta = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
dados = resposta.json()
print(dados['USDBRL']['bid'])

with open('cotação.csv', 'a') as arquivo:
    arquivo.write(f'{dados['USDBRL']['create_date']},{dados['USDBRL']['bid']}\n')