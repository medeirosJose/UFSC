notaMaior = 0
notaMenor = 0
soma = 0

for i in range(5):
    nota = float(input("Insira uma nota: "))
    
    if (i==0):
        notaMenor = nota
        notaMaior = nota
    if (nota < notaMenor):
        notaMenor = nota
    if (nota > notaMaior):
        notaMaior = nota
    
    soma += nota

print("A nota final é {:.1f}".format(soma - notaMaior - notaMenor))