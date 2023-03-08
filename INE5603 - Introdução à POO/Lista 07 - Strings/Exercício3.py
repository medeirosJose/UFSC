teste = int(input("Insira a quantidade de testes: "))

for i in range(teste):
    codigo = input("Insira os caracteres: ")
    
    x = int(codigo[0])
    y = codigo[1]
    z = int(codigo[2])

    if x == z:
            print(x*z)
    #isupper verifica se a string é maiúscula ou minúscula
    elif codigo[1].isupper():
       print(z-x)
    else:
            print(x+z)
