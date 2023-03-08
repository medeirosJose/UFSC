
def menu(op):
    if op == 1:
        while True:
            jogador['nome'] = input('Informe seu nome: ')
            jogador['partidas'] = int(input('Quantas partidas foram jogadas? '))
            
            total = 0 
            gols = []
            for i in range(jogador['partidas']):
                gol = int(input(f'Na {i+1}ª partida, quantos gols vc fez? '))
                gols.append(gol)
                total += gol

            jogador['gols'] = gols
            jogador['total'] = total
            
            time.append(jogador.copy())
            print(jogador)
            
            continuar = input("Deseja continuar? [S/N] ").upper()
            if continuar == 'N':
                break
    elif op == 2:
        nome = str(input("Insira o nome que deseja buscar: "))
        for i in range(len(time)):
            if time[i]['nome'] == nome:
                e = time[i]
                for v in e.values():
                    print(v,end = ' ')
    else:
        print('Encerrando o programa...')

    return op

#main
jogador = {}
time = []

while True:
    print("\nBoas Vindas aos TimeBom")
    print("O que deseja fazer? " +
            '\n 1 - Cadastrar jogadores' +
            '\n 2 - Pesquisar por nome' +
            '\n 3 - Encerrar programa')
    op = menu(int(input()))
    if op == 3:
        break