#Exercício1323
while True:
    total = 0
    n = int(input("Digite o número de quadrados em cada lado do quadrado: "))
    if (n == 0):
        break
    for i in range(1,n+1):
        total = total + (i*i)
        
    print("O número total de quadrados é: ",total)