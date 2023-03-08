# imprimindo uma lista composta

cadastro = [['Ana', 30], ['Camila', 40], ['Arthur', 20], ['Osvaldo',25]]

#imprimindo estrutura completa
print(cadastro)

#imprimindo o conteudo da estrutura completa (por linha)
for i in range(len(cadastro)):
    for j in range(2):
        print(f"{cadastro[i][j]}",end=" ")
    print()

#imprimindo o conteúdo (apenas o nome)
for p in cadastro:  # p recebe a lista que está na posição 0 de cadastro
    print(p[0])     # considerando a lista p - a informação que está na posição 0 = nome

#imprimindo o conteudo (nome e idade)
for p in cadastro:  
    print(f"{p[0]} - {p[1]}")
