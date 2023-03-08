'''
Após a morte de Ares, o último godofor, os outros deuses decidiram fazer um concurso 
para decidir quem seria o novo godofor. Porém seres de diversos universos tinham 
interesse na vaga. Por haver tantos candidatos os deuses estão com muita dificuldade 
para selecionar um deles, então eles decidiram recorrer a você o deus da programação, 
eles querem que você desenvolva um programa que decida quem será o novo godofor 
com base nos critérios definidos pelos deuses. 

Os candidatos serão avaliados com base em um atributo, o nível de poder do candidato. 
O godofor deve ser o candidato mais poderoso, caso ocorra empate o godofor será o 
candidato  com  o  menor  nome  lexicograficamente.  Se  ainda  assim  existir  empate, 
mostrar o nome dos candidatos finalistas.
'''

seres = int(input("Quantos seres? "))

maiorPoder = 0
compararNome = ''
deus = {}
deuses = []

for i in range(seres):
    deus['nome'] = str(input("Digite o nome do deus: "))
    deus['poder'] = int(input("Digite o poder do deus: "))

    if i == 0:
        maiorPoder = deus['poder']
        compararNome = deus['nome']

    elif maiorPoder < deus['poder']:
        maiorPoder = deus['poder']
        compararNome = deus['nome']

    elif maiorPoder == deus['poder']:
        if len(deus['nome']) < len(compararNome):
            compararNome = deus['nome']

    deuses.append(deus.copy())

print(compararNome)


