def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio  # posição do item
        elif chute < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  # não encontrado

numeros = [1, 3, 5, 7, 9, 11, 13, 15]

print(busca_binaria(numeros, 7))   # Saída: 3
print(busca_binaria(numeros, 4))   # Saída: -1 (não está na lista)
