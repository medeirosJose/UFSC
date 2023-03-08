sorteadas = int(input("Digite a quantidade de camisetas que serão sorteadas: "))
lista = []

for i in range(sorteadas):

    qtAlunos, sNumero = [int(x) for x in input("Informe a quantidade de alunos do grupo e o número que deverá ser acertado: ").split()]

    for i in range(qtAlunos):
        chute = int(input("Aluno {} chute um valor: ".format(i)))
        lista.append(chute)
        
print(lista)