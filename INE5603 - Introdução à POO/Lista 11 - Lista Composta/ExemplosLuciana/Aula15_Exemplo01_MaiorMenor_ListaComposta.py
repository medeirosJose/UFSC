#Aula 15 Exemplo 01  Lista Composta

'''Programa que leia o nome e o peso de várias pessoas (guarde em uma única lista).
Responda:
1) quantas pessoas foram cadastradas
2) mostre a relação de nomes das pessoas mais pesadas
3) mostre a relação de nomes das pessoas mais leves'''

temp =[]
princ=[]
maior=menor=0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1]<menor:
            menor=temp[1]
    princ.append(temp[:])
    temp=list()
    #temp.clear()
    
    resp=str(input('Deseja continuar cadastrando? S/N'))
    if resp in 'Nn':
        break
 
print(f"Total de cadastrados: {len(princ)}")
print(princ)

print(f'Maior peso foi de {maior}kg. Peso de ',end='')
for p in princ:
    #print(p)
    if p[1]==maior:                #compara o valor que está na posição p[1]
        print(f'[{p[0]}]',end='')  #imprime o nome que está na posição p[0]
print()

print(f'Menor peso foi de {menor}kg. Peso de ',end='')
for p in princ:
    if p[1]==menor:
        print(f'[{p[0]}]',end='')        
