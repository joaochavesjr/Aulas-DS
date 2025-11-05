
NUM_NOTAS = 5
notas = []

for i in range(NUM_NOTAS):
    nota = float(input(f"Digite a nota {i + 1}: "))
    if nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        break
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")


