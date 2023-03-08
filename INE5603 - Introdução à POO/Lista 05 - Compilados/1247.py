distanciaMax = 12

d = int(input("Digite a distância entre a guarda e o fugitivo: "))
velF = int(input("Digite a velocidade do fugitivo: "))
velG = int(input("Digite a velocidade da guarda: "))

distancia = (12*12 + d*d)**0.5

tempoG = distancia / velG
tempoF = distanciaMax / velF

if tempoG <= tempoF:
    print("S")
else:
    print("N")