
primo = 0
numero = int(input("Digite um número inteiro: "))

for i in range(numero):
    if (numero % (i+1) == 0):
        primo += 1
    
if primo > 2:
    print(numero, "não é um número primo.")
else:
    print(numero, "é um número primo.")
    