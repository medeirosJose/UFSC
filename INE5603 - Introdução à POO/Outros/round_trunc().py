#exemplo de como usar round no input

import math
A = 3/7
print(A)
valor = round(A,3)
print (valor)
#Ou você pode fazer direto:
A = round(3/7,3)
print (A)

b = math.trunc(9/7)
print(b)
c = 9/7
print(c)
print(round(9/7,2))

teste = round(float(input("Digite um número:")),2)
print(teste)
teste1= float(input("Digite o mesmo número:  (sem round)"))
print(teste1)

teste2 = math.trunc(float(input("Digite outro número (com vírgula):")))
print(teste2)
print(type (teste2))

print(" teste .f: {:.2f}".format(3.149))  #arredonda