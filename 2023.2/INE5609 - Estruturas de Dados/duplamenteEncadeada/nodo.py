class Nodo:  # está ok
    def __init__(self, elemento=None, proximo=None, anterior=None):
        self.elemento = elemento
        self.proximo = proximo
        self.anterior = anterior

    def __str__(self):
        return str(self.elemento)

    @property
    def elemento(self):
        return self._elemento

    @elemento.setter
    def elemento(self, elemento):
        self._elemento = elemento

    @property
    def proximo(self):
        return self._proximo

    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, anterior):
        self._anterior = anterior
