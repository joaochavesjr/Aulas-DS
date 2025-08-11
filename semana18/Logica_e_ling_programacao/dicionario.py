dicionario = {'Nome': 'Maria', 
              'Telefone': '555-1234'}

print(dicionario, 'Tamanho:',len(dicionario))

dicionario['Idade'] = 30
dicionario['Cidade'] = 'Campinas'

print(dicionario, 'Tamanho:',len(dicionario))

dicionario['Nome'] = 'Roberto'
print(dicionario, 'Tamanho:',len(dicionario))

del dicionario['Telefone']
print(dicionario, 'Tamanho:',len(dicionario))

for chave in dicionario:
    print(f'Chave: {chave} Valor: {dicionario[chave]}')