
while True:
    direita = 0
    esquerda = 0
    direcao = 0

    nComandos = int(input("Insira a quantidade de comandos dada pelo sargento: "))
    
    if nComandos == 0:
        break

    ordem = input('Informe os comandos: ').upper()
    
    for i in ordem:
        if i == 'D':
            direita += 1
        if i == 'E':
            esquerda += 1

    direcao = direita - esquerda
    direcao = direcao % 4

    if direcao == 0:
        print('N')
    elif direcao == 1:
        print('L')
    elif direcao == 2:
        print('S')
    elif direcao == 3:
        print('O')
    

#print('d',direita)
#print('e',esquerda)

