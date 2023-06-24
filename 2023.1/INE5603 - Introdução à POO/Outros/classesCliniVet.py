
class Clinica:
    pass

class Cliente:
    def __init__(self, nome, contato, convenio): #classe pai / mais genérica
        self.nome = nome
        self.contato = contato
        self.convenio = convenio
        self.animais = []
    
    def addPet(self, pet):
        self.animais.append(pet)

    def consultarPets(self):
        for pets in self.animais:
            print(pets)

    def setNome(self,nome):
        self.nome = nome
    def setContato(self,contato):
        self.contato = contato
    def setConvenio(self,convenio):
        self.convenio = convenio

    def getNome(self):
        return self.nome
    def getContato(self):
        return self.contato
    def getConvenio(self):
        return self.convenio

class PessoaFísica(Cliente): #classe filha de Cliente HERANÇA (CPF)

    def __init__(self, dono, contato, convenio, cpf ):
        super().__init__(dono, contato, convenio)
        self.cpf = cpf
    
    def isFisica(self):
        return True

    def getCod(self):
        return self.cpf
    
    def setCod(self,cpf):
        self.cpf = cpf

    #talvez seja possível evitar a redundancia de infocliente em cpf e cnpj
    def info_cliente(self):
        print(f"Nome: {self.nome} \nCPF: {self.cpf} \nContato: {self.contato} \nConvênio: {self.convenio}") 

class PessoaJurídica(Cliente): #classe filha de Cliente (CNPJ)
    def __init__(self, dono, contato, convenio, cnpj):
        super().__init__(dono, contato, convenio)
        self.cnpj = cnpj

    def getCod(self):
        return self.cnpj

    def isFisica(self):
        return False

    def setCod(self,cnpj):
        self.cpf = cnpj

    def info_cliente(self):
        print(f"Nome: {self.nome} \nCNPJ: {self.cnpj} \nContato: {self.contato} \nConvênio: {self.convenio}") 


class Animal:
    def __init__(self, nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
        self.nomePet = nomePet
        self.sexo = sexo
        self.especie = especie
        self.idadePet = idadePet
        self.raça = raça
        self.peso = peso
        self.doençaCronica = doençaCronica
        self.vacinas = vacinas
        self.motivo = motivo
    
    '''def addDoença(self, doençaCronica):
        self.listaDoenças.append(doençaCronica)'''
    
    def infoPet(self):
        print(f'    -> {self.nomePet} ({self.sexo}) é um {self.especie} da raça {self.raça} com {self.peso}Kg.')
        if len(self.doençaCronica) == 0:
            print('       Não possui doenças crônicas.')
        else:
            print(f'       Possui {len(self.doençaCronica)} doenças crônicas, sendo elas: ',end='')
            for doença in self.doençaCronica:
                if doença != self.doençaCronica[len(self.doençaCronica)-1]:
                    print(doença, end=', ')
                else: 
                    print(doença, end='.\n')
        print(f'       Vacinas: {self.vacinas} e está na clínica para {self.motivo}.')
        print()
