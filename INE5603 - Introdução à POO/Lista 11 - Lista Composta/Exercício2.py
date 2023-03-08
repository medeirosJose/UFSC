'''
1)  ler o tamanho da matriz do teclado 
2)  deixar opção de preenchimento dos valores da matriz pelo teclado e também de 
forma randômica 
3)  imprimir a matriz
'''

from random import randint
matriz = []

ordem = int(input("Informe a ordem da matriz: "))
while ordem <= 0 or ordem > 12:
    ordem = int(input("Informe uma ordem entre 1 e 12: "))

#matriz2 = [[randint(0,10)] for k in range(ordem)]
#print(matriz2)

preencher = int(input("Você gostaria de preencher a matriz manualmente ou fazê-la de forma randômica?\n1 - Manualmente\n2 - Randomizar\n"))
while preencher >= 3 or preencher < 1:
    preencher = int(input("Informe uma opção entre 1 e 2: "))
    
while True:
    operacao = str(input("\nQual a operação a ser realizada?\nS -> Soma\nM -> Média\n").upper())
    if operacao == 'M' or operacao == 'S':
        break

if preencher == 1:
    for l in range(ordem):
        linha = []
        for c in range(ordem):
            numero = int(input("Digite o número que ficará armazenado {},{} :".format(l, c)))
            linha.append(numero)
        print(linha)
        matriz.append(linha)

elif preencher == 2:
    for l in range(ordem):
        linha = []
        for c in range(ordem):
            numero = randint(0,10)
            linha.append(numero)
        matriz.append(linha)

soma = 0
cont = 0

for l in range(0,ordem):
    for c in range(0,ordem):
        print(f'[{matriz[l][c]:^5}]',end=" ")
        if l > c:
            soma += matriz[l][c]
            cont += 1
    print()

if operacao == 'S':
    print('Soma ->',soma)

if operacao == 'M':
    print ('Média ->',(soma/cont))
