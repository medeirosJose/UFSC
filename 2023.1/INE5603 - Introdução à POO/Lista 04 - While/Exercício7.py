codigo = 0
alc = 0
gas = 0
die = 0

while codigo > 4 or codigo < 4:
    codigo = int(input("Informe o código: "))
    if codigo > 4:
        print("Digite um código válido.")
    if codigo < 1:
        print("Digite um código válido.")
    if codigo == 1:
        alc += 1
    elif codigo == 2:
        gas += 1
    elif codigo == 3:
        die += 1
print("Muito obrigado! \n Alcool: {} \n Gasolina: {} \n Diesel: {}".format(alc,gas,die))