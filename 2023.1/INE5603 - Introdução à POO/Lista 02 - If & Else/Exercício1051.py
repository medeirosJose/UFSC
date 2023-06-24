salario = float(input("Digite seu salário em R$: "))

#while (salario < 0):
    #salario = float(input("Salário inválido. Digite seu salário em R$: "))

if ((salario >= 0.00) and (salario <= 2000.00)):
    print("Isento.")
elif ((salario >= 2000.01) and (salario <= 3000.00)):
    impostoRenda = (salario - 2000) * 0.08
    print(impostoRenda)
elif ((salario >= 3000.01) and (salario <= 4500.00)):
    imposto1 = 1000 * 0.08
    imposto2 = (salario - 3000) * 0.18
    impostoRenda = imposto1 + imposto2
    print(impostoRenda)
    
elif salario > 4500:
    imposto1 = 1000 * 0.08
    imposto2 = 1500 * 0.18
    imposto3 = (salario - 4500) * 0.28
    impostoRenda = imposto1 + imposto2 + imposto3
    print("Imposto de renda é de {:.2f} ".format(impostoRenda))
    
    