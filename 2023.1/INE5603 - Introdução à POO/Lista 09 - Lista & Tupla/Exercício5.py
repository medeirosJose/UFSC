listaX = []
listaY = []

for i in range(5):
    valorX = int(input('Insira os valores de X: '))
    listaX.append(valorX)

for i in range(5):
    valorY = int(input('Insira os valores de Y: '))
    listaY.append(valorY)

print(listaX)
print(listaY)

for i in range(5):
    if listaX[i] + listaY[i] == 2:
        print('N')
        break
    else:
        print('S')
        break
