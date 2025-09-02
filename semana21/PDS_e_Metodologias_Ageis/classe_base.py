from datetime import datetime

class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao("Deposito", valor)
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print("Saldo:", self.saldo)
    
    def registrar_transacao(self, tipo, valor):
        self.transacoes.append({"Tipo": tipo, "Valor": valor,
                                 "Data": datetime.now() })
    
    def extrato(self):
        if not self.transacoes:
            print('Nenhum transacao efetuada!')
        else:
            for t in self.transacoes:
                data_formatada = t['Data'].strftime('%H:%M %d/%m/%y')
                print(f'Tipo: {t['Tipo']}, Valor: {t['Valor']}, Data: {data_formatada}')