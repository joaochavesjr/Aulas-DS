class Carro:
    def __init__(self, marca, modelo, ano, cor, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preco = preco
        self.publico = 1

    def get_marca(self):
        return self.__marca

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        self.__preco = novo_preco * 1.05
        return self.__preco

### Uso
def exemplo():
    novo_carro = Carro('Fiat', 'Uno', 2010, 'Cinza', 30000)
    print(novo_carro.get_marca())

    print(novo_carro.publico)

    print('Preco atual', novo_carro.get_preco())
    print('Reajusta preco em 50.000,00')
    novo_carro.set_preco(50000)
    print('Preco Novo', novo_carro.get_preco())


if __name__ == "__main__":
    exemplo()