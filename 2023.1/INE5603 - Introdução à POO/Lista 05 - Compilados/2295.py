#como limitar em duas casas decimais e ao mesmo tempo pedir todos os valores em uma linha só?

a, g, ra, rg = [float(x) for x in input("Digite os valores respectivos: ").split()]

custoA = ra * a 
custoG = rg * g

if a == g:
    print("G")
elif custoG > custoA:
    print("A")
elif custoA == custoG:
    print("G")
