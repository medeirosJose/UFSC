teste = int(input("Digite a quantidade de testes: "))
cont = 0

a = int(input("Seguindo a planificação do dado, insira o primeiro valor: "))
b, c, d, e = [int(x) for x in input("Digite outros 4 valores: ").split()]
f = int(input("Digite o último valor: "))

if a + f == 7:
    cont += 1
if b + d == 7:
    cont += 1
if c + e == 7:
    cont += 1

if cont == 3:
    print("SIM")
else:
    print("NÃO")