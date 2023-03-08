'''
A entrada consiste de duas linhas apenas. Na primeira linha são dados seis números 
inteiros distintos entre 1 e 99, representando a aposta do Flavinho. A segunda linha 
contém os seis números inteiros distintos sorteados. 
Saída 
Seu programa deve imprimir uma linha contendo uma palavra: “terno”, “quadra”, 
“quina”  ou  “sena”;  caso  Flavinho  tenha  acertado,  respectivamente,  3,  4,  5,  ou  6 
números. Caso ele tenha acertado menos do que 3 números, imprima a palavra “azar”.'''

while True:
    lista = []
    sorteio = []
    cont = 0

    for i in range(6):
        numero = int(input(f"Informe o {i+1}º número: "))
        lista.append(numero)

    print()

    for i in range(6):
        aleatorio = int(input(f"Informe {i+1}ª resposta: "))
        sorteio.append(aleatorio)

    print()

    for i in range(len(lista)):
        for k in range(len(sorteio)):
            if lista[i] == sorteio[k]:
                cont += 1

    print('Números apostados -',lista)
    print('\nNúmeros do Sorteio -',sorteio)

    print()

    if cont < 3:
        print('Azar.')
    elif cont == 3:
        print('Terno')
    elif cont == 4:
        print('Quadra')
    elif cont == 5:
        print('Quina')
    elif cont == 6:
        print('!!! Sena !!!')
    else:
        print("Algo de errado não está certo.")
    print(cont)
    continuar = input('\nContinuar? [S/N] ').upper()

    if continuar == 'N':
        break