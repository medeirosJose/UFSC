'''
Implementar um algoritmo que defina a classe Pessoa,
com 3 propriedades: nome, idade, identificação
(considerando que uma pessoa pode ser
Pessoa Física (possui cpf) ou Pessoa Jurídica (possui cnpj)
'''

from herança_PessoaFisica import PessoaFisica
from herança_PessoaJuridica import PessoaJuridica


#main
'''tipo = int(input())
nome = input('nome')
idade = int(input('idade'))
if tipo == 1:
    cpf = input('cpf')
    teste = PessoaFisica(nome, idade, cpf)
if tipo == 2:
    cnpj = input('cnpj')
    teste = PessoaJuridica(nome, idade, cnpj)
'''
#p1 = PessoaFisica("Ana Maria", 30, "927.715.678-09")
#p2 = PessoaJuridica("Angeloni", 50, "11.222.333/0001-99")
p3 = PessoaFisica(cpf="123.456.789.-99",nome="Paulo", idade=35)

#print(p3)

p3.__str__()

#p3.__str__()
