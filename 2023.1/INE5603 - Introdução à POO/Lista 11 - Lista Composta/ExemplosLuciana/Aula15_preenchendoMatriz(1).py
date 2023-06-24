#Aula 15 preechendo uma matriz
#crie um programa que crie uma matriz 3x3 e preencha seus valores

matriz=[[0,0,0],[0,0,0],[0,0,0]]   #para não usar append

for lin in range(0,3):
    for col in range(0,3):
        matriz[lin][col]= int(input(f'Digite um valor para posição [{lin},{col}]: '))

print(matriz)

for lin in range(0,3):
    for col in range(0,3):
        print(f'[{matriz[lin][col]:^5}]',end=" ")
    print()

