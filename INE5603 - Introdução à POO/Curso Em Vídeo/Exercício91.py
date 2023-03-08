from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
        }

for k,v in jogo.items():
        print(f'{k} tirou {v} no dado.')

ranking = sorted(jogo.items(),key=itemgetter(1), reverse = True)
print('\n       ===== Ranking Final ===== ')

for i,j in enumerate(ranking):
        print(f'       {i+1}º lugar -> {j[0]} com {j[1]} ')

print('       =========================')