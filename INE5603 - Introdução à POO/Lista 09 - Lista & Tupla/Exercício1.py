'''

1) Desenvolva um programa que leia 5 valores do teclado e guarde-os em um tupla. 
Ao final mostre: 
a) quantas vezes apareceu o número 9 
b) em que posição foi digitado o primeiro valor 3 
c) quais foram os números pares digitados

'''
lista = []
cont9 = 0
posicao = ''
contPar = 0

#for i in range(5):
#   valores = int(input("Insira os valores da tupla: "))
#   lista.append(valores)

#tupla = tuple(lista)

tupla = (int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')),
        int(input('Insira um número: ')))

for i in tupla:
    if i % 2 == 0:
        contPar += 1
    if i == 9:
        cont9 += 1

for pos, num in enumerate(tupla):
    if num == 3:
        posicao = pos
    else:
        posicao = 0
print('=-='*30)

print('A tupla foi:', tupla)
print("O número 9 apareceu", cont9,'vez(es).')
print('O primero valor de 3 apareceu na posição', posicao,'do iterador.')
print('Há um total de',contPar,'números pares.')

print('=-='*30)
