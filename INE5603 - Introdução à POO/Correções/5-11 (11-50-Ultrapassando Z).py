'''
Ian Macedo
Exercício 8  11 50 Ultrapassando Z

Faça um programa que leia dois inteiros: X e Z
(devem ser lidos tantos valores para Z quantos
necessários, até que seja digitado um valor
maior do que X para ele). Conte quantos
números inteiros devem ser somados em
sequência (considerando o X nesta soma) para
que a soma ultrapasse a Z o mínimo possível.
Escreva o valor final da contagem.

A entrada contém somente valores inteiros, um
por linha, podendo ser positivos ou negativos.
O primeiro valor da entrada será o valor de X.
A próxima linha da entrada irá conter Z. Se Z
não atender a especificação do problema, ele
deverá ser lido novamente, tantas vezes
quantas forem necessárias.
'''
X = int(input("Informe X: "))
Z = int(input("Informe Z: "))

while Z <= X:
    Z = int(input("Informe Z novamente: "))

cont = 0
soma = 0

while soma <= Z:
    soma = soma + (X + cont)
    cont += 1
    
print("Quantidade de inteiros: {}".format(cont))
