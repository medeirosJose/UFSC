# simulação de um código com uma classe pilha


class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        if not self.isEmpty():
            return self.pilha.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.pilha) == 0

    def length(self):
        return len(self.pilha)

    def peek(self):
        if not self.isEmpty():
            return self.pilha[-1]
        else:
            return None

    def __str__(self):
        return str(self.pilha)

    def show(self):
        for i in range(len(self.pilha) - 1, -1, -1):
            print(self.pilha[i])
