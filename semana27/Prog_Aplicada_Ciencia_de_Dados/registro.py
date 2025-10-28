import pandas as pd

df = pd.read_csv('quadro_medalhas.csv', delimiter=';')

# Quantas medalhas cada país ganhou no total ao longo dos anos?
df.groupby(['Pais'])['Qtde'].sum()

# Qual foi o número total de medalhas de cada tipo (Ouro, Prata, Bronze) ao longo dos anos?
df.groupby(['Pais','Medalha'])['Qtde'].sum()

# Quantas medalhas cada país ganhou em cada ano?
df.groupby(['Pais','Ano'])['Qtde'].sum()

# Quantas medalhas de cada tipo cada país ganhou em cada ano?
df.groupby(['Pais','Ano','Medalha'])['Qtde'].sum()

# Qual é o menor valor de medalhas por ano que cada país recebeu?
df.groupby(['Pais','Ano'])['Qtde'].min()
