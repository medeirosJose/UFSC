
def resultado():
    contPositivos = 0
    soma = 0
    for i in range(6):
        num = float(input("Digite seu número: "))
        if num >= 0:
            contPositivos += 1
            soma += num
    print(contPositivos, "valores positivos")
    print("Média:",soma/contPositivos)

resultado()
    
