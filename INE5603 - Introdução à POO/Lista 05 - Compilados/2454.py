p,r = input("Indique as posições com 0 ou 1: ").split()
p = int(p)
r = int(r)

if p == 0:
    print('C')
elif p == 1:
    if r == 1:
        print('A')
    else:
        print('B')