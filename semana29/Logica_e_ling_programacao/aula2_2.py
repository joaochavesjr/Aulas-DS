
NUM_NOTAS = 5
notas = []
contador = 0

while contador < NUM_NOTAS:
    nota = float(input(f"Digite a nota {contador + 1}: "))
    if nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        continue
    notas.append(nota)
    contador += 1

media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")


