def pesquisa_binaria(lista, item, baixo, alto):
    if baixo > alto:
        return False
    meio = (baixo + alto) // 2 # divisao inteira
    if lista[meio] == item:
        return True
    elif lista[meio] > item:
        return pesquisa_binaria(lista, item, baixo, meio - 1)
    else:
        return pesquisa_binaria(lista, item, meio + 1, alto)

lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
item_para_buscar = 16

alto = len(lista_ordenada) - 1
resultado = pesquisa_binaria(lista_ordenada, item_para_buscar, 0, alto)

if resultado:
    print("Item encontrado")
else:
    print("Nao encontrado")
