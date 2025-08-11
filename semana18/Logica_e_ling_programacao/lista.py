lista = ['maçã', 'banana', 'laranja']
print(lista, 'Tamanho:',len(lista))
lista.append('abacaxi')
print(lista, 'Tamanho:',len(lista))
lista.sort()
print(lista, 'Tamanho:',len(lista))
lista.remove('banana')
print(lista, 'Tamanho:',len(lista))

# Retorna tipo do objeto
print('\nTipo do objeto:', type(lista))

# Lista métodos e atributos do objeto
print('\nLista atributos do objeto:', dir(lista))

# Descreve a função
print('\nDocumentação da função:', lista.remove.__doc__)
