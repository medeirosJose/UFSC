from random import randint
matriz = []
soma = somaCol = somaSeg = 0


ordem = int(input("Ordem: "))

for linha in range(ordem):
    linha = []

    for coluna in range(ordem):
        numero = randint(0,10)
        if numero % 2 == 0:
            soma += numero
        if coluna == ordem-1:
            somaCol += numero
        linha.append(numero)
        
    matriz.append(linha)

for linha in range(0,ordem):
    for coluna in range(0,ordem):
        print(f'[{matriz[linha][coluna]:^5}]',end=" ")
    print()

print('Soma de todos os valores ->',soma)
print('Soma terceia coluna ->',somaCol)
