class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}, Marca: {self.marca}, Preco: R${self.preco:.2f}')


