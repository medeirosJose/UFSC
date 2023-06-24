'''
lista = list()
lista = []
'''
lista2= list(range(5))
print(lista2)

for i in range (0, len(lista2)):
    lista2[i] = lista2[i] + 5
print(lista2)

lista2.append("Pedro")
print(lista2)
print(len(lista2))
lista2.insert(1,"Ana")
print(lista2)
print(len(lista2))

