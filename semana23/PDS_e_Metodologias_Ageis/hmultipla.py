class AnimalTerrestre:
    def locomover(self):
        print("Andando terrestremente")

class AnimalAquatico:
    def locomover(self):
        print("Nadando aquaticamente")
    
    def consequenadar(self):
        print('Consegue nadar!')

class Anfibio(AnimalTerrestre, AnimalAquatico):
    pass # A classe Anfíbio herda de ambas as classes

# Cria um objeto Anfíbio
anfibio = Anfibio()

# Chama o método locomover
anfibio.locomover()
# Saída: Andando terrestremente (A busca começa em AnimalTerrestre)
anfibio.consequenadar()
