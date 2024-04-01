# Árvore binária de Busca - No
# def busca (chave):
#   if raiz != None:
#       buscaRecursiva (raiz, chave)
#   else:
#       return false

# def buscaRecursiva (raiz, chave):
# if raiz != None:
#   if raiz.dado == busca:
#       return true
#   else if chave < raiz.dado:
#       return buscaRecursiva (raiz.esquerda, chave)
#   else:
#       return buscaRecursiva (raiz.direita, chave)
# else:
#   return false


class No:
    def __init__(self, dado, esquerda=None, direita=None):
        self.dado = dado
        self.esquerda = esquerda
        self.direita = direita

    @property
    def getEsquerda(self):
        return self.esquerda

    @property
    def getDireita(self):
        return self.direita

    @property
    def getDado(self):
        return self.dado

    @getEsquerda.setter
    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    @getDireita.setter
    def setDireita(self, direita):
        self.direita = direita

    @getDado.setter
    def setdado(self, dado):
        self.dado = dado
