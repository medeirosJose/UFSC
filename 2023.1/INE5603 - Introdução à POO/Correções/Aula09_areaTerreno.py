'''
Aula 09 -
exerc 12
Faça um programa que tenha uma função chamada area(),
que receba por parâmetro as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

def area(l,c): 
    area = l * c
    print("A area do terreno é : ", area)
    
#programa principal
largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))
area(largura,comprimento)