'''
1)  Considere  um  Centro  de Treinamento  Esportivo  que  oferece  cursos  de  Futebol, 
Natação, Vôlei e Basquete.  Em função do grande número de desistência de seus 
alunos,  a  administração  resolveu  oferecer  um  desconto  de  50%  na  segunda 
modalidade. 
Para isso eles precisarão verificar os alunos em comum (matriculados em mais 
de um esporte). 
Você foi contratado para desenvolver um sistema que faça essa verificação e 
retorne as seguintes informações: 
1-  Mostre (imprimir na tela) a relação de alunos matriculados por modalidade: 
Futebol, Basquete, Natação e Vôlei. 
2-  Permita que novos alunos possam ser matriculados em qualquer uma das 
modalidades. 
3-  Faça a verificação se existem alunos matriculados em pelo menos 2 
modalidades. E indique quais os alunos que possuem direito ao desconto. 
4-  Indique o número total de alunos por modalidade, e também o número total 
de alunos do Centro de Treinamento.
'''

futebol = set()
natacao = set()
volei = set()
basquete = set()

print('=-'*45+'=')
print('* Menu *\n')
print('1 - Relação de Alunos matriculados por modalidade.')
print('2 - Matricular novos alunos.')
print('3 - Mostrar se há alunos matriculados em pelo menos dois, e mostrar alunos com direito ao desconto.')
#informar em qual ele possui desconto
print('4 - Número total de alunos por modalidade e número total de alunos do Centro de Treinamento.')
print('=-'*45+'=\n')

opcao = int(input('Escolha a opção desejada: '))

while opcao < 1 or opcao > 4:
    opcao = int(input('Opção inválida... informe novamente: '))

if opcao == 1:
    print('Total de alunos matriculados em futebol:',len(futebol))
    print('Total de alunos matriculados em futebol:',len(natacao))
    print('Total de alunos matriculados em futebol:',len(volei))
    print('Total de alunos matriculados em futebol:',len(basquete))

if opcao == 2:
    print('\nMatricular novos alunos em:\n')
    print('     1 - Futebol')
    print('     2 - Natação')
    print('     3 - Vôlei')
    print('     4 - Basquete')
    categoria = int(input('\nInforme a modalidade: '))

    while categoria < 0 or categoria > 4:
        categoria = int(input("Opção inválida... informe novamente: "))

    quantidade = int(input('Quantos alunos você quer matricular? '))

    if categoria == 1:
        for i in range(quantidade):
            aluno = input("Diga o nome do aluno: ")
            futebol.add(aluno)

    if categoria == 2:
        for i in range(quantidade):
            aluno = input("Digite o nome do aluno: ")
            natacao.add(aluno)

    if categoria == 3:
        for i in range(quantidade):
            aluno = input('Digite o nome do aluno: ')
            volei.add(aluno)

    if categoria == 4:
        for i in range(quantidade):
            aluno = input('Digite o nome do aluno: ')
            basquete.add(aluno)

if opcao == 3:
    print()

if opcao == 4:
    print()

