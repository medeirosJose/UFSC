'''
Ian Macedo
Exercício 7  1247 Guarda Costeira

O fugitivo, que a essa altura já está a bordo de sua
embarcação de fuga, pretende seguir perpendicularmente à
costa em direção ao limite de aguas internacionais, que
fica a 12 milhas náuticas de distância, onde estará são e
salvo das autoridades locais. Seu barco consegue percorrer
essa distância a uma velocidade constante de VF nós.

A Guarda Costeira pretende interceptá-lo, e sua embarcacão
tem uma velocidade constante de VG nós. Supondo que ambas
as embarcações partam da costa exatamente no mesmo instante,
com uma distância de D milhas náuticas entre elas, será
possível a Guarda Costeira alcançar o ladrão antes do
limite de aguas internacionais?

Assuma que a costa da Nlogônia é perfeitamente retilínea
e o mar bastante calmo, de forma a permitir uma trajetória
tão retilínea quanto a costa.
'''
# limite de 12 milhas nauticas
# o barco do fugitivo anda na velocidade VF
# a guarda costeira anda na velocidade VG
# há uma distância D entre eles
# é possível a guarda alcançar o ladrão?

while True:
    D = int(input("Informe a distância entre eles: "))
    VF = int(input("Digite a velocidade do fugitivo: "))
    VG = int(input("Informe a velocidade da guarda: "))
    
    #calcula hipotenusa do triangulo
    #hipotenuza = maior lado do triângulo retângulo
    #h**2 = a**2 + b**2  (considerando a e b os catetos)
    distancia = (12*12 + D*D) ** 0.5
    # h = distância o que queremos descobrir
    # a = 12 = distância limite (milhas nauticas fornecida no enunciado)
    # b = distância entre barco do Fugitivo e barco da Guarda
    
    # como calcular a velocidade pela distância e tempo:  D = T * V
    #tempo que Fugitivo chegaria em águas internacionais
    TF = 12 / VF
    #tempo que a guarda costeira chegará em aguas internacionais
    TG = distancia / VG
    
    if TG <= TF:
        print("S")
    else:
        print("N")
    
    dnv = str(input("Testar novamente? [S/N]")).upper()
    if dnv == "N":
        break