def calcularMedia():
    mediaTurma = 0
    notaMaior = 0
    nomeNotaMaior = ""
    
    for i in range(5):
        nome = input("Digite seu nome: ")
        notaAluno = int(input("Digite sua nota: "))
        
        mediaTurma = mediaTurma + notaAluno 

        if notaAluno > notaMaior:
            nomeNotaMaior = nome
            notaMaior = notaAluno
   
    return mediaTurma/5, nomeNotaMaior, notaMaior

#print(calcularMedia(int(input())))

mediaTurma, nomeNotaMaior, notaMaior = calcularMedia()

if notaMaior >= 5.75:
    status = "aprovado(a)!"
elif notaMaior >= 2.75:
    status = "em recuperação... Você tem direito de fazer uma prova de recuperação."
else:
    status = "reprovado(a)."

print("A média da turma foi de {}. {} teve a média mais alta com {} e está {}".format(mediaTurma, nomeNotaMaior, notaMaior, status))

