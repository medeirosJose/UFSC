#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print("Em ordem crescente: ")
for i in range(1,51):
    
    if i % 2 != 0:
        print(i)

print("\nEm ordem decrescente: ")
for i in range (49,0,-2):
    
    if i%2 != 0:
        print(i)
    
    
