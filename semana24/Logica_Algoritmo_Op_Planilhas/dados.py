import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV
df = pd.read_csv('dados.csv')

# Ver dados
print(df.head())

# Pivotar os dados para facilitar o gráfico
pivot_df = df.pivot(index='Mes', columns='Produto', values='Vendas')

# Plotar gráfico de linhas
pivot_df.plot(kind='line', marker='o')
plt.title('Vendas Mensais por Produto')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.legend(title='Produto')
plt.tight_layout()
plt.show()

