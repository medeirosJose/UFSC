notas = {'W': 1, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 
'S': 0.0625, 'T': 0.03125, 'X': 0.015625}

musica = []

compasso = input("Insira o compasso: ").split()
musica.append(compasso)

#for k,v in notas.items():
 #   print(k,v)

for i in range(len(musica)):
    print('musica',musica[i])
    if musica[i] == notas.keys():
        print('cu')