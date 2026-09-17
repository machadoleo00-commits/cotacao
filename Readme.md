# Cotação Moedas

Projeto em Python que consulta a cotação atual do dólar (USD-BRL) usando a [AwesomeAPI](https://economia.awesomeapi.com.br/), salva um histórico das consultas em CSV, analisa esse histórico com pandas e gera um gráfico da evolução com matplotlib.

## Estrutura do projeto

- `index.py` — contém a classe `ColetorDeCotacoes`, responsável por buscar a cotação atual e salvar no histórico (`cotação.csv`).
- `analise.py` — lê o histórico salvo, calcula estatísticas básicas (média, máximo, mínimo) com pandas e plota a evolução da cotação com matplotlib.
- `cotação.csv` — histórico de cotações coletadas (não versionado, ver `.gitignore`).

## O que o projeto faz

- Faz uma requisição GET para a AwesomeAPI usando a biblioteca `requests`.
- Extrai a data/hora da cotação e o valor de compra (`bid`) do JSON retornado.
- Salva cada consulta como uma nova linha no arquivo `cotação.csv`, com cabeçalho (`data,valor`) criado automaticamente na primeira execução.
- Lê o histórico com `pandas` e calcula média, valor máximo e valor mínimo do período.
- Gera um gráfico de linha (com `matplotlib`) mostrando a evolução da cotação ao longo do tempo.

## Como rodar

Coletar uma nova cotação:
```bash
python index.py
```

Analisar o histórico e visualizar o gráfico:
```bash
python analise.py
```

## Requisitos

- Python 3
- `requests` (`pip install requests`)
- `pandas` (`pip install pandas`)
- `matplotlib` (`pip install matplotlib`)

## Status

Projeto concluído com as funcionalidades principais: coleta, histórico, análise estatística e visualização gráfica.

## Possíveis melhorias futuras

- Suportar múltiplas moedas simultaneamente
- Agendar a coleta automática (ex: a cada hora)
- Salvar o gráfico como imagem, além de exibi-lo