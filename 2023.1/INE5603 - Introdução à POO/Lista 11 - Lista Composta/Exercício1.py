'''
1)  a ordem da matriz será lida do teclado 
2)  o preenchimento da matriz pode ser aleatório (usando random) 
3)  imprimir a matriz antes e depois de efetuar o cálculo
'''

from random import randint
matriz = list()

ordem = int(input("Informe a ordem da matriz: "))

escolhida = int(input("Informe a linha que será feita a operação: "))

tipo = str(input("Escolhe a operação:\nS -> Soma\nM -> Média\n").upper())

for l in range(ordem):
    linha = []
    for c in range(ordem):
        numero = randint(0,10)
        linha.append(numero)
    matriz.append(linha)

print("\nMatriz original: ")
for l in range(0,ordem):
    for c in range(0,ordem):
        print(f'[{matriz[l][c]:^5}]',end=" ")
    print()

if tipo == 'S':
    soma = 0 
    for c in range(ordem):
        soma += matriz[escolhida-1][c]
    print('Soma dos elementos da linha {} é {}.'.format(escolhida,soma))


if tipo == 'M':
    media = 0
    soma = 0
    for c in range(ordem):
        soma += matriz[escolhida-1][c]
        media = soma / ordem
    print('A média dos elementos da linha {} é {}.'.format(escolhida,media))