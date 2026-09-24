import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cotação.csv')

print(f'media: {df.groupby('moeda')['valor'].mean()}')
print(f'maximo: {df.groupby('moeda')['valor'].max()}')
print(f'minimo: {df.groupby('moeda')['valor'].min()}')

#plt.plot(df['data'],df['valor'])
#plt.xticks(rotation = 45)
#plt.title('Cotação')
#plt.xlabel('Data/Hora')
#plt.ylabel('Valor(R$)')
#plt.tight_layout()
#plt.show()
