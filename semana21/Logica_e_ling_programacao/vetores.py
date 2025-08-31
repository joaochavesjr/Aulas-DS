# Criando um vetor (lista) com números inteiros
numeros = [10, 20, 30, 40, 50]

# Acessando elementos
print("Primeiro elemento:", numeros[0])
print("Último elemento:", numeros[-1])
print("Meio:", numeros[1:-2])

# Percorrendo o vetor
print("Todos os elementos:")
for numero in numeros:
    print(numero)

# Adicionando um elemento
numeros.append(60)
print(f"Vetor após adicionar 60: {numeros}")

# Removendo um elemento
numeros.remove(30)
print(f"Vetor após remover 30: {numeros}")
