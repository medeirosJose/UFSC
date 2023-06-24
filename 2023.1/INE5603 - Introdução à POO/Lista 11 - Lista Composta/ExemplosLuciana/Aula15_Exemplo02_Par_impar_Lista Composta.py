#Aula 15 Lista Composta
'''Exemplo de aula 02
O usuário deve digitar 10 valores e cadastrar em uma lista composta única,
que mantenha separado os valores pares e ímpares.
No final, mostrar os valores pares e ímpares em ordem
crescente.'''

lista = [ [] , [] ]
num =0

for c in range (0,10):
    num = int (input("Digite um número: "))
    if num %2 ==0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"Valores digitados: {lista}")
print(f'Valores pares digitados: {lista[0]}')
print(f'Valores ímpares digitados: {lista[1]}')

print("\nUsando o sorted()")
print("Lista [0] - pares: ",sorted(lista[0]))
print("Lista [1] - ímpares: ",sorted(lista[1]))
print("Lista original: ", lista)

print("\nUsando sort()")
print(lista[0].sort())
print(lista[1].sort())
print("Lista original: ", lista)


