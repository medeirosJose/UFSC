'''
Crie um programa que crie uma matriz de dimensão nxn (n lido do teclado) e preencha 
com valores lidos pelo teclado.  
a)  Mostre a soma de todos os elementos pares da matriz 
b)  Mostre a média dos elementos da diagonal principal 
c)  Mostre o produto dos elementos da diagonal secundária 
d)  Mostre a média dos elementos acima da diagonal principal 
e)  Mostre a soma dos elementos da última coluna da matriz 
f)  Mostre o menor valor da primeira linha da matriz 
Importante: a matriz deve ser impressa na tela com formatação correta  
'''

matriz = []
somaPares = somaUltCol = mediaPrincipal = mediaSupPrincipal = menorValor = cont = 0
prodSecundaria = 1 

ordem = int(input("Informe a ordem da matriz: "))

for l in range(ordem):
    linha = []
    for c in range(ordem):
        numero = int(input("Digite o número que ficará armazenado {},{}: ".format(l, c)))
        linha.append(numero)
        #a)
        if not(numero%2):
            somaPares += numero

    print(linha)
    matriz.append(linha)


for l in range(0,ordem):
    for c in range(0,ordem):
        #b)
        if l == c:
            mediaPrincipal += matriz[l][c]
        #c)
        if c + l == ordem - 1:
            prodSecundaria = prodSecundaria * matriz[l][c]
        #d)
        if c > l:
            mediaSupPrincipal += matriz[l][c]
            cont += 1
        #e)
        if c == 2:
            somaUltCol += matriz[l][c]
        #f)
        if l == 0:
            if c == 0:
                menorValor = matriz[l][c]
            if matriz[l][c] < menorValor:
                menorValor = matriz[l][c]
        
        print(f'[{matriz[l][c]:^5}]',end=" ")
    print()

print('a) A soma dos números pares é igual a:',somaPares) #✔
print('b) A média dos elementos da diagonal principal é: {:.2f}'.format(mediaPrincipal/ordem)) #✔
print('c) O produto dos elementos da diagonal secundária é: {:.2f}'.format(prodSecundaria)) #✔
print('d) A média dos elementos acima da diagonal principal é: {:.2f}'.format(mediaSupPrincipal/cont)) #✔
print('e) A soma dos elementos da última coluna da matriz é:',somaUltCol) #✔
print('f) O menor valor da primeira linha da matriz é:',menorValor) #✔
