import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cotação.csv')

plt.plot(df['data'],df['valor'])
plt.xticks(rotation = 45)
plt.title('Cotação')
plt.xlabel('Data/Hora')
plt.ylabel('Valor(R$)')
plt.tight_layout()
plt.show()
