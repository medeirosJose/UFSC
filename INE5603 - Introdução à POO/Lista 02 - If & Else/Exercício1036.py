#Exercício1036
a = float(input("Digite o valor de A "))
b = float(input("Digite o valor de B "))
c = float(input("Digite o valor de C "))

delta = b**2 - 4*a*c

if delta > 0 and a != 0:
    raizDelta = pow(delta,0.5)
    r1= (-b + raizDelta) / (2*a)
    r2 = (-b - raizDelta) / (2*a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
else:
    print("Impossível calcular.")