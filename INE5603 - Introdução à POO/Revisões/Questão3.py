while True:
    matriz = []
    linha, coluna = [int(x) for x in input("Digite ordem da matriz (linha e coluna): ").split()]
    
    if linha or coluna == 0:
        break
    if 1<= linha >= 100 or 1 <= coluna >= 100:
        break

    for l in range(linha):
        lista = []
        for c in range(coluna):
            lista.append(int(input("Digite o número que ficará armazenado {},{} :".format(l, c))))
        matriz.append(lista)

    matrizAux = [[0]*coluna for k in range(linha)]
    #print(matrizAux)

    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == 1:
                matrizAux[i][j] = 9
                #cima
                if i-1 >= 0:
                    if matriz[i-1][j] != 1:
                        matrizAux[i-1][j] += 1
                #baixo
                if i+1 < linha:
                    if matriz[i+1][j] != 1:
                        matrizAux[i+1][j] += 1
                #esquerda
                if j-1 >= 0:
                    if matriz[i][j-1] != 1:
                        matrizAux[i][j-1] += 1
                #direita
                if j+1 < coluna:
                    if matriz[i][j+1] != 1:
                        matrizAux[i][j+1] += 1

    for i in range(len(matrizAux)):
        print(matrizAux[i])

