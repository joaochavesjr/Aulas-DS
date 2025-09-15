import os
import time
import sys

def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_array_visual(arr, comparing=None, swapped=None, title=""):
    """
    Imprime array com representação visual usando caracteres
    """
    print(f"\n{title}")
    print("=" * 60)
    
    # Normaliza os valores para a altura das barras
    if arr:
        max_val = max(arr)
        heights = [int((val / max_val) * 10) for val in arr]
    else:
        heights = []
    
    # Desenha as barras de cima para baixo
    for level in range(10, 0, -1):
        line = ""
        for i, height in enumerate(heights):
            if height >= level:
                if comparing and i in comparing:
                    line += "██"  # Barras sendo comparadas
                elif swapped and i in swapped:
                    line += "▓▓"  # Barras que foram trocadas
                else:
                    line += "██"  # Barras normais
            else:
                line += "  "
            line += " "
        print(line)
    
    # Imprime os valores
    print("─" * (len(arr) * 3))
    values_line = ""
    for val in arr:
        values_line += f"{val:2d} "
    print(values_line)
    
    # Legenda de cores
    if comparing:
        print(f"\n🔍 Comparando: {[arr[i] for i in comparing]}")
    if swapped:
        print(f"🔄 Trocados: {[arr[i] for i in swapped]}")

def bubble_sort_animated_terminal(arr):
    """
    Bubble Sort com animação no terminal
    """
    arr = arr.copy()
    n = len(arr)
    
    clear_screen()
    print_array_visual(arr, title="🎯 BUBBLE SORT - Estado Inicial")
    time.sleep(2)
    
    for i in range(n):
        print(f"\n🔄 Passada {i + 1}")
        
        for j in range(0, n - i - 1):
            clear_screen()
            print_array_visual(arr, comparing=[j, j+1], 
                             title=f"🔍 Passada {i + 1} - Comparando posições {j} e {j+1}")
            time.sleep(1)
            
            if arr[j] > arr[j + 1]:
                # Mostra a troca
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                clear_screen()
                print_array_visual(arr, swapped=[j, j+1],
                                 title=f"🔄 Passada {i + 1} - TROCOU! {arr[j+1]} ↔ {arr[j]}")
                time.sleep(1.5)
    
    clear_screen()
    print_array_visual(arr, title="✅ ORDENAÇÃO COMPLETA!")
    return arr

# Exemplo de uso
if __name__ == "__main__":
    numeros = [5, 2, 8, 1, 9, 3]
    print("🚀 Iniciando Bubble Sort animado...")
    time.sleep(1)
    resultado = bubble_sort_animated_terminal(numeros)