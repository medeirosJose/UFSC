valorAux = 0


#numero = int(input("Digite a quantidade de números inteiros: "))
numero = 5
for i in range(5):#numero):
    valor = int(input("Digite um número inteiro: "))
    
    if (i==0):
        menor = valor
        maior = valor
    if (valor < menor):
        menor = valor
    if (valor > maior):
        maior = valor
    
    valorAux = valorAux + valor
    
media = valorAux / numero
    
    
print("Media = ",media)
print("Maior = ",maior)
print("Menor = ",menor)