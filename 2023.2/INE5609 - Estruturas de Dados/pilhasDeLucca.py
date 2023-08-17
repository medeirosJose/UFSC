class Pilha:
    def __init__(self, tam):
        self.__dados = []
        self.__max = tam
        self.__cont = 0

    def pop(self):
        if self.__cont > 0:
            self.__cont -= 1
            temp = self.__dados[self.__cont]
            # del faz com que o elemento seja removido da memória
            # pode-se usar o pop() do python
            self.__dados.pop(self.__cont)
            # del self.__dados[self.__cont]
            return temp

    def push(self, novo):
        if self.__cont < self.__max:
            self.__cont += 1
            self.__dados.append(novo)

        else:
            print("Pilha cheia")


# testes otimizados
p = Pilha(5)
for i in range(6):
    p.push(i)
for i in range(6):
    print(p.pop())
