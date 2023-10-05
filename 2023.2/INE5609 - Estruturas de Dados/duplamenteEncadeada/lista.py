from cursor import Cursor


class Lista:
    def __init__(self, tamanho_maximo=None):
        self.primeiro = None
        self.ultimo = None
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0
        self.cursor = Cursor(self)

    def __str__(self):
        if self.vazia():
            return "[]"
        retorno = "["
        cursor_atual = self.cursor.posicao  # Memoriza a posição atual do cursor
        self.cursor.irParaPrimeiro()
        while self.cursor.posicao:
            retorno += str(self.cursor.posicao.elemento) + ", "
            if self.cursor.posicao.proximo:  # Verifica se há um próximo nodo
                self.cursor.avancarKPosicoes(1)
            else:
                break  # Para se este for o último nodo
        self.cursor.posicao = cursor_atual  # Restaura a posição original do cursor
        print()
        return retorno[:-2] + "]"

    @property
    def tamanho_atual(self):
        return self._tamanho_atual

    @tamanho_atual.setter
    def tamanho_atual(self, tamanho_atual):
        self._tamanho_atual = tamanho_atual

    @property
    def tamanho_maximo(self):
        return self._tamanho_maximo

    @tamanho_maximo.setter
    def tamanho_maximo(self, tamanho_maximo):
        self._tamanho_maximo = tamanho_maximo

    def vazia(self):
        return self.primeiro is None

    def cheia(self):
        return self.tamanho_atual == self.tamanho_maximo

    def inserirComoPrimeiro(self, novo):
        if self.cheia():
            raise Exception("Lista cheia")
        if self.vazia():
            self.ultimo = novo
            # Remova esta linha: self.cursor.posicao = novo
            # print("inserido com sucesso. - inserirComoPrimeiro")
        else:
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
        self.primeiro = novo
        self.tamanho_atual += 1
        # define o cursor como o atual
        self.cursor.posicao = novo
        # print("inserido com sucesso. - inserirComoPrimeiro")

    def inserirComoUltimo(self, novo):
        if self.cheia():
            raise Exception("Lista cheia")

        if self.vazia():
            self.primeiro = novo
            # Remova esta linha: self.cursor.posicao = novo
            # print("inserido com sucesso. - inserirComoUltimo")
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo
        self.tamanho_atual += 1
        self.cursor.posicao = novo

        # print("inserido com sucesso. - inserirComoUltimo")

    # para evitar problemas com o cursor, sempre que inserir um novo elemento, o cursor deve apontar para o primeiro
    def inserirNaPosicao(self, k, novo):
        if self.cheia():
            raise Exception("Lista cheia")
        if self.vazia() or k <= 1:
            self.inserirComoPrimeiro(novo)
            # print("inserido com sucesso. - inserirComoPrimeiro")
        elif k > self.tamanho_atual:
            self.inserirComoUltimo(novo)
            # print("inserido com sucesso. - inserirComoUltimo")
        else:
            self.cursor.irParaPrimeiro()  # Comece do começo
            self.cursor.avancarKPosicoes(k - 1)  # Vá para a posição k

            # Se após avançar, o cursor ainda aponta para um Nodo, insira antes dele
            if self.cursor.posicao:
                novo.anterior = self.cursor.posicao.anterior
                novo.proximo = self.cursor.posicao
                if self.cursor.posicao.anterior:
                    self.cursor.posicao.anterior.proximo = novo
                self.cursor.posicao.anterior = novo
                self.tamanho_atual += 1

            # print("inserido com sucesso. - inserirNaPosicaoAAAAA")

        self.cursor.irParaPrimeiro()  # faz o cursor voltar para o primeiro elemento

    def acessarAtual(self):
        if self.vazia() or self.cursor.posicao is None:
            return None
        return f"Atual -> {self.cursor.posicao.elemento}"

    def inserirAntesDoAtual(self, novo):
        if self.cheia():
            raise Exception("Lista cheia")

        if self.vazia() or self.cursor.posicao is None:
            self.inserirComoPrimeiro(novo)
        else:
            novo.proximo = self.cursor.posicao
            novo.anterior = self.cursor.posicao.anterior
            self.cursor.posicao.anterior = novo
            if novo.anterior is None:
                self.primeiro = novo
            else:
                novo.anterior.proximo = novo

        self.tamanho_atual += 1
        self.cursor.posicao = novo

    def inserirAposAtual(self, novo):
        if self.cheia():
            raise Exception("Lista cheia")

        if self.vazia() or self.cursor.posicao is None:
            self.inserirComoUltimo(novo)
        else:
            novo.anterior = self.cursor.posicao
            novo.proximo = self.cursor.posicao.proximo
            self.cursor.posicao.proximo = novo
            if novo.proximo is None:
                self.ultimo = novo
            else:
                novo.proximo.anterior = novo
        self.tamanho_atual += 1
        self.cursor.posicao = novo

    def excluirAtual(self):
        if self.vazia() or self.cursor.posicao is None:
            return

        if self.cursor.posicao.anterior is None:
            self.primeiro = self.cursor.posicao.proximo
        else:
            self.cursor.posicao.anterior.proximo = self.cursor.posicao.proximo

        if self.cursor.posicao.proximo is None:
            self.ultimo = self.cursor.posicao.anterior
        else:
            self.cursor.posicao.proximo.anterior = self.cursor.posicao.anterior

        # Atualize a posição do cursor
        if self.cursor.posicao.proximo:
            self.cursor.posicao = self.cursor.posicao.proximo
        elif self.cursor.posicao.anterior:
            self.cursor.posicao = self.cursor.posicao.anterior
        else:
            self.cursor.posicao = None

        self.tamanho_atual -= 1  # Decrementa o tamanho da lista

    # excluirPrim e excluirUlt são iguais a excluirAtual, mas não necessitam do cursor
    def excluirPrim(self):
        if self.vazia():
            return
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo

        self.tamanho_atual -= 1  # Decrementa o tamanho da lista

    def excluirUlt(self):
        if self.vazia():
            return
        if self.ultimo.anterior is None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior

        self.tamanho_atual -= 1  # Decrementa o tamanho da lista

    def excluirElem(self, chave):
        while self.cursor.posicao is not None and self.cursor.posicao.elemento != chave:
            self.cursor.avancarKPosicoes(1)
        if self.cursor.posicao is None:
            return

        if self.cursor.posicao.anterior is None:
            self.primeiro = self.cursor.posicao.proximo
        else:
            self.cursor.posicao.anterior.proximo = self.cursor.posicao.proximo

        if self.cursor.posicao.proximo is None:
            self.ultimo = self.cursor.posicao.anterior
        else:
            self.cursor.posicao.proximo.anterior = self.cursor.posicao.anterior

        self.tamanho_atual -= 1  # Decrementa o tamanho da lista

    def excluirDaPos(self, k):
        self.cursor.avancarKPosicoes(k)
        if self.cursor.posicao is None:
            return

        proximo_nodo = self.cursor.posicao.proximo
        nodo_anterior = self.cursor.posicao.anterior

        # Atualize os ponteiros do nodo anterior e próximo, se eles existirem
        if nodo_anterior:
            nodo_anterior.proximo = proximo_nodo
        else:  # Se não houver nodo anterior, atualize o primeiro elemento
            self.primeiro = proximo_nodo

        if proximo_nodo:
            proximo_nodo.anterior = nodo_anterior
        else:  # Se não houver próximo nodo, atualize o último elemento
            self.ultimo = nodo_anterior

        # Atualize a posição do cursor.
        # Se o próximo nodo existir, mova para ele. Caso contrário, mova para o nodo anterior.
        # Se nenhum dos dois existir, defina o cursor como None.
        if proximo_nodo:
            self.cursor.posicao = proximo_nodo
        elif nodo_anterior:
            self.cursor.posicao = nodo_anterior
        else:
            self.cursor.posicao = None

        self.tamanho_atual -= 1  # Decrementa o tamanho da lista

    # percorre a lista um a um até encontrar o elemento desejado
    # conta a quantidade de vezes que o elemento aparece na lista, caso hajam repetições
    def buscar(self, chave):
        contador = 0
        encontrado = False

        self.cursor.irParaPrimeiro()  # Vá para o primeiro elemento

        while self.cursor.posicao is not None:
            if self.cursor.posicao.elemento == chave:
                contador += 1
                encontrado = True
            self.cursor.avancarKPosicoes(1)

        if encontrado:
            return f"\n[Busca] Elemento {chave} foi encontrado {contador} vez(es) na lista."
        else:
            return f"\n[Busca] Elemento {chave} não está na lista."

    # percorre a lista um a um até encontrar o elemento desejado
    # retorna a posição do elemento na lista, caso ele exista
    def posicaoDe(self, chave):
        posicao = 1
        self.cursor.irParaPrimeiro()
        while self.cursor.posicao is not None:
            if self.cursor.posicao.elemento == chave:
                return f"\n[Posição Sequencial] - Elemento {chave} está na posição {posicao} da lista."
            self.cursor.avancarKPosicoes(1)
            posicao += 1
        return f"\n[Posição Sequencial] - Elemento {chave} não está na lista."
