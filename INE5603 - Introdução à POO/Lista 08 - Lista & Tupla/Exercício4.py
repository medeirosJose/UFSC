"""4) Escreva  um  programa  que leia  uma  lista  X  contendo “N”  elementos  numéricos e  leia 
um  valor  numérico  qualquer  K.    Após  a  inserção  dos  dados  na  lista,  determine  e 
imprima a lista resultante da multiplicação de K pelos elementos de X. 
"""

n = int(input("Informe a quantidade de elementos da lista: "))
k = int(input("Digite o valor que deseja multiplicar a lista: "))

lista = []
for i in range(0,n):
    lista.append(int(input("Digite o valor: ")))
    
for i in range(0,n):
    lista[i] = lista[i] * 5

print("Lista multiplicada por",k,"-> ",lista)

