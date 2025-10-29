tabuleiro = [
	[2, 0, 0, 0],
        [2, 2, 0, 0],
        [4, 0, 4, 0],
        [0, 0, 0, 0]
]

def print_tab(matriz):
    for linha in matriz:
        print(linha)

def mover(matriz):
    #import pdb; pdb.set_trace()
    for lin_num, linha in enumerate(matriz):
        soma = 0
        for coluna in linha:
            soma += coluna
        matriz[lin_num][0] = soma
     
    for lin_num, linha in enumerate(matriz):
        for col_num, coluna in enumerate(linha):
            if col_num > 0:
                 matriz[lin_num][col_num] = 0

    return matriz


if __name__ == '__main__':
    print_tab(tabuleiro)
    print('-' * 20)
    novo_tabuleiro = mover(tabuleiro)
    print_tab(novo_tabuleiro)

