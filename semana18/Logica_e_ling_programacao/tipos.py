# Tipos primitivos
booleano = 1 == 1 
inteiro = 10 
flutuante = 10.123
texto = 'Texto'
lista = [inteiro, flutuante, texto, booleano]

for obj in lista:
    print(f'O objeto {obj} é do tipo {type(obj)}')

print('\nInteiro:', str(inteiro), hex(inteiro), bin(inteiro))
print('\nFlutuante:', str(flutuante), round(flutuante, 2), int(flutuante))
print('\nTexto:', texto, len(texto), texto.upper())
print('\nBooleano:', booleano, not booleano)
