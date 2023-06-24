'''
1) Faça um programa que leia nome, idade e peso de várias pessoas, guardando estas 
informações em uma lista composta. Depois de sua execução mostre:
  1.1) quantas pessoas foram cadastradas
  1.2) uma lista com a(s) pessoa(s) mais pesada(s)
  1.3) uma lista com a(s) pessoa(s) mais leve(s)
  1.4) o número de pessoas acima de 20 anos (mostrar também o nome e idade de casa 
uma)
  1.5) o usuário define quantas pessoas serão cadastradas (Perguntar: Deseja continuar 
cadastrando?)
'''
dados = list()
cadastro = list()
maior = menor = 0

while True:

    dados.append(str(input("Digite o nome: ")))
    dados.append(int(input('Insire a idade: ')))
    dados.append(float(input('Insira o peso: ')))

    if len(cadastro) == 0:
        maior = menor = dados[1]

    else: 
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
        
    cadastro.append(dados[:])
    dados.clear()

    continuar = input("Deseja continuar ? [S/N] ").upper()
    if continuar == 'N':
        break

print()
print('=-'*5+'=','Output','=-'*5+'=')

print('\nAo todo, foram cadastradas',len(cadastro),'pessoas')

print('\nOs mais pesados foram: ')
for i in cadastro:
    if i[1] == maior:
        print(f'{i[0]}')

print('\nOs mais leves foram: ')
for i in cadastro:
    if i[1] == menor:
        print(f'{i[0]}')

print("\nOs maiores de 20 são: ")
idade = 0

for i in cadastro:
    if i[2] > 20:
        print(f"{i[0]} - {i[2]}")
        idade += 1

if idade == 0:
    print("Não há pessoas acima de 20 anos.")
if idade >= 1:
    print("Há {} pessoa(s) acima de 20 anos.".format(idade))