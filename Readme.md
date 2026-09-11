# Cotação Moedas

Script em Python que consulta a cotação atual do dólar (USD-BRL) usando a [AwesomeAPI](https://economia.awesomeapi.com.br/) e salva um histórico das consultas em um arquivo CSV.

## O que o projeto faz

- Faz uma requisição GET para a AwesomeAPI usando a biblioteca `requests`.
- Extrai a data/hora da cotação e o valor de compra (`bid`) do JSON retornado.
- Salva cada consulta como uma nova linha no arquivo `cotação.csv`, no formato:

  ```
  data_hora,valor
  ```

## Como rodar

```bash
python index.py
```

Cada execução adiciona uma nova linha ao histórico em `cotação.csv`.

## Requisitos

- Python 3
- Biblioteca `requests` (`pip install requests`)

## Próximos passos

- [ ] Organizar a lógica de busca e salvamento em uma classe (`ColetorDeCotacoes`)
- [ ] Carregar o histórico com `pandas` e calcular estatísticas (média, variação, máx/mín)
- [ ] Gerar gráfico da evolução da cotação com `matplotlib`