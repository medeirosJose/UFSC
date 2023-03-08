'''Criar um programa que cadastre informações de uma pessoa. • Informações: nome, idade e peso.
Seu sistema deve ser capaz de cadastrar, atualizar e imprimir as
informações da pessoa cadastrada.'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def atualizarNome(self, nome):
        self.nome = nome
    
    def atualizarIdade(self, idade):
        self.idade = idade
    
    def consultaNome(self):
        return self.nome 
    
    def consultaIdade(self):
        return self.idade


#main

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
p1 = Pessoa(nome, idade)

print('\natualização')
nome = input('Novo nome: ')
idade = int(input('Nova idade: ')) 

print('\nNome original',p1.consultaNome())
p1.atualizarNome(nome)
print('Novo nome:',p1.consultaNome())

print('Idade original:',p1.consultaIdade())
p1.atualizarIdade(idade)
print('Idade nova:', p1.consultaIdade())

