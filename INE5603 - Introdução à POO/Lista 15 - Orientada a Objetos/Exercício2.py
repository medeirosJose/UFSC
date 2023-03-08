'''2) Implementar um programa que calcule o aumento de salário dos funcionários de uma empresa.
O aumento está condicionado ao atual salário de cada funcionário.

Regras:
• para abaixo ou igual a R$2.000,00 : aumento de 15%;
• para 2.000,00 < salarioAtual < = 3.000,00: aumento de 10%;
• para acima de 3.000,00: aumento igual a 5%.

• Calcular o aumento de 3 funcionários;

• A cada cálculo efetuado imprimir as seguintes informações: nome do funcionário, salário atual e salário com reajuste.

• Devem ser implementadas 2 arquivos (.py):
    • Um arquivo contendo uma classe Funcionário que conterá os métodos para calcular o aumento de salárioe o construtor.
    • Um arquivo contendo o controle_do_Funcionário (main), onde serão feitas chamadas para criar instâncias
da classe Funcionário e também acessar os métodos que pertencem a classe Funcionário.'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.novoSalario = 0
    
    def verificarReajuste(self):
        if self.salario <= 2000:
            novoSalario = (self.salario * 1.15)

        elif self.salario > 2000 and self.salario < 3000:
            novoSalario = (self.salario * 1.10)

        else:
            novoSalario = (self.salario * 1.05)

        return novoSalario

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def informacao(self):
        print(f'Nome do funcionário -> {self.nome}')
        print(f'Salário atual do funcionário -> {self.salario}')
        print(f'Salário reajustado do funcionário -> {self.verificarReajuste()}')


#main
equipe = []

for i in range(3):
    nome = input('   Nome: ')
    salario = int(input('   Salario: '))
    print()

    funcionario = Funcionario(nome,salario)
    equipe.append(funcionario)

for f in equipe:
    # print(f) também irá printar o local de memória
    f.verificarReajuste()
    f.informacao()
    print()

#print(equipe) irá printar o local de memória
