testes = int(input("Insira a quantidade de testes: "))

for i in range(testes):
    soma = 0
    numero = input("Insira a o valor: ")

    for i in numero:
        if i == '1':
            soma += 2
        elif i == '2' or i == '3' or i == '5':
            soma += 5
        elif i == '4':
            soma += 4
        elif i == '6' or i == '9' or i == '0':
            soma += 6
        elif i == '7':
            soma += 3
        elif i == '8':
            soma += 7
        
    print(soma,'leds')
    
