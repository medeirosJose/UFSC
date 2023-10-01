from lista import Lista
from nodo import Nodo
from cursor import Cursor


# testes
lista = Lista(4)

lista.inserirComoPrimeiro(Nodo(1))
print("Lista depois de inserirComoPrimeiro ->", lista)
lista.inserirComoUltimo(Nodo(5))
print("Lista antes de inserirNaPosicao ->", lista)
print("Cursor->", lista.cursor.posicao)

print("\n\ntentando inserir na posicao 20 o elemento 77")
lista.inserirNaPosicao(20, Nodo(55))
print("Cursor ->", lista.cursor.posicao)
print("LISTA OLHA AQUI depois de inserirNaPosicao ->", lista)

print("\n\ntentando inserir na posicao 25 o elemento 44")
print("Cursor TESTE->", lista.cursor.posicao)
lista.inserirNaPosicao(25, Nodo(44))
print("LISTA OLHA AQUI 2 depois de inserirNaPosicao ->", lista)

print("Cursor ->", lista.cursor.posicao)
# printar cursor
print()
print()
print()

lista.inserirNaPosicao(3, Nodo(3))
print("Cursor ->", lista.cursor.posicao)

print("Lista depois de inserirNaPosicao ->", lista)
lista.inserirComoPrimeiro(Nodo(0))
print("Lista depois de inserirComoPrimeiro ->", lista)

lista.inserirComoUltimo(Nodo(99))
print("Lista depois de inserirComoUltimo ->", lista)
lista.inserirComoPrimeiro(Nodo(99))
# printar cursor
print("Cursor ->", lista.cursor.posicao)

lista.buscar(99)
print("Cursor ->", lista.cursor.posicao)
print(lista.buscar(99))

print(lista.posicaoDe(99))
print(lista.posicaoDe(55))
print(lista.posicaoDe(44))
print(lista.posicaoDe(300))
