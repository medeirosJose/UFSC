mediaTurma = 0
notaAlunoAux = 0
nomeAux = ""

for i in range(5):
    nome = input("Digite seu nome: ")
    notaAluno = int(input("Digite sua nota: "))
    mediaTurma = mediaTurma + notaAluno
    
    if notaAluno > notaAlunoAux:
        nomeAux = nome
        notaAlunoAux = notaAluno
     
if notaAlunoAux >= 5.75:
    status = "Aprovado(a)!"
elif notaAlunoAux >= 2.75:
    status = "Em recuperação... Você tem direito de fazer uma prova de recuperação."
else:
    status = "Reprovado(a)."
    
print("A média da turma foi de {}. {} teve a média mais alta com {} e está {}".format(mediaTurma/5, nomeAux, notaAlunoAux, status))
