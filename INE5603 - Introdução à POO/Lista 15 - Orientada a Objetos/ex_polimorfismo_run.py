#polimorfismo

from ex_polimorfismo_Carro import Carro
from ex_polimorfismo_Veiculo import Veiculo

v1 = Veiculo('azul', 'Scania', 'R450', 10)
c1 = Carro('Grafite', 'Fiat', 'Argo', 25, 2020)

# instancia da classe Veiculo abastecendo
v1.__str__()
v1.abastecer(50)
v1.__str__()
v1.abastecer(30)
v1.__str__()
v1.abastecer(40)
v1.__str__()

print()
# instância da classe Carro abastecendo
# a instancia c1 irá executar o método abastecer que está definido na Classe Carro (polimorfismo)
# e irá executar o método __str__() na super classe Veiculo  (herança)
c1.__str__()
c1.abastecer(10)
c1.__str__()
c1.abastecer(20)
c1.__str__()
c1.abastecer(40)
c1.__str__()
