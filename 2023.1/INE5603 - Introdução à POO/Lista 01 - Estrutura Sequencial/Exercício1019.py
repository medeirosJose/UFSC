#Exercício 1019
tempo = int(input("Digite a quantidade de segundos: "))
print(tempo)
horas = int(tempo / 3600)
restante = int(tempo%3600)
minutos = int(restante/60)
segundos = int(restante%60)

print(horas,":",minutos,":",segundos)