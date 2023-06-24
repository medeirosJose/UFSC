while True: 
    num1, num2 = input("Digite dois numeros: ").split()
    num1 = int(num1)
    num2 = int(num2)
    soma = 0

    '''
    if num1 > num2:
        maior = num1
        menor = num2
    elif num2 > num1:
        menor = num1
        maior = num2
    if menor == 0 or maior == 0:
        print('0 - Encerrando o loop...')
        break

    for i in range(menor,maior+1):
        soma += i
        print(i, end=' ')
    '''

    if num2 > num1:
        aux2 = num2
        num2 = num1
        num1 = aux2
    
    if num1 == 0 or num2 == 0:
        print('0 - Encerrando o loop...')
        break

    for i in range(num2,num1+1):
        soma += i
        print(i, end=' ')
    print("SUM = ", soma)




    

