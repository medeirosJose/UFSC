from random import randint

matriz = []

pulos = int(input('Altura dos pulos: '))
quantia = int(input('Quantidade de canos: '))

pulo = [0]*quantia

for i in range(quantia):
    matriz.append(int(input('Insira a altura dos canos: ')))
    #canos = int(randint(0,10))
    #matriz.append(canos)

print('Original ->',matriz)
print('Matriz com os pulos ->',pulo)
