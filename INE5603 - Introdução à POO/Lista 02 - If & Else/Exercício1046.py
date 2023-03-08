#Exercício1046

inicio, final = [int(x) for x in input("Digite a hora que o jogo iniciou e a hora que terminou: ").split()]

duracao = inicio - final

if inicio == final:
    print("O jogo durou 24 horas.")
    
elif inicio > final:
    print("O jogo durou",((24 - inicio) + final), "horas.")

elif inicio < final:
    print("O jogo durou", final - inicio, "horas.")