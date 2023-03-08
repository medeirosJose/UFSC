salarioNovo = 0
resposta = "S"

while resposta == 'S':
  salario = int(input("Digite seu salário para sofrer reajuste: "))
  salarioNovo = salario * 1.11
  desconto = salarioNovo - salario
  if desconto > 320:
    salarioNovo = salario + 320
    print("Seu salário alcançou o teto do INSS, tendo um ajuste de no máximo R$ 320.")

  print("\nSeu salário é de R$ {}".format(salarioNovo))
  resposta = input("Deseja continuar? [S/N] ").upper()