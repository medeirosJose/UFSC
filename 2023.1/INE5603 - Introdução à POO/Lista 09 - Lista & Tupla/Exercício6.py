vetorX = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    valor = int(input("Insira um valor: "))
    vetorX[i] = valor

    if vetorX[i] <= 0:
        valor = 1

    print('X[{}] = {} '.format(i,valor))

print('\n',vetorX)