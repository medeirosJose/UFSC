'''
Livraria
criar um programa com uma tupla única com produtos e respectivos preços,
na sequencia.
Seu programa deve simular uma compra:'''

produtos = ('borracha', 1.50,
            'lápis grafite', 2.00,
            'régua', 3.60,
            'caderno 40fls', 13.60,
            'caderno 100fls', 16.90)

print(produtos)

#como imprimir de forma organizada na tela:
for pos in range(0,len(produtos)):
    if pos % 2 ==0:
        print(f'{produtos[pos]:.<30}', end="")
    else:
        print(f' R$ {produtos[pos]:.2f}')
        
