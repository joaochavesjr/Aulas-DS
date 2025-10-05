def insertion_sort(arr):
    """
    Função para ordenar uma lista usando o algoritmo de ordenação por inserção.
    
    Parâmetros:
    arr (list): Lista de números a ser ordenada.
    
    Retorna:
    list: Lista ordenada.
    """
    # Percorre a lista a partir do segundo elemento (índice 1)
    for i in range(1, len(arr)):
        # Elemento atual a ser inserido na sublista ordenada
        key = arr[i]
        # Índice do elemento anterior
        j = i - 1

        # Move os elementos da sublista ordenada que são maiores que 'key'
        # para uma posição à frente de sua posição atual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere o elemento na posição correta
        arr[j + 1] = key

    return arr


# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    lista = [30, 10, 20, 40, 5]
    print("Lista original:", lista)

    # Ordena a lista
    lista_ordenada = insertion_sort(lista)
    print("Lista ordenada:", lista_ordenada)

