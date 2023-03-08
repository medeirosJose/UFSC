#Exercício 1012
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

TRIANGULO = a * c / 2
CIRCULO =  3.14159 * (c*c)
TRAPEZIO = ((a + b) * c) / 2 
QUADRADO = b * b 
RETANGULO = a * b

print("\nTRIANGULO = {:.3f}".format(TRIANGULO))
print("CIRCULO = {:.3f}".format(CIRCULO))
print("TRAPEZIO = {:.3f}".format(TRAPEZIO))
print("QUADRADO = {:.3f}".format(QUADRADO))
print("RETANGULO = {:.3f}".format(RETANGULO))