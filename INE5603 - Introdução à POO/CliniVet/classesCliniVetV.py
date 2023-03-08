
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
    def getAnimais(self):
        return self.animais


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
    def __init__(self, nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, motivo):
        self.nomePet = nomePet
        self.sexo = sexo
        self.especie = especie
        self.idadePet = idadePet
        self.raça = raça
        self.peso = peso
        self.doençaCronica = doençaCronica
        #self.vacinas = vacinas
        self.motivo = motivo
        self.procedimentos = []
    
    def getNome(self):
        return self.nomePet
    def setNome(self, nome):
        self.nomePet = nome

    def getProcedimento(self):
        return self.procedimentos
    def setProcedimento(self, procedimento):
        self.procedimentos.append(procedimento)

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
                    
        #TODO Excluir depois.
        if self.motivo == 1:
            self.motivo = 'Presença de Sintomas'
        elif self.motivo == 2:
            self.motivo = 'Exames de Rotina'
        elif self.motivo == 3:
            self.motivo = 'Medicamentos'
        else:
            self.motivo = 'Cirurgia'

        print(f'       Está na clínica por conta de {self.motivo}.')
        print()

    def historicoProcedimentos(self):
        if len(self.procedimentos) == 0:
            print(f'\n{self.nomePet} não realizou nenhum procedimento em nossa clínica.')
        else:
            print(f'\n{self.nomePet} realizou o(s) seguinte(s) procedimento(s) em nossa clínica: ')
            for proced in self.procedimentos:
                print(f'\n{proced.get_tipo()} ' +
                    f'\nProfissional responsável: {proced.get_profissional()}' +
                    f'\nValor: R${proced.get_valor()}')

#super-classe dos procedimentos realizados na clínica
class Procedimento():
    def __init__(self, tipo, profissional, valor, convenio):
        self.tipo = tipo
        self.profissional = profissional
        self.valor = valor
        self.convenio = convenio

    def get_tipo(self):
        return self.tipo
    def get_profissional(self):
        return self.profissional
    def get_valor(self):
        return self.valor


    def set_tipo(self, tipo):
        self.tipo = tipo
    def set_profissional(self, profissional):
        self.profissional = profissional
    def set_valor(self, valor):
        self.valor = valor
    def set_convenio(self, convenio):
        self.convenio = convenio

    def custo_procedimento(self):
        if self.convenio == "S":
            self.valor = self.valor*0.75

#sub-classes de opções de procedimentos
class Consulta(Procedimento):
    def __init__(self, tipo, profissional, valor, convenio):
        super().__init__(tipo, profissional, valor, convenio)


class Exame(Procedimento):
    def __init__(self, tipo, profissional, valor, convenio):
        super().__init__(tipo, profissional, valor, convenio)


class Cirurgia(Procedimento):
    def __init__(self, tipo, profissional, valor, convenio):
        super().__init__('Cirurgia de ' + tipo, profissional, valor, convenio)

    def custo_procedimento(self):
        if self.convenio == "S":
            self.valor = self.valor*0.9


class Vacina(Procedimento):
    def __init__(self, tipo, profissional, valor, convenio):
        super().__init__('Vacina ' + tipo, profissional, valor, convenio)
    

class Internacao(Procedimento):
    def __init__(self, tipo, profissional, valor, qtd_dias, convenio):
        super().__init__(tipo, profissional, valor, convenio)
        self.qtd_dias = qtd_dias

    def get_qtd_dias(self):
        return self.qtd_dias

    def set_qtd_dias(self, qtd_dias):
        self.qtd_dias = qtd_dias

    def custo_procedimento(self):
        if self.convenio == "S":
           self.valor = self.valor*self.qtd_dias*0.9


#dicionários com valores dos procedimentos
tiposProcedimentos = {"cirurgia":2000.00, "vacina":30.00, "internacao":100.00}
tiposConsultas = {"geral":210.00, "especialista": 405.00, "retorno":0.00}
tiposExames = {"sangue":50.00, "ultrassom":110.00, "raioX":60.00}
