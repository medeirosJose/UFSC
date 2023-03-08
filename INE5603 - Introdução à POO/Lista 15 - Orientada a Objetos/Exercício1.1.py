'''1) Utilizando os conceitos de POO vistos em sala, implemente um programa que calcule e imprima o cubo de
um número lido do teclado.'''

class Cubo:
    def __init__(self, numero):
        self.numero = numero

    def cubar(self):
        cubão = self.numero * self.numero * self.numero

        return cubão


# main
numero = int(input('Número: '))
n1 = Cubo(numero)

print(n1.cubar())