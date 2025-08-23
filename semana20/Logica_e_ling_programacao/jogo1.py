import random  # para gerar números aleatórios

# Lista de mensagens
mensagens = [
    "Boa tentativa!",
    "Quase lá!",
    "Continue tentando!",
    "Você consegue!",
    "Não desista!"
]

print("🎲 Bem-vindo ao jogo: Adivinhe o número! 🎲")
print("Tente adivinhar o número secreto entre 1 e 10.\n")

# Gerar número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

tentativas = 0
acertou = False

# Enquanto não acertar, o jogo continua
while not acertou:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        acertou = True
    else:
        # Escolher uma mensagem aleatória da lista
        dica = random.choice(mensagens)
        if chute < numero_secreto:
            print(f"{dica} O número é MAIOR que {chute}.")
        else:
            print(f"{dica} O número é MENOR que {chute}.")

print("\nObrigado por jogar! 😄")

# Exemplo de uso do 'for' no final:
print("\nVeja uma contagem especial só para você:")
for i in range(1, 6):
    print(f"🔢 Número {i}")

