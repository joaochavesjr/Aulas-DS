from produtoeletronico import ProdutoEletronico

class Televisor(ProdutoEletronico):
    def __init__(self, nome, marca, preco, tamanho_tela):
        super().__init__(nome, marca, preco)

        self.tamanho_tela = tamanho_tela
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Tamanho da Tela: {self.tamanho_tela} polegadas')


if __name__ == '__main__':
    obj = Televisor('TV Oled', 'Samsung', 3000.0, 60)
    obj.exibir_informacoes()