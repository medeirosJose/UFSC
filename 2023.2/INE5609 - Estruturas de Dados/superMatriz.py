""" Como comentamos em aula, o trabalhinho consiste em implementar uma SuperMatriz usando como recurso de suporte unicamente um SuperArray 
(como implementado em aula e compartilhado pelos colegas no grupo de whats!)

Para construir uma SuperMatriz, o construtor recebe 2 argumentos: o número_de_linhas e o número_de_colunas 
que o usuário quer para a sua nova matriz.

As operações da SuperMatriz são:

atribuir ( linha, coluna, valor)
acessar ( linha, coluna ) : retorna o valor daquela [linha, coluna]
As operações devem verificar se o usuário está usando linha/coluna dentro dos limites pré-estabelecidos (no construtor) 
e lançar exceção caso contrário.

Quero poder usar da seguinte forma:

m1 = SuperMatriz ( 3, 4 )  // cria uma matriz de 3x4
m1.atribuir ( 1, 1, 111) // atribui para a posição m(1,1) o valor 111
x = m1.acessar ( 1, 1)  //  x recebe o valor da posição m(1,1)

ENTREGA:

Classe SuperArray
Classe SuperMatriz
um programa que usa a SuperMatriz com ao menos 3 instâncias ( 3x4, 5x5, 2x7 ) """

"""x = int(input("X - "))
y = int(input("Y - "))
j = int(input("J - "))

print(j * (x - 1) + y - 1)"""


# classe do superArray feito em sala de aula
class SuperArray:
    def __init__(self, ini, fim):
        if fim >= ini:
            self.__linf = ini
            self.__lsup = fim
        else:
            self.__linf = fim
            self.__lsup = ini

        self.__dados = [None] * (self.__lsup - self.__linf + 1)

    def atribuir(self, pos, val):
        if (pos > self.__lsup) or (pos < self.__linf):
            raise IndexError("Posição fora do intervalo.")
        else:
            self.__dados[pos - self.__linf] = val

    def acessar(self, pos):
        if (pos > self.__lsup) or (pos < self.__linf):
            raise IndexError("Posição fora do intervalo.")
        else:
            return self.__dados[pos - self.__linf]


class SuperMatriz:
    def __init__(self, linhas, colunas):
        self.__linhas = linhas
        self.__colunas = colunas
        self.array = SuperArray(0, (linhas * colunas) - 1)

    def atribuir(self, linha, coluna, valor):
        # se a linha ou coluna estiverem fora do intervalo, lança um erro
        if linha < 0 or linha > self.__linhas:
            raise IndexError("[ATRIBUIÇÃO] Posição fora do intervalo -> Linha", linha)

        if coluna < 0 or coluna > self.__colunas:
            raise IndexError("[ATRIBUIÇÃO] Posição fora do intervalo -> Coluna", coluna)

        # do contrário, atribui o valor na posição correta
        self.array.atribuir((linha * self.__colunas) + coluna, valor)

    def acessar(self, linha, coluna):
        # novamente, se a linha ou coluna estiverem fora do intervalo, lança um erro
        if linha < 0 or linha > self.__linhas:
            raise IndexError("[ACESSO] Posição fora do intervalo ->", linha)

        if coluna < 0 or coluna > self.__colunas:
            raise IndexError("[ACESSO] Posição fora do intervalo ->", coluna)

        # se não houver nada na posição, retorna ""
        if self.array.acessar((linha * self.__colunas) + coluna) is None:
            # retorna um espaço vazio apenas para fins estéticos
            return ""

        # do contrário, retorna o valor na posição correta
        return self.array.acessar((linha * self.__colunas) + coluna)


# criando instancia de uma matriz 3x4
m1 = SuperMatriz(3, 4)
m1.atribuir(1, 3, 11)
m1.atribuir(2, 2, 33)
m1.atribuir(0, 0, 33)
m1.atribuir(2, 3, 44)
m1.atribuir(0, 3, 55)
A = m1.acessar(1, 3)
# print("A", A)

# criando instancia de uma matrix 1x1
m2 = SuperMatriz(1, 1)
m2.atribuir(0, 0, 666)
B = m2.acessar(0, 0)
# print("B", B)

# criando instancia de uma matrix 5x5
m3 = SuperMatriz(5, 5)
m3.atribuir(4, 4, 33)
m3.atribuir(0, 0, 00)
m3.atribuir(2, 2, 11)
m3.atribuir(1, 1, 44)
m3.atribuir(3, 3, 55)
C = m3.acessar(4, 4)
# print("C", C)

# criando instancia de uma matrix 2x7
m4 = SuperMatriz(2, 7)
m4.atribuir(1, 6, 44)
m4.atribuir(0, 0, 00)
m4.atribuir(1, 1, 11)
m4.atribuir(0, 2, 22)
m4.atribuir(1, 3, 33)
m4.atribuir(0, 4, 44)
m4.atribuir(1, 5, 55)
m4.atribuir(0, 6, 66)
D = m4.acessar(1, 6)
# print("D", D)


# teste de todas as posições possíveis em m1
print("\nSuperMatriz 1")
for i in range(3):
    for j in range(4):
        print(f"m1[ {i} ][ {j} ] =", m1.acessar(i, j))
input("\nDigite algo para prosseguir...")

# teste de todas as posições possíveis em m2
print("\nSuperMatriz 2")
for i in range(1):
    for j in range(1):
        print(f"m2[ {i} ][ {j} ] =", m2.acessar(i, j))
input("\nDigite algo para prosseguir...")

# teste de todas as posições possíveis em m3
print("\nSuperMatriz 3")
for i in range(5):
    for j in range(5):
        print(f"m3[ {i} ][ {j} ] =", m3.acessar(i, j))
input("\nDigite algo para prosseguir...")

# teste de todas as posições possíveis em m4
print("\nSuperMatriz 4")
for i in range(2):
    for j in range(7):
        print(f"m4[ {i} ][ {j} ] =", m4.acessar(i, j))
input("\nDigite algo para prosseguir...")
