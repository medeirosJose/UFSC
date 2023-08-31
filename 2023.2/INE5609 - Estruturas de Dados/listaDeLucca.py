"""
 Classe elemento
    - construtor(valor, proximo)

Classe lista possui elementos
Inserir elemento
 InserirComoPrimeiro ( novo )
 InserirComoÚltimo ( novo )
 InserirNaPosição ( posição , novo )
 InserirAntesDe ( referência, novo )
 InserirDepoisDe ( referência, novo )
● Remoção de elemento
 RemoverPrimeiro ()
 RemoverÚltimo ()
 RemoverDaPosição ( posição )
 Remover ( referência ) # referência a identificador único
 De posição relativa a outro elemento (antesDe, depoisDe) # menos usados
● Consulta / Acesso
 AcessaPrimeiro ()
 AcessaÚltimo ()
 AcessaDaPosição ( posição )


"""


class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None
        self.__anterior = None

    @property
    def get_valor(self):
        return self.__valor

    @property
    def get_proximo(self):
        return self.__proximo

    def set_valor(self, valor):
        self.__valor = valor

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def get_valor_e_proximo(self):
        return self.__valor, self.__proximo


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

    def inserir_como_primeiro(self, novo):
        if self.__inicio is None:
            self.__inicio = novo
            self.__fim = novo
        else:
            novo.set_proximo(self.__inicio)
            self.__inicio = novo
        self.tamanho += 1

    def remover_primeiro(self):
        if self.__inicio is None:
            print("Lista vazia")
        else:
            self.__inicio = self.__inicio.get_proximo
            self.tamanho -= 1

    def acessar_primeiro(self):
        if self.__inicio is None:
            print("Lista vazia")
        else:
            return self.__inicio.get_valor


# testes

lista = Lista()
elemento1 = Elemento(1)
lista.inserir_como_primeiro(elemento1)

print(lista.get_inicio.get_valor)  # Correção aqui
print(lista.get_inicio.get_proximo)
print("Acessar Primeiro", lista.acessar_primeiro())


print()
elemento2 = Elemento(2)
lista.inserir_como_primeiro(elemento2)

print(lista.get_inicio.get_valor)  # Correção aqui
print(lista.get_inicio.get_proximo)
print("Acessar Primeiro", lista.acessar_primeiro())

print("\nTamanho atual da lista -> ", lista.get_tamanho())

lista.remover_primeiro()
print("\nTamanho atual da lista -> ", lista.get_tamanho())

lista.remover_primeiro()
print("\nTamanho atual da lista -> ", lista.get_tamanho())
