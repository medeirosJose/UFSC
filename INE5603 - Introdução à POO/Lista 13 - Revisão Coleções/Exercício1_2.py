dois = tres = quatro = cinco = 0
lista = []

quantidade = int(input("Quantos números serão inseridos? "))

for i in range(quantidade):
    numero = int(input(f"Insira {i+1}º número: "))
    lista.append(numero)

for i in lista:
    if i % 2 == 0:
        dois += 1
    if i % 3 == 0:
        tres += 1
    if i % 4 == 0:
        quatro += 1 
    if i % 5 == 0:
        cinco += 1

print('{} múltiplo(s) de 2'.format(dois))
print('{} múltiplo(s) de 3'.format(tres))
print('{} múltiplo(s) de 4'.format(quatro))
print('{} múltiplo(s) de 5'.format(cinco))

print(lista)
