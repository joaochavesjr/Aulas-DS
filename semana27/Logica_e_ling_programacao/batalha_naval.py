
tabuleiro = [['~'] * 10 for _ in range(10)]


def colocar_navio(tabuleiro, linha_inicial, coluna_inicial, tamanho, orientacao):
    if orientacao == 'horizontal':
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial + i] = '#'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            tabuleiro[linha_inicial + i][coluna_inicial] = '#'


def dar_tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = 'X'
        print("Tiro certeiro!")
        return True
    
    elif tabuleiro[linha][coluna] == '~':
        tabuleiro[linha][coluna] = 'o'
        print("Você errou o tiro.")
        return False
    else:
        print("Esta posição já foi escolhida.")
        return False
    
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()
    print()


imprimir_tabuleiro(tabuleiro)

colocar_navio(tabuleiro, 2, 3, 4, 'horizontal')
colocar_navio(tabuleiro, 5, 5, 3, 'vertical')
imprimir_tabuleiro(tabuleiro)
dar_tiro(tabuleiro, 2, 3)
imprimir_tabuleiro(tabuleiro)
dar_tiro(tabuleiro, 0, 0)
imprimir_tabuleiro(tabuleiro)
