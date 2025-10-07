cidades = [
    [22, 25, 28, 32],
    [20, 23, 26, 30],
    [18, 22, 25, 29]
]

num_colunas = len(cidades[0])

transposta = []

for i in range(num_colunas):
    nova_linha = []
    for linha in cidades:
        nova_linha.append(linha[i])
    transposta.append(nova_linha)

print(transposta)

