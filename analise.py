import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cotação.csv')
df['data'] = pd.to_datetime(df['data'])
print(f'media: {df.groupby('moeda')['valor'].mean()}')
print(f'maximo: {df.groupby('moeda')['valor'].max()}')
print(f'minimo: {df.groupby('moeda')['valor'].min()}')

fig, eixos = plt.subplots(3, 1, figsize=(10, 8))

for posicao, moeda in enumerate(df['moeda'].unique()):
    dados_moeda = df[ df['moeda'] == moeda ]
    eixos[posicao].plot(dados_moeda['data'], dados_moeda['valor'])
    eixos[posicao].set_title(f'Cotação {moeda}')
    eixos[posicao].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('grafico.pdf', dpi=150)
plt.show()

