#Exemplo 01 - Lista Composta
"""
Faça um programa que leia nome, idade e peso de várias pessoas, guardando estas informações
em uma lista composta.
Depois de sua execução mostre:
1.1) quantas pessoas foram cadastradas
1.2) a relação dos nomes da(s) pessoa(s) mais pesada(s)
1.3) a relação dos nomes da(s) pessoa(s) mais leve(s)
1.4) o número de pessoas acima de 20 anos (mostrar também o nome e idade de casa uma)
1.5) o usuário define quantas pessoas serão cadastradas (Perguntar: Deseja continuar cadastrando?)
"""
dados = list()
cadastro = list()
maior=menor=0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    dados.append(int(input("Idade: ")))
    
    #1.2
    if len(cadastro)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        if dados[1]<menor:
            menor=dados[1]
       
    cadastro.append(dados[:])  #criando uma cópia da lista dados na posição 'x' da lista cadastro
    dados.clear() #para evitar a cópia duplicada da estrutura a cada iteração
    
    #1.5
    resp = str(input("Deseja continuar? [S/N]"))
    if resp in 'Nn':
        break

print(f'Cadastro: {cadastro}')
print(f'Ao todo, foram cadastradas {len(cadastro)} pessoas.')  #1.1

print(f'O maior peso é {maior} kg.')
print(f'Mais pesado(s): ')
for p in cadastro:
    if p[1]==maior:     #1.2
        print(f'{p[0]}')

print(f'O menor peso é {menor} kg.')
print("Mais leve(s): ")
for p in cadastro:     #1.3
    if p[1]==menor:
        print(f'{p[0]}')
        
#1.4
print( "Maiores de 20 anos: ")
idade=0
for p in cadastro:
    if p[2]>20:
        print(f'{p[0]} - {p[2]}')
        idade+=1
if idade == 0:
    print("Nenhuma pessoa com idade acima de 20 anos foi cadastrada.")
else:
    print(f"Existem {idade} pessoas com idade acima de 20 anos.")        
        
                