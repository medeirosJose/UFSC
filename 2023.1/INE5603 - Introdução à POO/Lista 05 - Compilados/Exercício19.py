#Exercício19

l1, l2, l3 = input("Informe os três lados do triângulo: ").split()

l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

if l1+l2 > l3:
    if l1 == l2 and l2 == l3:
        print("Triângulo equilátero.")