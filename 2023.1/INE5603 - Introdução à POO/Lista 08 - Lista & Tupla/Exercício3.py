import random

lista = []

for i in range(10):
    numero = random.randrange(1000,9999)
    lista.append(numero)

tupla = tuple(lista)

maior = 0
menor = 0

for i in range(10):
    if i == 0:
        maior = menor = tupla[i]
    else:
        if tupla[i] > maior:
            maior = tupla[i]
        elif tupla[i] < menor:
            menor = tupla[i]

posicaoMaior = tupla.index(maior) + 1
posicaoMenor = tupla.index(menor) + 1

print('=-='*45)
print('\nOs números gerados aleatóriamente foram:', tupla)
print('O maior valor da tupla é', maior ,'estando na posição', posicaoMaior )
print('O menor valor da tupla é', menor ,'estando na posição', posicaoMenor ,'\n')
print('=-='*45)
    
    