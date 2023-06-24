'''Entrada
A entrada consiste em diversos casos de teste e termina com EOF. 
A primeira linha contém um número X (3 ≤ X ≤ 20) que representa a quantidade de participantes no amigo secreto. 
Em seguida, as próximas X linhas irão conter o nome N e as 3 opções de presentes desejados P. 
Em seguida, as próximas linhas irão conter um nome N e um presente P, representando as consultas realizadas no programa.

Saída
Seu programa deverá informar se a pessoa acertou ou não na escolha do presente, 
retornando "Uhul! Seu amigo secreto vai adorar o/" caso acerto e, se não, "Tente Novamente!".'''

participantes = int(input("Quantos participarão? "))
secreto = {}
pessoas = []

desejo = {}
desejos = []

for i in range(participantes):
    secreto['pessoa'] = input("Digite o nome da pessoa: ")
    secreto['presente1'] = input("Primeira sugestão: ")
    secreto['presente2'] = input("Segunda sugestão: ")
    secreto['presente3'] = input("Terceira sugestão: ")
    pessoas.append(secreto.copy())
print(pessoas)

for i in range(participantes):
    desejo['nome'] = input("A quem vc dará o presente? ")
    desejo['presente'] = input('O q vc dará? ')
    
print(pessoas)