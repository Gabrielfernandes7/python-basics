class Carro:
    # construtor
    def __init__(self, marca, modelo):
        # atributos
        self.marca = marca
        self.modelo = modelo
    
    # métodos
    def correr(self):
        print("O carro está correndo")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

    def correr(self):
        super().correr()
        print("O carro está correndo eletricamente")

# Exemplo de uso corrigido
carro_electrico = CarroEletrico("Tesla", "Model S", 400)
carro_electrico.correr()
