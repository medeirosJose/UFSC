'''
2) Crie um programa que gere 5 números aleatórios e os insira em uma tupla. Mostre a 
listagem dos números gerados, e indique o maior e o menor.
'''

from random import randint

numeros = (randint(1,100),
randint(1,100),
randint(1,100),
randint(1,100),
randint(1,100))

maior = 0
menor = 0

for i in range(5):
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        elif numeros[i] < menor:
            menor = numeros[i]

print(('=-'*30)+'=')
print('A tupla é',numeros)
print('Maior ->', maior)
print('Menor ->', menor)
print(('=-'*30)+'=')