#1154

def calcularMedia():
    soma = 0
    idade = 0
    cont = 0
    while True:

        idade = int(input("Insira a idade: "))
        if idade < 0:
            break
        soma = idade + soma
        cont += 1
    media = (soma / (cont))
    return media

print(calcularMedia())