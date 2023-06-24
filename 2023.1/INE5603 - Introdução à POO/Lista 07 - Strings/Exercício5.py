cobaias = ratos = coelhos = sapos = 0

testes = int(input("Digite a quantidade de testes a serem realizados: "))

for i in range(testes):
    quantia, animal = input("Digite a quantidade de animais e a espécie: ").split()
    
    quantia = int(quantia)
    animal = animal.upper()
    
    while not(1 <= quantia <= 15):
        quantia = int(input("Digite uma quantidade válida: "))
    while (animal != 'C' and animal != 'R' and animal != 'S'):
        animal = input("Digite um animal válido: ")
        animal = animal.upper()

    cobaias += quantia

    if animal == 'C':
        coelhos += quantia
    if animal == 'R':
        ratos += quantia
    if animal == 'S':
        sapos += quantia

print("Total:",cobaias,"cobaias")
print('Total de coelhos:',coelhos)
print('Total de ratos:',ratos)
print('Total de sapos:',sapos)
print('Percentual de coelhos: {:.2f}'.format((coelhos/cobaias)*100),'%')
print('Percentual de ratos: {:.2f}'.format((ratos/cobaias)*100),'%')
print('Percentual de sapos: {:.2f}'.format((sapos/cobaias)*100),'%')