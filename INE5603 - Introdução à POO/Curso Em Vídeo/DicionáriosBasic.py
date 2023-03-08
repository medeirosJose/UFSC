filme = {}
locadora = []

for i in range(3):
    filme['titulo'] = input("Nome do filme: ")
    filme['ano'] = int(input('Ano do lançamento: '))
    filme['diretor'] = input('Diretor do filme: ')
    print()
    
    locadora.append(filme.copy())

print('Printando a lista de filmes separadamente: ')
for f in range(len(locadora)):
    print(locadora[i])

print('\nPrintando a lista toda de uma vez só: ')
print(locadora)
print()

print('Printando a lista toda, separada em keys e values: ')
for g in locadora:
    for k,v in g.items():
        print(f'O {k} é {v}')
    print()
