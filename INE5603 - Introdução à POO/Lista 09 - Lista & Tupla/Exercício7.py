vetorN = []

valor = int(input("Insira o valor inicial: "))

for i in range(10):
    if i == 0:
        vetorN.append(valor)
    else:
        vetorN.append(valor)
        valor = valor * 2
    print('N[{}] = {} '.format(i,valor))
    
