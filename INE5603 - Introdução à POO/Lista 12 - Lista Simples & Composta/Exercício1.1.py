participantes, problemas = [int(x) for x in input('Informe a quantidade de parcipantes e quantidade de problemas: ').split()]
resultado = 0
competicao = []

for l in range(problemas):
    linha = []
    for c in range(participantes):
        numero = int(input("Digite o número que ficará armazenado {},{} :".format(l, c)))
        linha.append(numero)
    print(linha)
    #matriz[l] = linha
    competicao.append(linha)

print(competicao)

for lin in range(0,3):
    for col in range(0,3):
        print(f'[{competicao[lin][col]:^5}]',end=" ")
    print()

if resultado == 1:
    print('1')
if resultado == 2:
    print('2')
if resultado == 3:
    print('3')
if resultado == 4:
    print('4')
    
'''
1. Ninguém resolveu todos os problemas.
2. Todo problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).
3. Não há nenhum problema resolvido por todos.
4. Todos resolveram ao menos um problema (não necessariamente o mesmo).
'''