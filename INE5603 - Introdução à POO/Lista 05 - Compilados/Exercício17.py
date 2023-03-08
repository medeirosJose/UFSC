#Exercício17

resposta = "N"

while True:
    print("1 - Pedra \n2 - Papel \n3 - Tesoura")
    jog1 = int(input("Jogador 1, insira sua opção: "))
    jog2 = int(input("Jogador 2, insira sua opção: "))
    
    if jog1 == 1 and jog2 == 2:
        print("Jogador 2 vence!")
    elif jog1 == 1 and jog2 == 3:
        print("Jogador 1 vence!")
    elif jog1 == jog2:
        print("Empate.")
    elif jog1 == 2 and jog2 == 1:
        print("Jogador 1 vence!")
    #elif jog 1 == 2 and jog2 == 2:
     #   print("Empate")
    elif jog1 == 2 and jog2 == 3:
        print("Jogador 2 vence!")
    elif jog1 == 3 and jog2 == 1:
        print("Jogador 1 vence!")
    elif jog1 == 3 and jog2 == 2:
        print("Jogador 2 vence!")
    elif jog1 >= 4 or jog1 <= 0 or jog2 >= 4 or jog2 <= 0:
        print("Digite um número válido.")
    
    resposta = input("Deseja continuar? [S/N]")
    if resposta == "N":
        break