#Exercício2375

diametro = int(input("Insira o diâmetro da bola: "))
altura, largura, profundidade = [int(x) for x in input("Digite a altura, largura e profundidade da caixa: ").split()]

if diametro > altura or diametro > profundidade or diametro > largura:
    print("N")
else:
    print("S")