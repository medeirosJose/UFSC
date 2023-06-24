#Exercício2568

#No início dos dias pares, o preço da ação sobe X reais em relação ao preço do final do dia anterior.
#Nos dias ímpares, o preço da ação já se inicia com um valor X reais abaixo do valor no fim do dia anterior.

diaD, precoInicial, variacaoX, previsaoFuturo = [int(x) for x in input("Insira dia, preço inicial, variação diária e número de dias futuros: ").split()]
#print(diaD, precoInicial, variacaoX, previsaoFuturo)

if diaD % 2 == 0:
    preco = precoInicial - variacaoX
    print(preco)
    
else:
    preco = precoInicial - variacaoX
    print(preco*previsaoFuturo)
    
#Dúvida.