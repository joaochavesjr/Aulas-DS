import pandas as pd

dados = {
    "nome": ['João', 'Maria', 'Pedro', 'Ana'],
    "idade": [30, 25, 22, 32],
    "cidade": ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador'],
    "curso": ['Engenharia', 'Medicina', 'Direito', 'Ciência da Computação'],
    "nota1": [8.5, 9.2, 7.8, 9.1],
    "nota2": [9.0, 8.8, 8.2, 9.4]
}

df = pd.DataFrame(dados)
print(df)

