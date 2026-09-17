# Cotação Moedas

Projeto em Python que consulta a cotação atual do dólar (USD-BRL) usando a [AwesomeAPI](https://economia.awesomeapi.com.br/), salva um histórico das consultas em CSV e permite analisar esse histórico com pandas.

## Estrutura do projeto

- `index.py` — contém a classe `ColetorDeCotacoes`, responsável por buscar a cotação atual e salvar no histórico (`cotação.csv`).
- `analise.py` — lê o histórico salvo e calcula estatísticas básicas (média, máximo, mínimo) usando pandas.
- `cotação.csv` — histórico de cotações coletadas (não versionado, ver `.gitignore`).

## O que o projeto faz

- Faz uma requisição GET para a AwesomeAPI usando a biblioteca `requests`.
- Extrai a data/hora da cotação e o valor de compra (`bid`) do JSON retornado.
- Salva cada consulta como uma nova linha no arquivo `cotação.csv`, com cabeçalho (`data,valor`) criado automaticamente na primeira execução.
- Lê o histórico com `pandas` e calcula média, valor máximo e valor mínimo do período.

## Como rodar

Coletar uma nova cotação:
```bash
python index.py
```

Analisar o histórico coletado:
```bash
python analise.py
```

## Requisitos

- Python 3
- `requests` (`pip install requests`)
- `pandas` (`pip install pandas`)

## Próximos passos

- [x] Organizar a lógica de busca e salvamento em uma classe (`ColetorDeCotacoes`)
- [x] Carregar o histórico com `pandas` e calcular estatísticas (média, variação, máx/mín)
- [ ] Gerar gráfico da evolução da cotação com `matplotlib`