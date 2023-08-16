#! preciso adicionar algumas exceções. por exemplo
#  se o index for menor que o inicio ou maior que o fim
#  inverter o inicio e o fim


class SuperArray:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.array = [None] * (fim - inicio + 1)

    def atribuir(self, index, valor):
        if index < self.inicio or index > self.fim:
            raise IndexError("Index fora do intervalo")
        self.array[index - self.inicio] = valor

    def acessar(self, index):
        if index < self.inicio or index > self.fim:
            raise IndexError("Index fora do intervalo")
        return self.array[index - self.inicio]
    