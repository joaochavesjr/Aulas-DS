import numpy as np

# Criando vetores com NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operações vetoriais
soma = a + b
produto = a * b
media = np.mean(a)

print("Vetor A:", a)
print("Vetor B:", b)
print("Soma A+B:", soma)
print("Produto A*B:", produto)
print("Média de A:", media)
