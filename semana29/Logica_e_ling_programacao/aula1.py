# formula calculo percentual
# valor_final = valor_original * (1 - percentual_desconto / 100)

PRECO_PRODUTO = 10.0

num_pecas = int(input(">>> Digite o número de peças que deseja comprar: "))

preco_total = 0
preco_final = 0
desconto = 0

preco_total = PRECO_PRODUTO * num_pecas

if num_pecas <= 5:
    preco_final = preco_total

elif 6 <= num_pecas <= 10:

    preco_final = preco_total * 0.9
    desconto = 10

elif num_pecas > 10:
    preco_final = preco_total * 0.8
    desconto = 20

print(f"Num. peças compradas: {num_pecas}")
print(f"O preço total é: R$ {preco_total:.2f}")
print(f"O preço final é: R$ {preco_final:.2f}")
print(f"O desconto foi de: {desconto}%")

