def bubble_sort(lista):
    """
    Implementação do algoritmo Bubble Sort
    
    Args:
        lista: Lista de elementos a serem ordenados
    
    Returns:
        Lista ordenada em ordem crescente
    """
    # Cria uma cópia da lista para não modificar a original
    arr = lista.copy()
    n = len(arr)
    
    # Percorre todos os elementos da lista
    for i in range(n):
        # Flag para otimização - detecta se houve troca
        trocou = False
        
        # Últimos i elementos já estão ordenados
        for j in range(0, n - i - 1):
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        
        # Se não houve troca, a lista já está ordenada
        if not trocou:
            break
    
    return arr

def bubble_sort_verbose(lista):
    """
    Versão do Bubble Sort que mostra o processo passo a passo
    """
    arr = lista.copy()
    n = len(arr)
    print(f"Lista inicial: {arr}")
    
    for i in range(n):
        print(f"\n--- Passada {i + 1} ---")
        trocou = False
        
        for j in range(0, n - i - 1):
            print(f"Comparando {arr[j]} e {arr[j + 1]}", end=" ")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
                print(f"-> Trocou! Lista: {arr}")
            else:
                print("-> Não trocou")
        
        if not trocou:
            print("Lista já está ordenada!")
            break
    
    return arr

# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("=== BUBBLE SORT ===")
    print(f"Lista original: {numeros}")
    
    # Ordenação simples
    resultado = bubble_sort(numeros)
    print(f"Lista ordenada: {resultado}")
    
    print("\n" + "="*50)
    print("=== BUBBLE SORT DETALHADO ===")
    
    # Ordenação com detalhes
    numeros2 = [5, 2, 8, 1, 9]
    resultado_verbose = bubble_sort_verbose(numeros2)
    print(f"\nResultado final: {resultado_verbose}")
    
    # Testando com diferentes tipos de dados
    print("\n" + "="*50)
    print("=== OUTROS EXEMPLOS ===")
    
    # Strings
    palavras = ["banana", "maçã", "uva", "abacaxi"]
    print(f"Palavras ordenadas: {bubble_sort(palavras)}")
    
    # Lista já ordenada
    ordenada = [1, 2, 3, 4, 5]
    print(f"Lista já ordenada: {bubble_sort(ordenada)}")
    
    # Lista em ordem decrescente
    decrescente = [5, 4, 3, 2, 1]
    print(f"Lista decrescente ordenada: {bubble_sort(decrescente)}")