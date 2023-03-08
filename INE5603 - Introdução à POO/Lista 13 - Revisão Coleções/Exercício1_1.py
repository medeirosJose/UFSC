
lista = []
posMaior = 0
posSegundoMaior = -1

suspeitos = int(input("Há quantos suspeitos? "))

for i in range(suspeitos):
    classificação = int(input(f"Informe o quão suspeita a {i+1}ª pessoa é: "))
    lista.append(classificação)

    if lista[posSegundoMaior] < lista[i] or i == 0:
        if lista[posMaior] < lista[i]:
            posSegundoMaior = posMaior
            posMaior = i
            
        else:
            posSegundoMaior = i
           

#1 15 3 5 2

print(posSegundoMaior+1)
