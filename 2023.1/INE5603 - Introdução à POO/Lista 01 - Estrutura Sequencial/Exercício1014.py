#Exercício 1014
distancia = int(input("Qual foi a distância percorrida? "))
combustivel = float(input("Qual a quantidade de combustível gasto? "))
consumoMedio = float(distancia / combustivel)
print("{:.3f}".format(consumoMedio) + " km/l")