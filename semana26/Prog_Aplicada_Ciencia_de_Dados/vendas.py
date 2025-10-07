import pandas as pd
data = {
    "Date": ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"],
    "Sales": [200, 300, 400, 200, 300, 300],
    "Price": [3, 1, 2, 4, 3, 2]
}

df = pd.DataFrame(data)
df_mask = df['Sales'] == 300
df_filtrado = df[df_mask]
df_filtrado

df.loc[df['Sales'] == 300]

colunas_selecionadas = df.loc[df['Sales'] == 300, ['Date', 'Sales']]
colunas_selecionadas
