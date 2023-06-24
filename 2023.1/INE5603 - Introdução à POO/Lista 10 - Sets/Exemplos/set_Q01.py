futebol = {'A', 'B', 'C', 'D'}
natacao = {'B', 'D', 'E'}
volei = {'D', 'F', 'G'}
basquete = {'A', 'H', 'I'}

total = set()

while True:
    print('\nMENU')
    print('1 - Mostrar a relação de alunos matriculados por modalidade')
    print('2 - Matrícula de novos alunos')
    print('3 - Verificação de alunos aptos para o desconto')
    print('4 - Total de alunos por modalidade e total do Centro de Treinamento')
    n = int(input('\nDigite a opção escolhida: '))
    
    while n < 0 or n > 4:
        n = int(input('Opção Inválida. Digite novamente a opção escolhida: '))
    
    if n == 1:
        print(f'Alunos matriculados no futebol: {futebol}')
        print(f'Alunos matriculados na natação: {natacao}')
        print(f'Alunos matriculados no vôlei: {volei}')
        print(f'Alunos matriculados no basquete: {basquete}')
    
    if n == 2:
        fut = int(input('Digite o número de novos alunos no futebol: '))
        for x in range(fut):
            futebol.add(input(f'Digite o nome do aluno novo: '))
        
        nat = int(input('Digite o número de novos alunos na natação: '))
        for y in range(nat):
            natacao.add(input(f'Digite o nome do aluno novo: '))
        
        vol = int(input('Digite o número de novos alunos no vôlei: '))
        for z in range(vol):
            volei.add(input(f'Digite o nome do aluno novo: '))
        
        bas = int(input('Digite o número de novos alunos no basquete: '))
        for w in range(bas):
            basquete.add(input(f'Digite o nome do aluno novo: '))
    
    if n == 3:
        for a in futebol.intersection(natacao):
            total.add(a)
        for b in futebol.intersection(volei):
            total.add(b)
        for c in futebol.intersection(basquete):
            total.add(c)
        for d in natacao.intersection(volei):
            total.add(d)
        for e in natacao.intersection(basquete):
            total.add(e)
        for f in volei.intersection(basquete):
            total.add(f)
        for g in futebol.intersection(natacao, volei):
            total.add(g)
        for h in futebol.intersection(volei, basquete):
            total.add(h)
        for i in futebol.intersection(natacao, basquete):
            total.add(i)
        for j in natacao.intersection(volei, basquete):
            total.add(j)
        for k in futebol.intersection(volei, basquete, natacao):
            total.add(k)

        print(f'Existem {len(total)} alunos matriculados em mais de uma modalidade.')
        print(f'Os alunos que possuem direito ao desconto são {total}')
    
    if n == 4:
        total = futebol.union(natacao, volei, basquete)
        print(f'Na modalidade futebol estão matriculados {len(futebol)} alunos.')
        print(f'Na modalidade natação estão matriculados {len(natacao)} alunos.')
        print(f'Na modalidade vôlei estão matriculados {len(volei)} alunos.')
        print(f'Na modalidade basquete estão matriculados {len(basquete)} alunos.')
        print(f'No Centro de Treinamento estão matriculados {len(total)} alunos.')
    
    continuar = input('Você deseja continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
    