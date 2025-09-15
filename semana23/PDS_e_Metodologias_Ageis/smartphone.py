from produtoeletronico import ProdutoEletronico

class Smartphone(ProdutoEletronico):
    def __init__(self, nome, marca, preco, capacidade_armazenamento):
        super().__init__(nome, marca, preco)

        self.capacidade_armazenamento = capacidade_armazenamento
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Capacidade de Armazenamento: {self.capacidade_armazenamento}GB')


if __name__ == '__main__':
    obj = Smartphone('IPhone16', 'Apple', 5000.0, 128)
    obj.exibir_informacoes()