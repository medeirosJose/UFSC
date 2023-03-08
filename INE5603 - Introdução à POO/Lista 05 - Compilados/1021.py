valor = float(input("Digite o valor em reais: "))

if valor > 0 and valor < 1000000:
    nota100 = valor // 100
    resto = valor%100

    nota50 = resto // 50
    resto = resto%50

    nota20 = resto // 20
    resto = resto%20

    nota10 = resto // 10
    resto = resto%10

    nota5 = resto // 5
    resto = resto%5

    nota2 = resto // 2
    resto = resto%2

    moeda1 = resto // 1
    resto = resto%1

    moeda50 = resto // 0.5
    resto = resto%0.5

    moeda25 = resto // 0.25
    resto = resto%0.25

    moeda10 = resto // 0.10
    resto = resto%0.10

    moeda05 = resto // 0.05
    resto = resto%0.05

    moeda01 = resto // 0.01

    print(valor)
    print()
    print(nota100, "nota(s) de R$ 100,00")
    print(nota50, "nota(s) de R$ 50,00")
    print(nota20, "nota(s) de R$ 20,00")
    print(nota10, "nota(s) de R$ 10,00")
    print(nota5, "nota(s) de R$ 5,00")
    print(nota2, "nota(s) de R$ 2,00")
    print(moeda1, "moeda(s) de R$ 1,00")
    print(moeda50, "moeda(s) de R$ 0,50")
    print(moeda25, "moeda(s) de R$ 0.25")
    print(moeda10, "moeda(s) de R$ 0.10 ")
    print(moeda05, "moeda(s) de R$ 0.05")
    print(moeda01, "moeda(s) de R$ 0.01")
    
else:
    print("Insira um valor válido.")