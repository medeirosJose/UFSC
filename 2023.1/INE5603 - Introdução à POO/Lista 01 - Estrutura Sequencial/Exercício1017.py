#Exercício 1017
horas = int(input("Quantas horas levou a viagem? "))
velocidadeMedia = int(input("Qual foi a velocidade média da viagem? "))
distancia = (horas * velocidadeMedia)
combustNecessario = distancia / 12
print("{:.3f}".format(combustNecessario))