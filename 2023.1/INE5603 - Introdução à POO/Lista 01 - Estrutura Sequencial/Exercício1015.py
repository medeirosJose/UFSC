#Exercício 1015
import math
x1,y1 = [float(x) for x in input("Digite os dois valores de x1 e y1: ").split()]
x2,y2 = [float(x) for x in input("Digite os dois valores de x2 e y2: ").split()]

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4f}".format(distancia))