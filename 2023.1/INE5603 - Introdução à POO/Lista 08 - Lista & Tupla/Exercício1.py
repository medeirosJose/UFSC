alunos = int(input("Informe a quantidade de alunos: "))
notas = [0,0,0]

for i in range(alunos):
    notaMaior = -1
    notaMenor = 11
    soma = 0

    for i in range(3):
        nota = int(input("Digite a nota: "))
        while not(0<=nota<=10):
            print("Digite uma nota válida entre 0 e 10: ")
            nota = int(input("Digite a nota: "))
        notas[i] = nota

        soma += notas[i]
        if notas[i] > notaMaior:
            notaMaior = notas[i]
        if notas[i] < notaMenor:
            notaMenor = notas[i]

    print(notas)
    print("A média do aluno é de {:.2f}".format(soma/3))
    print("A maior nota foi de",notaMaior,"enquanto que a menor nota foi de",notaMenor,". A diferença entre as duas notas foi de",(notaMaior - notaMenor))        