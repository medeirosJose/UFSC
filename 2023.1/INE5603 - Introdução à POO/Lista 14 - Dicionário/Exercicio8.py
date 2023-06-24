turma = []
alunos = {}
validas = ['EPR','EHD']
epr = ehd = intrusos = 0

numAlunos = int(input("Informe a quantidade de alunos na sala: "))

for i in range(numAlunos):
    alunos['matricula'] = int(input("Digite a matrícula: "))
    alunos['curso'] = input("Insira o curso: ")

    turma.append(alunos.copy())

for i in turma:

    if i['curso'] == 'EPR':
        epr += 1
    elif i['curso'] == 'EHD':
        ehd += 1
    else:
        intrusos += 1
print()
print('EPR:',epr)
print('EHD',ehd)
print('INTRUSOS:',intrusos)
print()
