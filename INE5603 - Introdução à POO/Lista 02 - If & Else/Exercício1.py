valor = int(input("Insira o valor da casa: "))
salario = int(input("Informe seu salário: "))
anos = int(input("Em quantos anos irá pagar? "))

prestacaoMensal = valor / (anos * 12) 
if prestacaoMensal > salario * 0.3:
    print("Emprestimo negado.")
    #print(prestacaoMensal)
else:
    print("Empréstimo realizado com sucesso!")
    #print(prestacaoMensal)