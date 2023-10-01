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
        cursor_atual = self.cursor.posicao  # Memorize a posição atual do cursor
        self.cursor.irParaPrimeiro()
        while self.cursor.posicao:
            retorno += str(self.cursor.posicao.elemento) + ", "
            if self.cursor.posicao.proximo:  # Verifique se há um próximo nodo
                self.cursor.avancarKPosicoes(1)
            else:
                break  # Pare se este for o último nodo
        self.cursor.posicao = cursor_atual  # Restaure a posição original do cursor
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

    def inserirComoPrimeiro(self, novo):
        if self.vazia():
            self.ultimo = novo
            # Remova esta linha: self.cursor.posicao = novo
            print("Inserido com sucesso. - inserirComoPrimeiro")
        else:
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
        self.primeiro = novo
        self.tamanho_atual += 1
        print("Inserido com sucesso. - inserirComoPrimeiro")

    def inserirComoUltimo(self, novo):
        if self.vazia():
            self.primeiro = novo
            # Remova esta linha: self.cursor.posicao = novo
            print("Inserido com sucesso. - inserirComoUltimo")
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo
        self.tamanho_atual += 1
        print("Inserido com sucesso. - inserirComoUltimo")

    # para evitar problemas com o cursor, sempre que inserir um novo elemento, o cursor deve apontar para o primeiro
    def inserirNaPosicao(self, k, novo):
        if self.vazia() or k <= 1:
            self.inserirComoPrimeiro(novo)
            print("Inserido com sucesso. - inserirComoPrimeiro")
        elif k > self.tamanho_atual:
            self.inserirComoUltimo(novo)
            print("Inserido com sucesso. - inserirComoUltimo")
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

            print("Inserido com sucesso. - inserirNaPosicao")

        self.cursor.irParaPrimeiro()  # faz o cursor voltar para o primeiro elemento

    def acessarAtual(self):
        if self.vazia() or self.cursor.posicao is None:
            return None
        return self.cursor.posicao.elemento

    def inserirAntesDoAtual(self, novo):
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
        self.cursor.posicao = novo

    def inserirApósAtual(self, novo):
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

    # excluirPrim e excluirUlt são iguais a excluirAtual, mas não necessitam do cursor
    def excluirPrim(self):
        if self.vazia():
            return
        if self.primeiro.proximo is None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo

    def excluirUlt(self):
        if self.vazia():
            return
        if self.ultimo.anterior is None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior

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

    def excluirDaPos(self, k):
        self.cursor.avancarKPosicoes(k - 1)
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
            return f"\n[Busca] - Elemento {chave} foi encontrado {contador} vez(es) na lista."
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
