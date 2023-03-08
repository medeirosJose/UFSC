#polimorfismo
class Veiculo:
    def __init__(self, cor, marca, modelo, tanque):
        self.tanque = tanque
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
       

    def abastecer(self, litros):
        print('Abastecendo...' + str(litros) + " litros")
        self.tanque += litros

    def __str__(self):
        print('O Veiculo: ' + self.marca + " " + self.modelo + " está com " +
              str(self.tanque) + " litros no tanque.")

