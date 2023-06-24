nome = list()
print(nome)
nome.append(123)
print(nome)
nome.append("Maria")
print(nome)
nome.insert(1,"Joaquim")
print(nome)

#imprimindo o conteúdo de uma lista
for i in nome:
    print(i)

#imprimindo o conteúdo de uma lista, pela posição
for i in range(len(nome)):
    print(i,":",nome[i])
    
#imprimindo usando o enumerate
for pos,valor in enumerate(nome):
    print("Na posição:", pos, "valor: ", valor)
    
    
