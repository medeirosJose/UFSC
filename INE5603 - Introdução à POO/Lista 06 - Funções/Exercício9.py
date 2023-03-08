#Encontrar números primos é uma tarefa difícil. Faça um programa que defina uma 
#função que retorne a quantidade de números primos existentes no intervalo digitado 
#(intervalo fechado, ou seja, considerando os números digitados). 

def primo(num):
    contDivisor = 0
    for i in range(num):
        if (num % (i+1) == 0):
            contDivisor += 1
    if contDivisor > 2:
        return False
    else:
        return True
        
def primosIntervalo(inicio, fim):
    contPrimos = 0
    for i in range(inicio, fim+1):
        if primo(i):
            contPrimos += 1

    return contPrimos     

inicio, fim = [int(x) for x in input("Digite o início e fim do intervalo: ").split()]

print("Há um total de",primosIntervalo(inicio,fim),"números primos")