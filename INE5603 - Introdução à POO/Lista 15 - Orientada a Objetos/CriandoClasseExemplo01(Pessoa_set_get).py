#usando métodos acessores para ler e alterar o conteúdo de um atributo

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self,nome):
        self.nome = nome
    
    def set_idade(self,idade):
        self.idade = idade
        
        
#main
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
p1 = Pessoa(nome, idade)
p2 = Pessoa("Ana", 45)

#print(p1)
print(p1.get_nome())
print(p1.get_idade())

#exemplo do uso do set
nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))
p3 = Pessoa(nome, idade)
print(p3.get_nome())

# quando quer alterar o valor do atributo, passa o novo valor por parâmetro
#ou p2.setNome("Maria")
p3.set_nome(input("Digite o novo nome:"))
print("Nome atualizado: ",p3.get_nome())