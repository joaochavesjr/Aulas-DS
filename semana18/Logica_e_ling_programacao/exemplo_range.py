
zero_ate_5 = range(6)
um_ate_5 = range(1, 6)
pares = range(0, 10, 2)

print('Números de 0 a 5:\r')
for i in zero_ate_5:
    print(i, end=' ')

print('\n\nNúmeros de 1 a 5:\r')
for i in um_ate_5:
    print(i, end=' ')

print('\n\nNúmeros pares de 0 a 10:', list(pares))