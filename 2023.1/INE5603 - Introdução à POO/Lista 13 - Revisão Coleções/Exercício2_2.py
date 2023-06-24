'''faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa 
vai perguntar quantos jogos serão sorteados e vai gerar 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma única lista composta.'''

from random import randint

resultado = []
jogos = int(input("Quais jogos serão sorteados? "))

print('---'*15,'\nJogos da Mega Sena\n','---'*15)

print('=-=-=-=-= {} jogos sorteados =-=-=-=-=\n'.format(jogos))

for j in range(jogos):
    for i in range(6):
        numero = randint(1,60)
        resultado.append(numero)
    print(f'Jogo {j+1}:',resultado)
    resultado.clear()
print('\n=-=-=-=-=-= Boa sorte! =-=-=-=-=-=\n')
