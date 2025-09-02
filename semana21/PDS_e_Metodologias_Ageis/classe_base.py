from datetime import datetime
from tarifas import CalculadoraTarifas

class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []
        self.numero_transacoes = 0

    def depositar(self, valor):
        self.saldo += valor
        self.registrar_transacao("Deposito", valor)
        self.numero_transacoes += 1
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
            self.numero_transacoes += 1
            return True
        else:
            print("** Saldo insuficiente.")
            return False

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

    def calcular_tarifa(self):
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo(self.saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo
        