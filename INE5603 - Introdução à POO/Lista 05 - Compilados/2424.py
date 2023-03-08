falha = 0
x, y = input("Insira as coordenadas: ").split()
x = int(x)
y = int(y)
4
if x > 432 or x < 0:
    falha += 1
if y > 468 or y < 0:
    falha += 1
    
if falha >= 1:
    print("Fora")
else:
    print("Dentro")