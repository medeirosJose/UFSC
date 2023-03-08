#Exemplo 2
# preenchendo uma matriz usando a função append()

n = int(input("tamanho matriz :"))
matriz=list()

'''
linha = [1] * n
print("linha:",linha)
matriz = [linha] * n   #matriz é uma lista contendo outras n listas(linhas)
print("matriz:",matriz)
'''

#preenchendo uma matriz (utilizando append)
for l in range(n):
    linha = []
    for c in range(n):
        numero = int(input("Digite o número que ficará armazenado {},{} :".format(l, c)))
        linha.append(numero)
    print(linha)
    #matriz[l] = linha
    matriz.append(linha)

print(matriz)

for l in range(0,n):
    for c in range(0,n):
        print(f'[{matriz[l][c]:^5}]',end=" ")
    print()

