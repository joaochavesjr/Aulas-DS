from abc import ABC, abstractmethod

# Classe base abstrata
class Veiculo(ABC):
    @abstractmethod
    def calcular_tempo_entrega(self, distancia):
        pass


class Carro(Veiculo):
    def calcular_tempo_entrega(self, distancia):
        # supondo uma velocidade media de 60Km/h para carros
        return distancia / 60
    
class Caminhao(Veiculo):
    def calcular_tempo_entrega(self, distancia):
        # supondo uma velocidade media de 40Km/h para carros
        return distancia / 40 # tempo em horas
    
class Bicicleta(Veiculo):
    def calcular_tempo_entrega(self, distancia):
        # supondo uma velocidade media de 15Km/h para carros
        return distancia / 15
    

    
def main():
    carro = Carro()
    caminhao = Caminhao()
    bicicleta = Bicicleta()

    distancia = 100 #Km

    # Calcular tempo de entrega para cada tipo de veiculo
    tempo_carro = carro.calcular_tempo_entrega(distancia)
    tempo_caminhao = caminhao.calcular_tempo_entrega(distancia)
    tempo_bicicleta = bicicleta.calcular_tempo_entrega(distancia)

    print("Tempo estimado de entrega para carro:", tempo_carro, "horas")
    print("Tempo estimado de entrega para caminhao:", tempo_caminhao, "horas")
    print("Tempo estimado de entrega para bicicleta:", tempo_bicicleta, "horas")


if __name__ == "__main__":
    main()