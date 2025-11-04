# Tarefas:
# - Crie um dicionário para armazenar a contagem de vendas de cada produto.
# - Crie outro dicionário para armazenar a receita total acumulada de cada produto.
# - Para cada venda registrada, atualize a contagem de vendas e a receita acumulada.
# - No final, exiba a contagem de vendas e a receita total para cada produto.

# Estrutura de dados para análise de vendas

vendas = [
    ('Produto A', 10, 5.0),
    ('Produto B', 5, 12.0),
    ('Produto A', 3, 5.0),
    ('Produto C', 8, 7.5),
    ('Produto B', 7, 12.0),
]

# Dicionários para armazenar os valores
total_venda = {}
total_receita = {}

for venda in vendas:
    produto, quantidade, preco = venda
    receita = quantidade * preco
    if produto in total_venda:
        total_venda[produto] += quantidade
        total_receita[produto] += receita
    else:
        total_venda[produto] = quantidade
        total_receita[produto] = receita

print('Total receita por produto', total_receita)
print('Contagem de venda por produto', total_venda)

