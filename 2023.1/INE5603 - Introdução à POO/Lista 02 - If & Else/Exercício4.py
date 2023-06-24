n1, n2, n3 = [int(x) for x in input("Digite as três notas: ").split()]

media = (n1+n2+n3) / 3

print("{:.1f}".format(media))

if media < 5:
    print("Reprovado.")
elif media >= 5 and media < 7:
    print("Em recuperação...")
elif media >= 7:
    print("Aprovado")