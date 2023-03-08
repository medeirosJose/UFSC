#implementando herança
from herança_Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self,nome, idade,cpf):
        super().__init__(nome, idade)
        self.cpf = cpf
    
    def getCpf(self):
        return self.cpf
    
    def setCpf(self,cpf):
        self.cpf = cpf
    
    def __str__(self):
        super().__str__()
        print(f"CPF: {self.cpf}")
