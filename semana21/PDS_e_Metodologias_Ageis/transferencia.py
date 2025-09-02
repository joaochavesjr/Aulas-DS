from classe_base import ContaBancaria

def transferencia(origem, destino, valor):

    print(f'Saldos antes -> Origem: {origem.saldo}, Destino: {destino.saldo}')

    sacar_valor = origem.sacar(valor)
    if sacar_valor:
        destino.depositar(valor)
        print(f'Saldos depois -> Origem: {origem.saldo}, Destino: {destino.saldo}')
    else:
        print ('Saldo da conta de origem nao suficiente!')


conta1 = ContaBancaria('1234567', 200)
conta2 = ContaBancaria('8765431', 100)
transferencia(conta2, conta1, 100)

