import random
import time

print("🐢🏁 Bem-vindo à Corrida das Tartarugas! 🏁🐢")

# Lista com os competidores
tartarugas = ["Leonardo", "Michelangelo", "Donatello", "Rafael"]

# Distância da corrida
distancia = 30  

# Posição inicial de cada tartaruga
posicoes = [0] * len(tartarugas)

vencedor = None

print("\nA corrida começou!\n")

# Enquanto ninguém chegou na linha de chegada
while vencedor is None:
    for i in range(len(tartarugas)):
        # Cada tartaruga anda um número aleatório de passos (1 a 3)
        passos = random.randint(1, 3)
        posicoes[i] += passos
        if posicoes[i] > distancia:
            posicoes[i] = distancia  # não ultrapassa a linha
        
        # Monta a barra de progresso da tartaruga
        pista = "-" * posicoes[i] + "🐢" + "-" * (distancia - posicoes[i])
        print(f"{tartarugas[i]:12}: {pista}")
        
        if posicoes[i] >= distancia:
            vencedor = tartarugas[i]
    
    print("\n" + "=" * 50 + "\n")
    time.sleep(0.5)  # pequena pausa para simular animação

print(f"\n🎉 O vencedor foi {vencedor}! 🎉")
