#Polimorfismo

from ex_polimorfismo_Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, modelo, tanque, ano):
        super().__init__(cor, marca, modelo, tanque)
        self.ano = ano
        self.limit = 50
        
    def abastecer(self, litros):
        print('Tentando abastecer: ' + str(litros) + " litros")
        if self.tanque + litros > self.limit:
            print('Capacidade máxima alcançada, foi possível abastecer: ' +
                  str(self.limit -self.tanque) + ' litros.')
            self.tanque = self.limit
        else:
            self.tanque += litros
    
    def getAno(self):
        return self.ano
    
    