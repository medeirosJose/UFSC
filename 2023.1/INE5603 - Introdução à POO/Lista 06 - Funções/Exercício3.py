cont = 0

def ultrapassar(x,z):
    cont = 0
    soma = 0

    while soma <= z:
        soma = soma + (x + cont)
        cont += 1
    print("Cont =",cont)

x = int(input("Digite o valor de X: "))
z = int(input("Digite o valor de Z: "))

while x >= z:
    z = int(input("Digite o valor de Z novamente: "))

ultrapassar(x,z)