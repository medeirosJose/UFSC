lista = []
listaAux = []
cinco = 0
flag = False
cont = 0

while True:
    cont += 1
    num = int(input(f"Informe o {cont}º número: "))
    lista.append(num)
    mais = input("Deseja adicionar mais? [s/n] ").upper()
    if mais == 'N':
        break

for i in lista:
    if i == 5:
        flag = True
        cinco += 1

listaAux = lista[:]
listaAux.sort(reverse=True)
print(listaAux)

#a
print('A lista possui',len(lista),'elementos.')
print('Em ordem reversa, a lista é ->',listaAux)

if flag == True:
    print(f'O número 5 está presente na lista, aparecendo um total de {cinco} vez(es).')
else:
    print("O número 5 não está presente na lista.")

print('Lista original ->',lista)
