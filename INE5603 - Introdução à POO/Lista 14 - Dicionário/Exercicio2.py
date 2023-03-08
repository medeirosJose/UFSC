cartas = []
carta = {}

envio = []
envios = {}

quantia = int(input("Quantas traduções deseja inserir? "))

for i in range(quantia):
    carta['idioma'] = str(input("Insira o idioma: "))
    carta['tradução'] = str(input("Insira a frase traduzida em {}: ".format(carta['idioma'])))
    cartas.append(carta.copy())

print(cartas)
crianças = int(input("Quantas crianças receberão a carta? "))

for j in range(crianças):
    envios['nome'] = str(input("Insira o nome da criança: "))
    envios['lingua'] = str(input("Insira o idioma da criança: "))
    envio.append(envios.copy())
print(envio)

for i in range(len(envio)):
    print(envio[i]['nome'])
    for j in range(len(cartas)):
        if envio[i]['lingua'] == cartas[j]['idioma']:
            print(cartas[j]['tradução'])
            print()