class Cursor:  # está ok
    def __init__(self, lista):
        self.lista = lista
        self.posicao = None

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, posicao):
        self._posicao = posicao

    # avanca um numero k de posicoes na lista a partir da posicao atual do cursor
    def avancarKPosicoes(self, k):
        if self.posicao is None and k > 0:
            self.posicao = self.lista.primeiro
            k -= 1

        for i in range(k):
            if self.posicao is not None:
                # print("posicao atual:", self.posicao.elemento)
                self.posicao = self.posicao.proximo

    # volta um numero k de posicoes na lista a partir da posicao atual do cursor
    def retrocederKPosicoes(self, k):
        for i in range(k):
            if self.posicao is None:
                self.posicao = self.lista.ultimo
            else:
                self.posicao = self.posicao.anterior

    # resgata da lista o primeiro elemento e atribui à posição do cursor
    def irParaPrimeiro(self):
        self.posicao = self.lista.primeiro

    # resgata da lista o último elemento e atribui à posição do cursor
    def irParaUltimo(self):
        self.posicao = self.lista.ultimo
