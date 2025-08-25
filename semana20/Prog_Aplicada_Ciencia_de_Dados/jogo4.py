import random
import time
from colorama import Fore, Style, init

# Inicializa o colorama (necessário no Windows)
init(autoreset=True)

print("🐢🏁 Bem-vindo à Corrida das Tartarugas! 🏁🐢")

# Lista com os competidores e suas cores
tartarugas = [
    (Fore.BLUE, "Leonardo"),
    (Fore.YELLOW, "Michelangelo"),
    (Fore.MAGENTA, "Donatello"),
    (Fore.RED, "Rafael")
]

distancia = 30  # comprimento da pista
posicoes = [0] * len(tartarugas)
vencedor = None

print("\nA corrida começou!\n")

while vencedor is None:
    for i, (cor, nome) in enumerate(tartarugas):
        # Cada tartaruga anda um número aleatório de passos (1 a 3)
        passos = random.randint(1, 3)
        posicoes[i] += passos
        if posicoes[i] > distancia:
            posicoes[i] = distancia
        
        # Monta a barra de progresso da tartaruga
        pista = "-" * posicoes[i] + "🐢" + "-" * (distancia - posicoes[i])
        print(f"{cor}{nome:12}: {pista}{Style.RESET_ALL}")
        
        if posicoes[i] >= distancia and vencedor is None:
            vencedor = nome
    
    print("\n" + "=" * 50 + "\n")
    time.sleep(0.5)

print(f"\n🎉 {Fore.GREEN}O vencedor foi {vencedor}! 🎉{Style.RESET_ALL}")
