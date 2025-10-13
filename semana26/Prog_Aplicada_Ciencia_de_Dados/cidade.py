import pandas as pd

dados = {
    "nome": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"],
    "estado": ["SP", "RJ", "MG", "BA"],
    "população": [12.2, 6.7, 5.5, 2.9],
}
 
df = pd.DataFrame(dados)
print(df)

