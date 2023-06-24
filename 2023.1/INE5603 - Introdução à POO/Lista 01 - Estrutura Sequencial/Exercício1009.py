#Exercício 1009
nome = input(str("Digite seu nome: "))
salario = float(input("Qual seu salário? "))
vendas = float(input("Quantas vendas você realizou este mês? "))
total = salario + (0.15 * vendas)

print("TOTAL = R$ {:.2f}".format(total))