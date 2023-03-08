#Exercício 1003
a = int(input("Digite um valor inteiro "))
b = int(input("Digite outro valor inteiro "))
SOMA = int(a + b)
print("SOMA = " + str(SOMA))

#Exercício 1004
a = int(input("Digite um valor inteiro "))
b = int(input("Digite outro valor inteiro "))
PROD = int(a*b)
print ("PROD = " + str(PROD))

#Exercício 1005
a = float(input("Digite sua nota: "))
b = float(input("\nDigite sua outra nota: "))
a = 3.5*a
b = 7.5*b
MEDIA = (a + b) / 11
print("\nMEDIA = {:.5f}" .format(MEDIA))

#Exercício 1006
a = float(input("Digite sua primeira nota: "))
b = float(input("Digite sua segunda nota: "))
c = float(input("Digite sua terceira nota: "))
a = 2*a
b = 3*b
c = 5*c
MEDIA = (a+b+c)/10
print("\nMEDIA = {:.1f}".format(MEDIA))

#Exercício 1007
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
DIFERENCA = (a*b - c*d)
print("\nDIFERENCA = ", DIFERENCA)

#Exercício 1008
NUMBER = int(input("Digite seu número de funcionário: "))
numeroHoras = int(input("Digite seu número de horas trabalhadas: "))
valorHora = float(input("Digite quanto você ganha por hora trabalhada: "))
SALARY = numeroHoras * valorHora
print("NUMBER =",NUMBER)
print("SALARY = U$",SALARY)

#Exercício 2374
N = int(input("Qual a pressão desejada? "))
M = int(input("Qual a pressão lida pela bomba? "))
diferencaPressao = N - M
print("A diferença de pressão é de",diferencaPressao)


#Exercício 2413
t = int(input("Quantas pessoas clicaram no terceiro link? "))
primeiroLink = t * 4
print(primeiroLink)

#Exercício 1012
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

TRIANGULO = a * c / 2
CIRCULO =  3.14159 * (c*c)
TRAPEZIO = ((a + b) * c) / 2 
QUADRADO = b * b 
RETANGULO = a * b

print("\nTRIANGULO = {:.3f}".format(TRIANGULO))
print("CIRCULO = {:.3f}".format(CIRCULO))
print("TRAPEZIO = {:.3f}".format(TRAPEZIO))
print("QUADRADO = {:.3f}".format(QUADRADO))
print("RETANGULO = {:.3f}".format(RETANGULO))

#Exercício 1020
idade = int(input("Digite sua idade em dias: "))
ano = int(idade / 365)
restante = idade - (ano * 365)
mes = int (restante / 30)
dia = int(restante - (mes *30))

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")

#Exercício 1015
import math
x1,y1 = [float(x) for x in input("Digite os dois valores de x1 e y1: ").split()]
x2,y2 = [float(x) for x in input("Digite os dois valores de x2 e y2: ").split()]

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4f}".format(distancia))

#Exercício 1019
tempo = int(input("Digite a quantidade de segundos: "))
print(tempo)
horas = int(tempo / 3600)
restante = int(tempo%3600)
minutos = int(restante/60)
segundos = int(restante%60)

print(horas,":",minutos,":",segundos)

#Exercício 1017
horas = int(input("Quantas horas levou a viagem? "))
velocidadeMedia = int(input("Qual foi a velocidade média da viagem? "))
distancia = (horas * velocidadeMedia)
combustNecessario = distancia / 12
print("{:.3f}".format(combustNecessario))

#Exercício 1014
distancia = int(input("Qual foi a distância percorrida? "))
combustivel = float(input("Qual a quantidade de combustível gasto? "))
consumoMedio = float(distancia / combustivel)
print("{:.3f}".format(consumoMedio) + " km/l")


#Exercício 1009
nome = input(str("Digite seu nome: "))
salario = float(input("Qual seu salário? "))
vendas = float(input("Quantas vendas você realizou este mês? "))
total = salario + (0.15 * vendas)

print("TOTAL = R$ {:.2f}".format(total))






