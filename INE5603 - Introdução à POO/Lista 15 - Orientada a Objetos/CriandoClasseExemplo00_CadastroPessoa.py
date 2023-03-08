#Exemplo 001
#cadastro de Pessoa

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def consulta_nome(self):
        return self.nome
    
    def consulta_idade(self):
        return self.idade
    
    def altera_nome(self,nome):
        self.nome = nome
    
    def altera_idade(self,idade):
        self.idade = idade
        
        
#main

#lendo valores do teclado para criar um objeto (instancia) da Classe Pessoa
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
#p1 é um objeto, ou seja, uma instância da Classe Pessoa
p1 = Pessoa(nome, idade)


#consultando as informações cadastradas:
print("Imprimindo dados pessoa 1:")
#print("Pessoa 1:", p1)
print("Nome: ",p1.nome)
print("Idade: ",p1.idade)

'''
print("Imprimindo dados da instância cadastrada no código fonte:")
print("Nome: ",p2.nome)
print("Idade: ",p2.idade)
'''

#alterando a informação de um objeto
#exemplo do uso do método
nome = input("Digite novo nome para Pessoa 1: ")
idade = int(input("Digite nova idade para Pessoa 1: "))
print("Nome original: ", p1.consulta_nome())
p1.altera_nome(nome)
print("Nome atualizado: ", p1.consulta_nome())
p1.altera_idade(idade)
print("Idade atualizada: ", p1.consulta_idade())

