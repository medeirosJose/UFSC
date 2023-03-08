#implementando herança
from herança_Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self,nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj
    
    def getCnpj(self):
        return self.cnpj
    
    def setCnpj(self,cnpj):
        self.cnpj = cnpj
    
    def __str__(self):
        super().__str__()
        print(f"CNPJ: {self.cnpj}")


        