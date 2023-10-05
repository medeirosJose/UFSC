# importando as classes necessarias
from lista import Lista
from nodo import Nodo
from cursor import Cursor


# testes
# lista = Lista(4)

"""lista.inserirComoPrimeiro(Nodo(1))
print("Lista depois de inserirComoPrimeiro ->", lista)
lista.inserirComoUltimo(Nodo(5))
print("Lista antes de inserirNaPosicao ->", lista)

print("\n\ntentando inserir na posicao 20 o elemento 77")
lista.inserirNaPosicao(20, Nodo(55))
print("LISTA OLHA AQUI depois de inserirNaPosicao ->", lista)

print("\n\ntentando inserir na posicao 25 o elemento 44")
lista.inserirNaPosicao(25, Nodo(44))
print("LISTA OLHA AQUI 2 depois de inserirNaPosicao ->", lista)

# printar cursor
print()
print()
print()

lista.inserirNaPosicao(3, Nodo(3))

print("Lista depois de inserirNaPosicao ->", lista)
lista.inserirComoPrimeiro(Nodo(0))
print("Lista depois de inserirComoPrimeiro ->", lista)

lista.inserirComoUltimo(Nodo(99))
print("Lista depois de inserirComoUltimo ->", lista)
lista.inserirComoPrimeiro(Nodo(99))
# printar cursor

lista.buscar(99)
print(lista.buscar(99))

#print(lista.posicaoDe(99))
print(lista.posicaoDe(55))
print(lista.posicaoDe(44))
print(lista.posicaoDe(300))
"""

"""lista.inserirComoPrimeiro(Nodo(0))
# deve printar 0, pois o cursor está na primeira posição
print(lista.acessarAtual())

# deve printar 10, pois o cursor está na última posição
lista.inserirComoUltimo(Nodo(10))
print(lista.acessarAtual())

lista.inserirNaPosicao(2, Nodo(5))
# deve printar 5, pois o cursor está na segunda posição
print(lista.acessarAtual())

print(lista)

lista.inserirAposAtual(Nodo(7))
print(lista.acessarAtual())
print(lista)

lista.inserirAntesDoAtual(Nodo(3))
print(lista.acessarAtual())
print(lista)

lista.inserirAntesDoAtual(Nodo(2))
print(lista.acessarAtual())
print(lista)

print(lista.acessarAtual())
lista.excluirAtual()
print(lista)

lista.excluirPrim()
print(lista.acessarAtual())
print(lista)

lista.excluirUlt()
print(lista.acessarAtual())
print(lista)

lista.excluirElem(7)
print(lista.acessarAtual())
print(lista)

lista.excluirDaPos(2)
print(lista.acessarAtual())
print(lista)

print(lista.buscar(88))
print(lista.buscar(5))
print(lista.buscar(3))"""


# lista 2
print("Inicializando Lista")
lista2 = Lista(7)
print("     Tamanho máximo definido como ->", lista2.tamanho_maximo)
print()
lista2.inserirComoPrimeiro(Nodo(0))
print(lista2)
lista2.inserirComoUltimo(Nodo(10))

print(lista2)
lista2.inserirNaPosicao(2, Nodo(5))
print(lista2)
lista2.inserirNaPosicao(4, Nodo(3))

print(lista2)
lista2.inserirComoPrimeiro(Nodo(91))
print(lista2)
lista2.inserirComoUltimo(Nodo(99))

print(lista2)
print(lista2.acessarAtual())

lista2.excluirAtual()  # deve excluir o 99
print(lista2)

print(lista2.acessarAtual())  # retornou uma posicao atras
lista2.inserirAposAtual(Nodo(999))
print(lista2)
print(lista2.acessarAtual())  # cursor foi para o 999

lista2.inserirAntesDoAtual(Nodo(888))
print(lista2)
print(lista2.acessarAtual())  # cursor foi para o 888

lista2.excluirAtual()  # deve excluir o 888
print(lista2)
print(lista2.acessarAtual())  # cursor foi para o 999

lista2.excluirAtual()  # deve excluir o 999
print(lista2)
print(lista2.acessarAtual())  # cursor foi para o 3

lista2.excluirPrim()
print(lista2)
print(
    lista2.acessarAtual()
)  # cursor se manteve no 3, pq a funcao excluirPrim() nao mexe no cursor

lista2.excluirUlt()
print(lista2)
print(
    lista2.acessarAtual()
)  # cursor se manteve no 3, pq a funcao excluirUlt() nao mexe no cursor

lista2.posicaoDe(3)
print(lista2.posicaoDe(3))

lista2.posicaoDe(5)
print(lista2.posicaoDe(5))

lista2.buscar(99)
print(lista2.buscar(99))

lista2.buscar(10)
print(lista2.buscar(10))

print(lista2)
lista2.excluirDaPos(2)
print(lista2)

print(lista2.acessarAtual())
lista2.inserirAposAtual(Nodo(999))
print(lista2)
