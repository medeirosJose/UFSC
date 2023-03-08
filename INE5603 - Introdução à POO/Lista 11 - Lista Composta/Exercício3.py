pesquisa = []

participantes = int(input("Quantas pessoas serão entrevistadas? "))
for i in range(1,participantes+1):
    opiniao = input(f"Pessoa {i}, qual sua opinição acerca da economia brasileira?\n0 - satisfatório\n1 - insatisfatório\n")
    pesquisa.append(opiniao)
    print()

positivo = negativo = 0

for i in range(len(pesquisa)):
    if pesquisa[i] == '1':
        negativo += 1
    if pesquisa[i] == '0':
        positivo += 1

if positivo > negativo:
    print('S')
else:
    print('N')

