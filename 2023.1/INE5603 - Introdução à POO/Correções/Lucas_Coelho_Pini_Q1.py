#Questão 1 - Prova

#Entrada dos valores que dizem respeito às posições do helicóptero, do fugitivo, do policial e a direção que será percorrida (horária ou anti-horária)
h, p, f, d = input('Informe, respectivamente, as posições do helicóptero, do policial e do fugitivo, e a direção que o fugitivo corre (-1 = horário / 1 = anti-horário): ').split(' ')
#Informa qual o tipo de dado de cada variável
h = int(h)
p = int(p)
f = int(f)
d = int(d)

#Calcula as distâncias do helicóptero ao fugitivo, e do policial ao fugitivo
distancia_fh = (h-f)*d
distancia_fp = (p-f)*d

#Se alguma das distancias calculadas previamente for negativa, ele acrescentará 16 como um coeficiente de correção, assim ele ajusta a distância ao sentido que o fugitivo irá percorrer
if distancia_fh < 0:
    distancia_fh = distancia_fh + 16
if distancia_fp < 0:
    distancia_fp = distancia_fp + 16

#Impressão do resultado a partir de uma comparação dos valores das distâncias
if distancia_fh < distancia_fp:
    print('S')
elif distancia_fh > distancia_fp:
    print('N')


