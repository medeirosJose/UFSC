"""Esse trabalho é simples e está diretamente relacionado com as conversas de nossas aulas com a lista duplamente encadeada COM cursor.

As operações públicas que precisam estar implementadas são (no mínimo)   (não devolve nada quer dizer que não retorna nada,

(devolve elemento) acessarAtual()
(não devolve nada) InserirAntesDoAtual ( novo )
(não devolve nada) InserirApósAtual ( novo )
(não devolve nada) inserirComoUltimo ( novo )
(não devolve nada) inserirComoPrimeiro ( novo )
(não devolve nada) inserirNaPosicao ( k, novo )
(não devolve nada) ExcluirAtual ()
(não devolve nada) ExcluirPrim ()
(não devolve nada) ExcluirUlt ()
(não devolve nada) ExcluirElem ( chave )
(não devolve nada) ExcluirDaPos ( k )
(boolean) Buscar ( chave )
LEMBRETE: Todas essas operações são baseadas na posição que o CURSOR estiver indicando; com exceção da BUSCA (operação Buscar) que manipula o cursor para deixá-lo indicando o elemento encontrado.

As operações para controle do cursor (privadas) devem ser, no mínimo:

avançarKPosições( K )
retrocederKPosições ( K )
irParaPrimeiro()
irParaUltimo()
Outras (de apoio):
(boolean) Vazia()
(boolean) Cheia()
(INT) posiçãoDe(chave)  // informa a posição sequencial do elemento com aquela chave, contado desde o primeiro"""


class No:
    def __init__(self, elemento, proximo=None, anterior=None):
        self.elemento = elemento
        self.proximo = proximo
        self.anterior = anterior


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
        self.cursor = None

    def vazia(self):
        return self.tamanho == 0

    def cheia(self):
        return False

    def acessarAtual(self):
        if self.cursor is None:
            return None
        else:
            return self.cursor.elemento

    def inserirComoPrimeiro(self, novo):
        novo_no = No(novo)
        if self.vazia():
            self.primeiro = self.ultimo = self.cursor = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no
            self.primeiro = self.cursor = novo_no
        self.tamanho += 1

    def inserirComoUltimo(self, novo):
        novo_no = No(novo)
        if self.vazia():
            self.primeiro = self.ultimo = self.cursor = novo_no
        else:
            self.ultimo.proximo = novo_no
            novo_no.anterior = self.ultimo
            self.ultimo = self.cursor = novo_no
        self.tamanho += 1

    def inserirNaPosicao(self, k, novo):
        if k == 1:
            self.inserirComoPrimeiro(novo)
        elif k == self.tamanho + 1:
            self.inserirComoUltimo(novo)
        else:
            novo_no = No(novo)
            self.cursor = self.primeiro
            for i in range(k - 1):
                self.cursor = self.cursor.proximo
            novo_no.proximo = self.cursor
            novo_no.anterior = self.cursor.anterior
            self.cursor.anterior.proximo = novo_no
            self.cursor.anterior = novo_no
            self.tamanho += 1

    def inserirAntesDoAtual(self, novo):
        if self.vazia():
            self.inserirComoPrimeiro(novo)
        else:
            novo_no = No(novo)
            novo_no.proximo = self.cursor
            novo_no.anterior = self.cursor.anterior
            self.cursor.anterior.proximo = novo_no
            self.cursor.anterior = novo_no
            self.tamanho += 1

    def inserirApósAtual(self, novo):
        if self.vazia():
            self.inserirComoPrimeiro(novo)
        else:
            novo_no = No(novo)
            novo_no.proximo = self.cursor.proximo
            novo_no.anterior = self.cursor
            self.cursor.proximo.anterior = novo_no
            self.cursor.proximo = novo_no
            self.tamanho += 1

    def excluirAtual(self):
        if not self.cursor:
            return

        if self.cursor.anterior:
            self.cursor.anterior.proximo = self.cursor.proximo
        else:
            self.primeiro = self.cursor.proximo

        if self.cursor.proximo:
            self.cursor.proximo.anterior = self.cursor.anterior
        else:
            self.ultimo = self.cursor.anterior

        self.cursor = (
            self.cursor.proximo if self.cursor.proximo else self.cursor.anterior
        )
        self.tamanho -= 1

    def excluirPrim(self):
        if not self.primeiro:
            return

        if self.cursor == self.primeiro:
            self.cursor = self.primeiro.proximo

        self.primeiro = self.primeiro.proximo
        if self.primeiro:
            self.primeiro.anterior = None

        self.tamanho -= 1

    def excluirUlt(self):
        if not self.ultimo:
            return

        if self.cursor == self.ultimo:
            self.cursor = self.ultimo.anterior

        self.ultimo = self.ultimo.anterior
        if self.ultimo:
            self.ultimo.proximo = None

        self.tamanho -= 1

    def excluirElem(self, chave):
        if self.vazia():
            return
        temp = self.cursor  # Save the current position of the cursor
        self.cursor = self.primeiro

        while self.cursor and self.cursor.elemento != chave:
            self.cursor = self.cursor.proximo

        if not self.cursor:  # If item not found
            self.cursor = temp  # Restore the cursor's position
            return

        self.excluirAtual()

    def buscar(self, chave):
        if self.vazia():
            return False
        temp = self.cursor
        self.cursor = self.primeiro
        while self.cursor and self.cursor.elemento != chave:
            self.cursor = self.cursor.proximo

        found = self.cursor is not None and self.cursor.elemento == chave
        if not found:  # If not found, restore cursor position
            self.cursor = temp
        return found

    def posicaoDe(self, chave):
        if self.vazia():
            return None
        else:
            self.cursor = self.primeiro
            pos = 1
            while self.cursor.elemento != chave:
                self.cursor = self.cursor.proximo
                pos += 1
            return pos

    def avancarKPosicoes(self, k):
        if self.vazia():
            return None
        else:
            for i in range(k):
                self.cursor = self.cursor.proximo

    def retrocederKPosicoes(self, k):
        if self.vazia():
            return None
        else:
            for i in range(k):
                self.cursor = self.cursor.anterior

    def irParaPrimeiro(self):
        if self.vazia():
            return None
        else:
            self.cursor = self.primeiro

    def irParaUltimo(self):
        if self.vazia():
            return None
        else:
            self.cursor = self.ultimo
