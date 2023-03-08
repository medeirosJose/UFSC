n = int(input("Digite a quantidade de bandejas: "))
coposQuebrados = 0

for i in range(n):
    latas, copos = input("Latas e Copos: ").split()
    latas = int(latas)
    copos = int(copos)
    
    if latas > copos:
        coposQuebrados += copos
print(coposQuebrados)