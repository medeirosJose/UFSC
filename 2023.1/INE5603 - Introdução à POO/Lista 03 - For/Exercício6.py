#Altere o programa de cálculo dos números primos (exercício 5), informando, caso
#o número não seja primo, por qual(is) número(s) ele é divisível.

primo = 0
numero = int(input("Digite um número inteiro: "))

for i in range(numero+1):
    if (numero % (i+1) == 0):
        primo += 1
    
if primo > 2:
    print(numero, "não é um número primo é divisível por ")
    for i in range(numero+1):
        if (numero % (i+1) == 0):
            print(i+1)
else:
    print(numero, "é um número primo")
    