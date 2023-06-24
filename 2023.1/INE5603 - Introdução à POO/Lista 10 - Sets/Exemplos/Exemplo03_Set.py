'''# Definindo dois conjuntos de número
c1 = {2, 10}
c2 = {10, 14, 8, 2}
print(c1,c2)

# True se c1 e c2 são disjuntos, ou seja, se eles não têm elementos em comum
print(c1.isdisjoint(c2))

#subconjunto
#retorna True se C1 estiver contido em C2
print(c1.issubset(c2))


# Subconjunto próprioc3)
#retorna True se C1 estiver contido em C2 e C1 for diferente de C2.
print(c1 < c2)

'''
#União dos conjuntos
# União dos conjuntos
c1 = {1,2,3,4,10}
c2 = {10, 14, 8, 2}
c3 = {-5, 10}
print(c1.union(c2, c3))
print(c1)
conjunto_uniao = c1.union(c2,c3)
print(conjunto_uniao)


#Remove um elemento do conjunto se ele estiver presente.
#Não acusa erro caso o elemento não pertença ao conjunto
c3.discard(10)
print(c3)
c3.discard(100)
print(c3)

#Remove um elemento do conjunto se ele estiver presente.
#Acusa erro caso o elemento não pertença ao conjunto
print(c1)
c1.remove(10)
print(c1)
# Remove e retorna um elemento arbitrário do conjunto
c1.pop()
print(c1)

