while True:
    horasAula = int(input("\nInforme as horas aulas da matéria: "))
    
    if horasAula == 0:
        break

    faltas = int(input("Insira a quantidade de faltas: "))

    atual = horasAula - (faltas*2)

    x = atual * 100
    y = horasAula

    resposta = x/y

    if resposta < 75:
        print('\nReprovado por FI. {:.1f}'.format(resposta))
    else:
        print('\nPresença máxima: {:.1f} ta safe'.format(resposta))
