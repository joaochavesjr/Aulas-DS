def abrir_caixa(n):
    if n == 0:
        print("🎁 Achou o presente!")
    else:
        print(f"Abrindo a caixa {n}...")
        abrir_caixa(n - 1)
        #print(f"Fechando a caixa {n}...")

# Testando com 3 caixas
abrir_caixa(3)
