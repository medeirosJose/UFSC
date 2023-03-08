dimA, dimB, dimC = [int(x) for x in input("Informe as dimensões do colchão: ").split()] 
lar, alt = [int(x)for x in input("Informe a largura e altura da porta: ").split()]

if (dimA <= alt) and (dimB <= lar):
    print("S")
elif (dimA <= alt) and (dimC <= lar):
    print("S")
elif (dimB <= alt) and (dimA <= lar):
    print("S")
elif (dimB <= alt) and (dimC <= lar):
    print("S")
elif (dimC <= alt) and (dimA <= lar):
    print("S")
elif (dimC <= alt) and (dimB <= lar):
    print("S")
else:
    print("N")

