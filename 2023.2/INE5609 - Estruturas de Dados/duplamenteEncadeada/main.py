# importando as classes necessarias
from lista import Lista
from nodo import Nodo
from cursor import Cursor


"""# lista
print("---------------------------------")
print("     Inicializando Lista")
print("---------------------------------")

lista = Lista(7)
print("\nTamanho máximo definido como ->", lista.tamanho_maximo)
print()

lista.inserirComoPrimeiro(Nodo(0))
print(lista)
lista.inserirComoUltimo(Nodo(10))

print(lista)
lista.inserirNaPosicao(2, Nodo(5))
print(lista)
lista.inserirNaPosicao(4, Nodo(3))

print(lista)
lista.inserirComoPrimeiro(Nodo(91))
print(lista)
lista.inserirComoUltimo(Nodo(99))

print(lista)
print(lista.acessarAtual())

lista.excluirAtual()  # deve excluir o 99
print(lista)

print(lista.acessarAtual())  # retornou uma posicao atras
lista.inserirAposAtual(Nodo(999))
print(lista)
print(lista.acessarAtual())  # cursor foi para o 999

lista.inserirAntesDoAtual(Nodo(888))
print(lista)
print(lista.acessarAtual())  # cursor foi para o 888

lista.excluirAtual()  # deve excluir o 888
print(lista)
print(lista.acessarAtual())  # cursor foi para o 999

lista.excluirAtual()  # deve excluir o 999
print(lista)
print(lista.acessarAtual())  # cursor foi para o 3

lista.excluirPrim()
print(lista)
print(
    lista.acessarAtual()
)  # cursor se manteve no 3, pq a funcao excluirPrim() nao mexe no cursor

lista.excluirUlt()
print(lista)
print(
    lista.acessarAtual()
)  # cursor se manteve no 3, pq a funcao excluirUlt() nao mexe no cursor

lista.posicaoDe(3)
print(lista.posicaoDe(3))

lista.posicaoDe(5)
print(lista.posicaoDe(5))

lista.buscar(99)
print(lista.buscar(99))

lista.buscar(10)
print(lista.buscar(10))

print(lista)
lista.excluirDaPos(2)  # exclui o elemento 5 que está na posicao '2'
print(lista)

print(lista.acessarAtual())
lista.inserirAposAtual(Nodo(999))
print(lista)"""

lista = Lista(4)
lista.inserirComoUltimo(Nodo(2))
lista.inserirComoPrimeiro(Nodo(3))
lista.inserirNaPosicao(44, Nodo(9))
print(lista)

lista.posicaoDe(9)
print(lista.posicaoDe(9))

lista.excluirAtual()
print(lista)

lista.inserirAposAtual(Nodo(8))
print(lista.acessarAtual())
print(lista)

lista.inserirAntesDoAtual(Nodo(5))
print(lista.acessarAtual())
print(lista)

lista.excluirUlt()
print(lista.acessarAtual())
print(lista)

lista.excluirPrim()
print(lista.acessarAtual())
print(lista)
