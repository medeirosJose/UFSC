numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
soma = 0
somaN = 0

for i in range(numero1,numero2-1):
    print(i+1)
    soma = i+1
    somaN = soma + somaN 
    
print("\nA soma dos números no intervalo entre {} e {} é de {}".format(numero1,numero2,somaN))