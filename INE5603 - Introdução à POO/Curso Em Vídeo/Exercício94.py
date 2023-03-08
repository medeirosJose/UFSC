
pessoa = {}

quantidade = 0
soma = 0
media = 0

pessoasAcima = []
mulheres = []
grupo = []

while True:
    pessoa['nome'] = input('Nome: ')

    pessoa['sexo'] = input('Sexo: ').upper()

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    
    grupo.append(pessoa.copy())
    quantidade += 1

    print()
    continuar = str(input("Deseja continuar? [S/N] ").upper())
    if continuar == 'N':
        break
    print()

media = soma / quantidade

for i in range(len(grupo)):
    for k,v in grupo[i].items():
        if k == 'sexo' and v == 'F':    
            mulheres.append(grupo[i]['nome'])
        if k == 'idade' and v > media:
            pessoasAcima.append(grupo[i]['nome'])

print('\nForam cadastradas',quantidade,'pessoas.')
print('A média do grupo é de',media,'anos')
print('A lista com todas as mulheres ->',mulheres)
print('A lista com todas as pessoas com idade acima de',media,', anos ->',pessoasAcima)
