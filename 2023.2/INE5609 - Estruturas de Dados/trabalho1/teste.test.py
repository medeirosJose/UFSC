import unittest
from teste import *


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_inserirComoPrimeiro(self):
        self.dll.inserirComoPrimeiro(10)
        self.assertEqual(self.dll.cabeca.dado, 10)

    def test_inserirComoUltimo(self):
        self.dll.inserirComoUltimo(20)
        self.assertEqual(self.dll.cauda.dado, 20)

    def test_inserirNaPosicao(self):
        self.dll.inserirComoPrimeiro(10)
        self.dll.inserirComoUltimo(20)
        self.dll.inserirNaPosicao(1, 15)
        self.assertEqual(self.dll.cabeca.prox.dado, 15)

    def test_ExcluirPrim(self):
        self.dll.inserirComoPrimeiro(10)
        self.dll.inserirComoUltimo(20)
        self.dll.ExcluirPrim()
        self.assertEqual(self.dll.cabeca.dado, 20)

    def test_ExcluirUlt(self):
        self.dll.inserirComoPrimeiro(10)
        self.dll.inserirComoUltimo(20)
        self.dll.ExcluirUlt()
        self.assertEqual(self.dll.cauda.dado, 10)

    def test_ExcluirDaPos(self):
        self.dll.inserirComoPrimeiro(10)
        self.dll.inserirComoUltimo(20)
        self.dll.inserirNaPosicao(1, 15)
        self.dll.ExcluirDaPos(2)
        self.assertEqual(self.dll.cabeca.prox.dado, 20)


if __name__ == "__main__":
    unittest.main()
