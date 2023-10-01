class Elemento:
    def __init__(self, valor: int, chave: str):
        self.__valor = valor
        self.__chave = chave
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor
    
    @property
    def chave(self):
        return self.__chave
    
    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, novo):
        self.__proximo = novo


class Lista:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.tamanho = 0

    @property
    def get_inicio(self):
        return self.__inicio

    @property
    def get_fim(self):
        return self.__fim

    def __str__(self):
        return f"Lista: {self.__inicio}"

    def get_tamanho(self):
        return self.tamanho

    def inserir_frente(self, id, dado):
        novo = Elemento(id, dado)
        if self.__inicio is None:
            self.__inicio = novo
            self.__fim = novo
        else:
            novo.proximo = self.__inicio
            self.__inicio = novo
        self.tamanho += 1

# testes
class Hash:
    def __init__(self, tamanho):
        self.__tamanho = tamanho

        #self.__elementos = Lista()
        self.__tab = [None] * tamanho

        for i in range(tamanho):
            self.__tab[i] = Lista()

    def get_tamanho(self):
        return self.__tamanho

    def funcao_hash(self, chave):
        return chave % self.__tamanho
    
    def inserirHash(self, chave, valor):
        posicao = self.funcao_hash(chave)
        self.__tab[posicao].inserir_frente(chave, valor)

    def imprimir(self):
        for i in range(self.__tamanho):
            # printa chave e valor tbm
            print(f"Posição {i}: {self.__tab[i]}")



