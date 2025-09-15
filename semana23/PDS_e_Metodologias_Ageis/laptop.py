from produtoeletronico import ProdutoEletronico

class Laptop(ProdutoEletronico):
    def __init__(self, nome, marca, preco, memoria_ram):
        super().__init__(nome, marca, preco)

        self.memoria_ram = memoria_ram
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Memoria RAM: {self.memoria_ram}GB')

if __name__ == '__main__':
    obj = Laptop('Latitude', 'Dell', 4500.0, 16)
    obj.exibir_informacoes()