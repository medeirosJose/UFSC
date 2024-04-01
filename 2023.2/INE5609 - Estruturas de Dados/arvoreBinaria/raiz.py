# Arvore binária de busca - ArvoreBinaria
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


from no import No


class ArvoreBinaria:
    def __init__(self, raiz=None):
        self.raiz = raiz

    @property
    def raiz(self):
        return self.raiz

    @raiz.setter
    def setRaiz(self, raiz):
        self.raiz = raiz

    def insere(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.insereRecursivo(self.raiz, valor)

    def insereRecursivo(self, no, valor):
        if valor < no.dado:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.insereRecursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.insereRecursivo(no.direita, valor)
