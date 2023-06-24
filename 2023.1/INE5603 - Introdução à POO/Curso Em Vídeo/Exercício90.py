while True:
    aluno = {}

    aluno['Nome'] = input('Nome: ')
    if aluno['Nome'] == 's':
        break

    aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
    print()

    if aluno['Media'] >= 5.75:
        aluno['Situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado'
    
    for k,v in aluno.items():
        print(f'{k} é {v}')
    print()

    print(aluno)