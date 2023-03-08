diaInicio = int(input("Digite o dia de início do evento: "))
horaI, minutoI, segundoI = [int(x) for x in input("Digite a hora, minuto e segundo no formato hh : mm : ss : ").split()]
diaTermino = int(input("Digite o dia de término do evento: "))
horaT, minutoT, segundoT = [int(x) for x in input("Digite a hora, minuto e segundo no formato hh : mm : ss do término do evento: ").split()]

tempoI = diaInicio * 24 * 60 * 60 + horaI * 60 * 60 + minutoI * 60 + segundoI
tempoT = diaTermino * 24 * 60 * 60 + horaT * 60 * 60 + minutoT * 60 + segundoT

tempoRestante = tempoT - tempoI
dias = tempoRestante//(24*60*60)
tempoRestante = tempoRestante%(24*60*60)

horas = tempoRestante//(60*60)
tempoRestante = tempoRestante%(60*60)

minutos = tempoRestante//60
tempoRestante = tempoRestante%60

segundos = tempoRestante

print(dias, "dia(s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")

