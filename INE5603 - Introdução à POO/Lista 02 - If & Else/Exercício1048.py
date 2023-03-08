#Exercício1048

salario = float(input("Digite seu salário para reajuste: "))

if salario >= 0 and salario <= 400.00:
    salarioNovo = salario + salario * 0.15
    print("Novo salário: ", salarioNovo)
    print("Reajuste ganho: ", salarioNovo - salario)
    print("Em percentual: 15%")

elif salario >= 400.01 and salario <= 800.00:
    salarioNovo = salario + salario * 0.12
    print("Novo salário: ", salarioNovo)
    print("Reajuste ganho: ", salarioNovo - salario)
    print("Em percentual: 12%")

elif salario >= 800.01 and salario <= 1200.00:
    salarioNovo = salario + salario * 0.10
    print("Novo salário: ", salarioNovo)
    print("Reajuste ganho: ", salarioNovo - salario)
    print("Em percentual: 10%")
elif salario >= 1200.01 and salario <= 2000.00:
    salarioNovo = salario + salario * 0.07
    print("Novo salário: ", salarioNovo)
    print("Reajuste ganho: ", salarioNovo - salario)
    print("Em percentual: 17%")
elif salario > 2000:
    salarioNovo = salario + salario * 0.04
    print("Novo salário: ", salarioNovo)
    print("Reajuste ganho: ", salarioNovo - salario)
    print("Em percentual: 14%")