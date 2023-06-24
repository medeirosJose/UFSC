#como criar uma lista composta
# atenção: usar cópia sem vínculo e lembrar de limpar a lista auxiliar

dados = list()
cadastro = list() # cadastro será a lista que armazenará as outras listas 

for i in range(3):
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    dados.append(int(input("Idade: ")))
    print(dados)
    cadastro.append(dados[:]) #inseriu a lista dados dentro da lista cadastro
    print(cadastro)
    dados.clear() #limpa a lista dados

print("Dados: ",dados)
print("Cadastro completo: ",cadastro)