def cartesiano(x,y):
    if x > 0 and y > 0:
        print("Primeiro quadrante")
    
    elif x > 0 and y < 0:
        print("Quarto quadrante")
        
    elif x < 0 and y > 0:
        print("Segundo quadrante")
        
    elif x < 0 and y < 0:
        print("Terceiro quadrante")
        
    else:
        print("")

while True:

    x = float(input("Digite o valor de X: "))
    y = float(input("Digite o valor de Y: "))

    if x == 0 or y == 0:
        print("")
        break

    cartesiano(x,y)