mediaMaior = 0
mensalidade = 0
nomeMaior = ""

for i in range(5):
    nome = input("Digite seu nome: ")
    media = int(input("Digite sua média final: "))
    mensalidade = int(input("Digite sua mensalidade: "))
    
    if media > mediaMaior:
        mediaMaior = media
        mensalidadeMaior = mensalidade
        nomeMaior = nome

print("\nO aluno com maior média foi {}. \nA mensalidade de R$ {} passará a ser R$ {}".format(nomeMaior, mensalidadeMaior, mensalidadeMaior*0.7))