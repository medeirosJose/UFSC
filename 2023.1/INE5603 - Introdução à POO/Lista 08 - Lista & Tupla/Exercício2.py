'''
2) Faça um programa que leia uma série de números inteiros e os armazene em uma lista. 
Em seguida, o programa deve determinar se nessa série de valores aparece algum valor 
repetido. 
Mostrar mensagem dizendo se existe ou não um número repetido! 
O número de elementos é definido pelo usuário.
'''

n = int(input("Informe a quantidade de números de elementos: "))
lista = []
repetido = False

for i in range(n):
    item = int(input("Digite o número: "))
    lista.append(item)

for externo in range(len(lista)):
    for interno in range(len(lista)):
        if interno > externo and lista[interno] == lista[externo]:
            print("Há um número repetindo ->", lista[interno])
            repetido = True

if not repetido:
    print('Não há números repetindo.')
 

