#Questão 2 - Prova

#Listas
lista_sexo = []
lista_idade = []
lista_salario = []
#Contador para o número pessoas
contador = 0
continuar = "S"

#Loop para entrada dos valores. Ele recebe os valores, adiciona as respectivas listas, soma 1 ao contador, e pergunta se deseja continuar cadastrando
while continuar == "S":
    sexo = str(input("Informe o sexo da pessoa - M/F: ")).upper()
    idade = int(input("Informe a idade dela: "))
    salario = float(input("Informe o salário: "))
    continuar = str(input("Deseja continuar? - S/N: ")).upper()
    lista_sexo.append(sexo)
    lista_idade.append(idade)
    lista_salario.append(salario)
    contador = contador + 1

#Variável acumuladora que recebe a soma das idades da lista_idade
idade_total = 0
#Loop que soma as idades
for i in range(len(lista_idade)):
    idade_total = idade_total + lista_idade[i]
#Fórmula que calcula a média das idades do grupo usando o contador do início e a idade total (calculado previamente no loop for)
idade_media = idade_total/contador

#Variável acumuladora que recebe o número de mulheres que tem o salário maior que 2000
contador_mulheres = 0
#Loop que percorre a lista lista_sexo, encontra as mulheres e verifica quais as que tem um salário maior que 2000. Para cada uma ele adiciona +1 ao contador contador_mulheres
for i in range(len(lista_sexo)):
    if lista_sexo[i] == "F":
        if lista_salario[i] > 2000:
            contador_mulheres = contador_mulheres + 1
            
#Variável acumuladora que é utilizada dentro do loop para fins de comparação
menor = 0
#Loop que percorre a lista lista_salario e verifica quem possui o menor salário
for i in range(len(lista_salario)):
    if (lista_salario[menor] > lista_salario[i]):
        menor = i

#Impressão dos resultados - Média das idades, número de mulheres com salário superior a 2000 reais, e qual a idade e o sexo da pessoa com o menor salário
print("A média de idade do grupo entrevistado é de {:.2f} anos.\nA quantidade de mulheres com o salário maior que 2000 reais é de {}.\nO sexo e a idade da pessoa com o menor salário é {} e {:.2f} respectivamente.".format(idade_media, contador_mulheres, lista_sexo[menor], lista_idade[menor]))

            


    
    