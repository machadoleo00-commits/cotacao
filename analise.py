import pandas as pd
df = pd.read_csv('cotação.csv')
print(df.head())
print(f'Média: {df['valor'].mean()}')
print(f'Valor máximo: {df['valor'].max()}')
print(f'Valor minimo: {df['valor'].min()}')