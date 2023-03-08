'''celulas = int(input("Informe a quantidade de células no tabuleiro: "))
lista = []
listaResposta = []
minas = 0

for i in range(celulas):
    tabuleiro = int(input("Insira a composição do tabuleiro em 0's e 1's: "))
    lista.append(tabuleiro)

print(listaResposta)
'''

celulas = int(input('Informe a quantidade de células no tabuleiro: '))

lista = [0]*celulas
listaResposta = [0]*celulas
print("Insira a composição do tabuleiro em 0's e 1's: ")
for i in range(0,celulas):
    lista[i] = int(input('Posição {} -> '.format(i)))

for i in range(0,celulas):
    if i == 0:
        listaResposta[i] = lista[i+1]
        if lista[i] == 1:
            listaResposta[i] += 1
    elif i == celulas-1:
        listaResposta[i] = lista[i-1]
        if lista[i] == 1:
            listaResposta[i] += 1
    else:
        listaResposta[i] = lista[i-1]+lista[i+1]
        if lista[i] == 1:
            listaResposta[i] += 1

print('\nO resultado é: ')
for i in range(0,celulas):
    print(f'Posição {i} ->',listaResposta[i])