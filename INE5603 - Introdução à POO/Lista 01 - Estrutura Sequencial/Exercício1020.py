#Exercício 1020
idade = int(input("Digite sua idade em dias: "))
ano = int(idade / 365)
restante = idade - (ano * 365)
mes = int (restante / 30)
dia = int(restante - (mes *30))

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")