praiaLonge = ""
distanciaAux = 0
contadorPraia = 0
distanciaLonge = 0

praias = int(input("Digite a quantidade de praias que deseja cadastrar: "))

for i in range(praias):
    nomePraia = input("Insira o nome da praia: ")
    distancia = int(input("Insira a distância entre a praia e o centro: "))
    
    distanciaAux = distancia + distanciaAux
    media = distanciaAux / praias
    
    if(i==0):
        distancia = distanciaLonge
        praiaLonge = nomePraia
        
    if distancia > distanciaLonge:
        distanciaLonge = distancia
        praiaLonge = nomePraia
  
    if distancia >= 15 and distancia <= 20:
        contadorPraia += 1
        
print("A praia mais distante é",praiaLonge)
print("Há",contadorPraia, "praia(s) entre 15 e 20km do centro.")
print("Média = {:.1f}".format(media))

        