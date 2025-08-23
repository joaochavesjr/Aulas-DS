import random

print("🐢🏁 Bem-vindo à Corrida das Tartarugas! 🏁🐢")

# Lista com os competidores
tartarugas = ["Leonardo", "Michelangelo", "Donatello", "Rafael"]

# Distância da corrida
distancia = 20

# Mostrar os participantes com um for
print("\nParticipantes da corrida:")
for t in tartarugas:
    print(f"- {t}")

print("\nA corrida começou!\n")

# Posição inicial de cada tartaruga
posicoes = [0, 0, 0, 0]

vencedor = None

# Enquanto ninguém chegou na linha de chegada
while vencedor is None:
    for i in range(len(tartarugas)):
        # Cada tartaruga anda um número aleatório de passos (1 a 3)
        passos = random.randint(1, 3)
        posicoes[i] += passos
        
        print(f"{tartarugas[i]} andou {passos} passos. (Total: {posicoes[i]})")
        
        if posicoes[i] >= distancia:
            vencedor = tartarugas[i]
            break  # sai do for, já temos um vencedor!
    
    print("-" * 30)  # separador visual

print(f"\n🎉 O vencedor foi {vencedor}! 🎉")

