pares = 0
impares = 0

for i in range (10):
    numero = int(input("Digite um valor inteiro: "))
    
    if (numero % 2 != 0):
        impares += 1
    else:
        pares += 1
    
print("\nHá um total de {} número(s) impar(es)".format(impares))
print("Há um total de {} número(s) par(es)".format(pares))
