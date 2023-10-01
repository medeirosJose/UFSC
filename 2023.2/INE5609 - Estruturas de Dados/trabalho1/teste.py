class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None


class DoublyLinkedList:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.atual = None
        self.size = 0

    def acessarAtual(self):
        if self.atual is None:
            return None
        return self.atual.dado

    def InserirAntesDoAtual(self, novo):
        if self.atual is None:
            return
        novo_node = Node(novo)
        if self.atual.ant is None:
            self.cabeca = novo_node
            self.cabeca.prox = self.atual
            self.atual.ant = self.cabeca
        else:
            self.atual.ant.prox = novo_node
            novo_node.ant = self.atual.ant
            novo_node.prox = self.atual
            self.atual.ant = novo_node
        self.size += 1

    def InserirApósAtual(self, novo):
        if self.atual is None:
            return
        novo_node = Node(novo)
        if self.atual.prox is None:
            self.cauda = novo_node
            self.cauda.ant = self.atual
            self.atual.prox = self.cauda
        else:
            self.atual.prox.ant = novo_node
            novo_node.prox = self.atual.prox
            novo_node.ant = self.atual
            self.atual.prox = novo_node
        self.size += 1

    def inserirComoUltimo(self, novo):
        novo_node = Node(novo)
        if self.cauda is None:
            self.cabeca = novo_node
            self.cauda = novo_node
        else:
            self.cauda.prox = novo_node
            novo_node.ant = self.cauda
            self.cauda = novo_node
        self.size += 1

    def inserirComoPrimeiro(self, novo):
        novo_node = Node(novo)
        if self.cabeca is None:
            self.cabeca = novo_node
            self.cauda = novo_node
        else:
            self.cabeca.ant = novo_node
            novo_node.prox = self.cabeca
            self.cabeca = novo_node
        self.size += 1

    def inserirNaPosicao(self, k, novo):
        if k < 1 or k > self.size:
            return
        if k == 1:
            self.inserirComoPrimeiro(novo)
            return
        if k == self.size:
            self.inserirComoUltimo(novo)
            return
        novo_node = Node(novo)
        atual_node = self.cabeca
        for i in range(1, k):
            atual_node = atual_node.prox
        atual_node.ant.prox = novo_node
        novo_node.ant = atual_node.ant
        novo_node.prox = atual_node
        atual_node.ant = novo_node
        self.size += 1

    def ExcluirAtual(self):
        if self.atual is None:
            return
        if self.atual.ant is None:
            self.cabeca = self.atual.prox
            if self.cabeca is not None:
                self.cabeca.ant = None
            else:
                self.cauda = None
        elif self.atual.prox is None:
            self.cauda = self.atual.ant
            self.cauda.prox = None
        else:
            self.atual.ant.prox = self.atual.prox
            self.atual.prox.ant = self.atual.ant
        self.atual = None
        self.size -= 1

    def ExcluirPrim(self):
        if self.cabeca is None:
            return
        if self.cabeca.prox is None:
            self.cabeca = None
            self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = None
        self.size -= 1

    def ExcluirUlt(self):
        if self.cauda is None:
            return
        if self.cauda.ant is None:
            self.cabeca = None
            self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = None
        self.size -= 1

    def ExcluirElem(self, chave):
        atual_node = self.cabeca
        while atual_node is not None:
            if atual_node.dado == chave:
                if atual_node.ant is None:
                    self.cabeca = atual_node.prox
                    if self.cabeca is not None:
                        self.cabeca.ant = None
                    else:
                        self.cauda = None
                elif atual_node.prox is None:
                    self.cauda = atual_node.ant
                    self.cauda.prox = None
                else:
                    atual_node.ant.prox = atual_node.prox
                    atual_node.prox.ant = atual_node.ant
                self.size -= 1
                return
            atual_node = atual_node.prox

    def ExcluirDaPos(self, k):
        if k < 1 or k > self.size:
            return
        if k == 1:
            self.ExcluirPrim()
            return
        if k == self.size:
            self.ExcluirUlt()
            return
        atual_node = self.cabeca
        for i in range(1, k):
            atual_node = atual_node.prox
        atual_node.ant.prox = atual_node.prox
        atual_node.prox.ant = atual_node.ant
        self.size -= 1

    def Buscar(self, chave):
        atual_node = self.cabeca
        while atual_node is not None:
            if atual_node.dado == chave:
                self.atual = atual_node
                return True
            atual_node = atual_node.prox
        return False

    def avancarKPosicoes(self, k):
        if self.atual is None:
            return
        for i in range(k):
            if self.atual.prox is None:
                return
            self.atual = self.atual.prox

    def retrocederKPosicoes(self, k):
        if self.atual is None:
            return
        for i in range(k):
            if self.atual.ant is None:
                return
            self.atual = self.atual.ant

    def irParaPrimeiro(self):
        self.atual = self.cabeca

    def irParaUltimo(self):
        self.atual = self.cauda

    def Vazia(self):
        return self.size == 0

    def Cheia(self):
        return False

    def posicaoDe(self, chave):
        atual_node = self.cabeca
        pos = 1
        while atual_no is not None:
            if atual_no.dado == chave:
                return pos
            atual_no = atual_no.prox
            pos += 1
        return -1
