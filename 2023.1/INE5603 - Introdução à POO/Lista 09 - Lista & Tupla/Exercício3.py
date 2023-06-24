'''
3) Faça um programa que leia uma série de números inteiros e os armazene em uma lista. 
O programa deve mostrar a relação de todos os números repetidos. 
Se não houverem números repetidos, imprimir uma mensagem avisando que não existem 
números repetidos nesta lista. 
'''
lista = []
repetidos = []

numeros = int(input("Quantos números terá sua lista? "))

for i in range(numeros):
    item = int(input("Digite o número: "))
    lista.append(item)

for externo in range(len(lista)):
    for interno in range(len(lista)):
        if interno > externo and lista[interno] == lista[externo]:
            repetidos.append(lista[interno])

if len(repetidos) == 0:
    print("Não há números repetidos na lista.")
else:
    print("A relação dos números repetidos é :",repetidos)