pagamento = 0
valor = int(input("Digite o valor do produto: "))
print(" (1) - à vista \n (2) - 1x no cartão \n (3) - 2x no cartão \n (4) - 3x ou mais no cartão.")
#pagamento = int(input("Informe o método de pagamento: "))

#while pagamento < 1 or pagamento > 4:
pagamento = int(input("Informe o método de pagamento: "))
if pagamento == 1:
    print("Você recebeu 10% de desconto, e o valor será de R$ ",valor*0.9)
elif pagamento == 2:
    print("Você recebeu 5% de desconto, e o valor será de R$ ",valor*0.95)
elif pagamento == 3:
    print("O valor será de R$", valor)
elif pagamento == 4:
    print("O valor será de R$ ", valor * 1.2)