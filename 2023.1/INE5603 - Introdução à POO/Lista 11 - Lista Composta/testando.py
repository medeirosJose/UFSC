
from random import randint
import time

ordem = 10000

start_time = time.time()
matrizL = [[randint(0,10) for i in range(ordem)] for k in range(ordem)]
print("1--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
matrizL = [[randint(0,10) for i in range(ordem)] for k in range(ordem)]
print("2--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
matrizL = [[randint(0,10) for i in range(ordem)] for k in range(ordem)]
print("3--- %s seconds ---" % (time.time() - start_time))

matriz = []

start_time = time.time()
for l in range(ordem):
        linha = []
        for c in range(ordem):
            numero = randint(0,10)
            linha.append(numero)
        matriz.append(linha)
print("11--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for l in range(ordem):
        linha = []
        for c in range(ordem):
            numero = randint(0,10)
            linha.append(numero)
        matriz.append(linha)
print("22--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for l in range(ordem):
        linha = []
        for c in range(ordem):
            numero = randint(0,10)
            linha.append(numero)
        matriz.append(linha)
print("33--- %s seconds ---" % (time.time() - start_time))

