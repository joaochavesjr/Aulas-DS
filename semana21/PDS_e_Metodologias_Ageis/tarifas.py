#Funcao utilitaria

class CalculadoraTarifas:

    @staticmethod # -> Decorator
    def calcular_tarifa_base():
        return 5
    
    @staticmethod
    def calcular_tarifa_transacao(numero_transacoes):
        if numero_transacoes > 10:
            return (numero_transacoes-10) * 1.5
        else:
            return 0
    
    @staticmethod
    def calcular_tarifa_saldo(saldo):
        if saldo < 1000:
            return 10
        else:
            return 0