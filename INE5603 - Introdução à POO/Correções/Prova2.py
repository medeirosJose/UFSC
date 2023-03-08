media = 0
cont = 0
abaixo2000 = 0
salarioMenor = 0
idadeMenor = 0
sexoMenor = 0
i = False

while True:
    idade = int(input("Digite a idade: "))
    sexo = int(input("Digite o sexo:\n1 - Masculino \n2 - Feminino\n"))
    salario = int(input("Informe o salário: "))
    
    if salario < salarioMenor or i == False:
        i = True
        salarioMenor = salario
        sexoMenor = sexo
        idadeMenor = idade

    if (sexo == 2) and (salario < 2000):
        abaixo2000 = abaixo2000 + 1

    cont += 1
    media += idade

    continuar = str(input("Deseja continuar? [S] / [N]\n")).upper()
    if continuar == "N":
        break

print("Há {} mulher(es) com salário abaixo de R$ 2000. ".format(abaixo2000))
print("A média de idade do grupo foi de {:.1f} anos.".format(media/cont))
print("A pessoa com o menor salário ({}), é do sexo {} e tem {} anos".format(salarioMenor, sexoMenor, idadeMenor))

