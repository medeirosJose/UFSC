'''Faça um programa que leia o nome e 3 notas de vários alunos e guarde em uma lista 
composta. No final mostre um boletim contendo a média de cada aluno e permita que 
sejam consultadas todas as notas parciais de cada aluno.'''

alunos = []

turma = []
media = []

quantidade = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade):
    aluno = str(input("Informe o nome do aluno: "))
    alunos.append(aluno)
    media.append(aluno)
    
    soma, notas = 0, 0

    for i in range(3):
        notas = int(input(f"Informe a {i+1}ª nota: "))
        soma += notas
        alunos.append(notas)

    media.append(soma/3)
    turma.append(alunos[:])
    alunos.clear()


print(f"{'---'*15}\n Boletim -> {media} \n{'---'*15}")

consultar = input('Deseja consultar todas as notas? ').upper()

if consultar == 'S':
    print(f"{'---'*15}\n Todas as notas -> {turma} \n{'---'*15}")