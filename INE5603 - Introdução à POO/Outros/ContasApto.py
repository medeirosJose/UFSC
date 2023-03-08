internet = float(input("Valor da conta da internet: "))
luz = float(input("Valor da conta de luz: "))
condominio = float(input("Valor da conta do condomínio: "))
aluguel = float(input("Valor da conta do aluguel: "))

total = (internet + luz + condominio + aluguel)

print("\nO valor total é de R$ {:.2f}.".format(total))
print("Cada um deve pagar R$ {:.2f}.".format(total/3))