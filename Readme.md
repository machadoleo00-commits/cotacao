# Cotação Moedas

Projeto em Python que consulta periodicamente a cotação de várias moedas (USD-BRL, EUR-BRL e BTC-BRL) usando a [AwesomeAPI](https://economia.awesomeapi.com.br/), salva um histórico das consultas em CSV, analisa esse histórico com pandas e gera um gráfico da evolução de cada moeda com matplotlib.

## Estrutura do projeto

- `modelos.py` — contém a classe `ColetorDeCotacoes`, responsável por buscar a cotação atual de uma lista de moedas (em uma única requisição) e salvar no histórico (`cotação.csv`).
- `index.py` — ponto de entrada do programa: cria o coletor com a lista de moedas e roda em loop contínuo, buscando novas cotações a cada 30 minutos.
- `analise.py` — lê o histórico salvo, calcula média, máximo e mínimo por moeda com pandas (`groupby`) e plota a evolução de cada moeda em gráficos separados com matplotlib.
- `cotação.csv` — histórico de cotações coletadas (não versionado, ver `.gitignore`).

## O que o projeto faz

- Faz uma única requisição GET para a AwesomeAPI com todas as moedas desejadas, usando a biblioteca `requests`.
- Extrai a data/hora e o valor de compra (`bid`) de cada moeda no JSON retornado.
- Salva uma linha por moeda a cada coleta no arquivo `cotação.csv`, no formato longo, com cabeçalho criado automaticamente na primeira execução:

  ```
  data,moeda,valor
  2026-09-28 08:40:19,USD-BRL,5.1802
  ```

- Roda continuamente, coletando novas cotações a cada 30 minutos, sem precisar de agendamento externo ao Python.
- Lê o histórico com `pandas` e calcula média, valor máximo e valor mínimo separados por moeda.
- Gera um gráfico de linha por moeda (cada um com sua própria escala), mostrando a evolução da cotação ao longo do tempo.

## Como rodar

Iniciar a coleta contínua (roda em loop, a cada 30 minutos, até ser interrompido com `Ctrl+C`):
```bash
python index.py
```

Analisar o histórico e visualizar os gráficos:
```bash
python analise.py
```

Para acompanhar outras moedas, basta alterar a lista passada ao `ColetorDeCotacoes` no `index.py` (no formato `'USD-BRL'`).

## Requisitos

- Python 3.12 ou superior
- `requests` (`pip install requests`)
- `pandas` (`pip install pandas`)
- `matplotlib` (`pip install matplotlib`)

## Status

Projeto concluído com as funcionalidades principais: coleta agendada de múltiplas moedas, histórico, análise estatística por moeda e visualização gráfica.

## Possíveis melhorias futuras

- Salvar os gráficos como imagem, além de exibi-los
- Rodar a coleta como serviço em segundo plano (sem precisar manter o terminal aberto)
- Abrir o arquivo de histórico uma única vez por coleta, em vez de uma vez por moeda