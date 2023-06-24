# Exerc 2 - Aula 21

class Funcionario:
    def __init__(self, nome, salarioAtual):
        self.nome = nome
        self.salarioAtual = salarioAtual
        self.salarioReajustado = 0

    
    def getNome(self):
        return self.nome
    
    def setNome(self,nome):
        self.nome = nome
    
    def aumento_salarial(self):
        if self.salarioAtual > 3000:
            self.salarioReajustado = self.salarioAtual * 1.05
        elif self.salarioAtual > 2000:
            self.salarioReajustado = self.salarioAtual * 1.1
        else:
            self.salarioReajustado = self.salarioAtual * 1.2

    
    def info_funcionario(self):
        print(f'Nome do funcionário: {self.nome}')
        print(f'Salário atual: R$ {self.salarioAtual}')
        print(f'Salário reajustado: R$ {self.salarioReajustado:.1f}')
        
