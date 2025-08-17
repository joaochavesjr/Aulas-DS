
lista_quadrados = [x**2 for x in range(10)]
print(lista_quadrados)

print('-' * 20)

nomes = ['Ana', 'Bruno', 'Luis']
idades = [20, 17, 18]

for nome, idade in zip(nomes, idades):
    print(f'{nome} tem {idade} anos')


