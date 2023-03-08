valor = 1
i = j = k = l = 0
resto = 0
teste = 1

while True:
    valor = int(input("Digite o valor que deseja sacar: "))
    if valor == 0:
        break
    while valor >= 0:
        i = j = k = l = 0
        i = valor // 50
        resto = valor % 50
        
        j = resto // 10
        resto = resto % 10

        k = resto // 5
        resto = resto % 5

        l = resto

        print("Teste",teste)
        print(i,j,k,l)
        teste += 1
        
        valor = int(input("Digite outro valor que deseja sacar: "))
        if valor == 0:
           break
