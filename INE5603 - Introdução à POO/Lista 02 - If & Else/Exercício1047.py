#Exercício1047

horaInicial, minutoInicial, horaFinal, minutoFinal = [int(x) for x in input("Digite a hora inicial, o minuto inicial, a hora final e o minuto final: ").split()]

if horaInicial and minutoInicial == horaFinal and minutoFinal:
    print("O jogo durou 24 horas.")

elif (horaFinal > horaInicial) and (minutoFinal > minutoInicial):
    duracaoHora = horaFinal - horaInicial
    duracaoMin = minutoFinal - minutoInicial
    print("O jogo durou", duracaoHora,"hora(s) e ", duracaoMin, " minuto(s)")
    
elif (horaFinal < horaInicial) and (minutoFinal > minutoInicial):
    duracaoHora = (horaFinal - horaInicial) + 24
    duracaoMin = minutoFinal - minutoInicial
    print("O jogo durou", duracaoHora,"hora(s) e ", duracaoMin, " minuto(s)")

elif (horaInicial > horaFinal) and (minutoInicial > minutoFinal):
    duracaoHora = (horaFinal - horaInicial) + 23
    duracaoMin = (minutoFinal - minutoInicial)+ 60
    print("O jogo durou", duracaoHora,"hora(s) e ", duracaoMin, " minuto(s)")
    
elif (horaInicial < horaFinal) and (minutoInicial > minutoFinal):
    duracaoHora = (horaFinal - horaInicial)
    duracaoMin = (minutoFinal - minutoInicial)
    if duracaoMin < 0:
        duracaoMin = duracaoMin + 60
        duracaoHora = duracaoHora - 1
        print("O jogo durou", duracaoHora,"hora(s) e ", duracaoMin, " minuto(s)")
    else:
        print("O jogo durou", duracaoHora,"hora(s) e ", duracaoMin, " minuto(s)")