
#modulos & classes
from classesCliniVet import *
import os #para dar clear no terminal
import math
from time import sleep

#função para formatação dos titulos
def printTituloBonitinho(titulo):
    a = math.floor((61 - len(titulo)) / 2)
    print("=-"*30+'=')
    print(' '*a+titulo)
    print("=-"*30+'=')

#flag de controle
flag = False

def menu(op):
    if op == 1:
        os.system('cls')
        printTituloBonitinho('Cadastro Pessoa')
        while True:
            tipo = int(input('Pessoa Física ou Jurídica? \n1 - Física | 2 - Jurídica\n'))
            if tipo == 1 or tipo == 2:
                break
            else: 
                print('Digite uma opção válida. [1/2]')
                print()
        print()
        nome = input("Informe o nome do dono/responsável: ")

        if tipo == 1:
            cpf = input("Informe o CPF (somente números): ")
        elif tipo == 2:
            cnpj = input("Informe o CNPJ (somente números): ")
        else:
            print('Digite um valor válido. ')

        contato = int(input("Informe um telefone de contato: "))

        while True:
            convenio = input("Possui convênio? [S/N] ").upper()
            if convenio == 'S' or convenio == 'N':
                break
        
        if tipo == 1:
            pessoa = PessoaFísica(nome, contato, convenio, cpf)
        if tipo == 2:
            pessoa = PessoaJurídica(nome, contato, convenio, cnpj)
        
        print()
        
        #cadastrar pet (vinculado ao dono)
        while True:
            #os.system('cls')
            printTituloBonitinho('Cadastro Pet')
            nomePet = input('Informe o nome do pet: ')

            while True:
                especie = int(input(f'Informe a espécie de {nomePet}: \n1 - Cachorro | 2 - Gato \n'))
                if especie == 1:
                    especie = 'Cachorro'
                    break
                elif especie == 2:
                    especie = 'Gato'
                    break
                else:
                    print('Digite um número valido. [1/2]')

            while True:
                sexo = input('Informe o sexo do pet: \nF - Fêmea | M - Macho\n').upper()
                if sexo == 'M' or sexo == 'F':
                    break
            
            idadePet = int(input(f"Qual a idade de {nomePet}? "))
            raça = input(f'Qual a raça do {especie}? ')
            peso = float(input(f'Quantos Kg {nomePet} tem? '))

            while True:
                doençaCronica = input('Possui alguma doença crônica? [S/N] ').upper()
                if doençaCronica == 'S' or doençaCronica == 'N':
                    doençaCronica = []
                    break
            if doençaCronica == 'S':
                listaDoenças = []
                while True:
                    doençaCronica = input('Qual(is) doença(s) crônica(s)? Digite 0 para terminar de inserir. ')
                    if doençaCronica == '0':
                        break
                    else:
                        listaDoenças.append(doençaCronica)
                doençaCronica = listaDoenças
            
            #TODO Desenvolver a sessão de Vacinas, pensar no que elaborar propriamente
            vacinas = int(input('As vacinas estão em dia? \n1 - Sim | 2 - Não\n'))
            if vacinas == 2:
                if especie == 1:
                    print('Qual(is) da(s) vacina(s) abaixo seu Pet não tomou? ')
                    print('1 - Raiva')
                    print('2 - Vacina Polivalente')
                    print('3 - Gripe Canina')
                elif especie == 2:
                    print('1 - Panleucopenia')
                    print('2 - Raiva')
                    print('3 - Leucemia Felina')

            motivo = int(input("Qual o motivo da visita na CliniPet?\n1 - Presença de Sintomas \n2 - Exames de Rotina \n3 - Medicamentos\n"))
            
            pet = Animal(nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo)
            pessoa.addPet(pet)
            
            continuar = input(f'Deseja cadastrar outro pet para o cliente {nome}? [S/N]').upper()
            if continuar == 'N':
                print('\n                 ***Cadastro realizado com sucesso!***                 \n')
                clientes.append(pessoa)
                break
    
    elif op == 2:
        os.system('cls')
        while True:
            printTituloBonitinho('Alterar Informações de Cadastro')
            print('1 - Por CPF \n2 - Por CNPJ')
            while True:
                buscar = int(input('Qual será o método de consulta? '))
                if buscar == 1 or buscar == 2:
                    break
                else: 
                    print('Digite uma opção válida. [1/2] ')
            
            if buscar == 1:
                id = input('Digite o CPF do cadastro: ')
                flag = False
                for pf in clientes:
                    if id == pf.getCod() and pf.isFisica():

                        print(f'\nDigite as novas informações do usuário {pf.getNome()}:')
                        nome = input('Nome: ')
                        cpf = input('CPF: ')
                        contato = int(input('Contato: '))
                        convenio = input('Convênio [S/N]').upper()
                            
                        pf.setNome(nome)
                        pf.setCod(cpf)
                        pf.setContato(contato)
                        pf.setConvenio(convenio)
                        flag = True

                if flag == False:
                    print(f"\nNão foi encontrado nenhum cliente registrado no CPF '{id}'")

            else: #buscar == 2
                id = input('Digite o CNPJ do cadastro: ')
                flag = False
                for pj in clientes:
                    if id == pj.getCod() and not pj.isFisica():
                
                        print(f'\nDigite as novas informações do usuário {pj.getNome()}:')
                        nome = input('Nome: ')
                        cnpj = input('CNPJ: ')
                        contato = int(input('Contato: '))
                        convenio = input('Convênio [S/N]').upper()
                            
                        pj.setNome(nome)
                        pj.setCod(cnpj)
                        pj.setContato(contato)
                        pj.setConvenio(convenio)
                        flag = True

                if flag == False:
                    print(f"\nNão foi encontrado nenhum cliente registrado no CNPJ '{id}'")
        
    elif op == 3:
        while True:
            os.system('cls')
            printTituloBonitinho('Consultar Dados')

            print('\n1 - Por Nome \n2 - Por CPF \n3 - Por CNPJ')
            while True: 
                buscar = int(input('Qual será o método de consulta? '))
                if buscar == 1 or buscar == 2 or buscar == 3:
                    break
                else:
                    print('Digite uma opção válida. [1/2/3]')
                    
            if buscar == 1: #consulta por nome
                flag = False
                consulta = input('Digite o nome que deseja buscar: ')
                print()
                for n in clientes:
                    if consulta == n.getNome():
                        print(n.info_cliente())
                        for a in n.animais:
                            a.infoPet()
                        flag = True
                if flag == False:
                    print(f"\nNão foi encontrado nenhum cliente registrado com o nome '{consulta}'")

            elif buscar == 2: #consulta por cpf
                    flag = False
                    consultar = input('Digite o CPF (somente números) que deseja buscar: ')
                    print()
                    for pf in clientes:
                        if consultar == pf.getCod() and pf.isFisica():
                            pf.info_cliente()
                            for a in pf.animais:
                                a.infoPet()
                            flag = True
                    if flag == False:
                        print(f"\nNão foi possível encontrar nenhum cliente registrado no CPF '{consultar}'")   

            else: #buscar == 3: #consulta por cnpj
                flag = False
                consultar = input('Digite o CNPJ (somente números) que deseja buscar: ')
                print()
                for pj in clientes:
                    if consultar == pj.getCod() and not pj.isFisica():
                        pj.info_cliente()
                        for a in pj.animais:
                            a.infoPet()
                        flag = True
                if flag == False:
                    print(f"Não foi possível encontrar nenhum cliente registrado no CNPJ '{consultar}'")
            
            continuar = input('Deseja realizar uma nova consulta? [S/N] ').upper()
            if continuar == 'N':
                break

    elif op == 4:
        os.system('cls')
        printTituloBonitinho('Relação dos Cadastrados na Clínica')
        for i in clientes:
            i.info_cliente()
            for a in i.animais:
                a.infoPet()

        input("Pressione algo para voltar ao menu... ")

    elif op == 5:
        while True:
            os.system('cls')
            printTituloBonitinho('Exclusão de Cadastro')
            while True:
                flag = False
                buscar = int(input('1 - Por CPF \n2 - Por CNPJ\n'))
                if buscar == 1 or buscar == 2:
                    break
                else:
                    print('Digite uma opção válida. [1/2]\n')

            if buscar == 1: #cpf
                excluir = input("\nDigite o CPF que deseja excluir: ")
                for cad, pf in enumerate(clientes):
                    if excluir == pf.getCod() and pf.isFisica():
                        print(f'\n                  ***Cadastro de {pf.getNome()} excluido!***                  ')
                        clientes.pop(cad)
                        flag = True
                if flag == False:
                    print(f"Não encontramos nenhum cadastro no CPF '{excluir}'.")
            else: #excluir == 2: #cnpj
                excluir = input("Digite o CNPJ que deseja excluir: ")
                for cad, pj in enumerate(clientes):
                    if excluir == pj.getCod() and not pj.isFisica():
                        print(f'\n                  ***Cadastro de {pj.getNome()} excluido!***                  ')
                        clientes.pop(cad)
                        flag = True
                if flag == False:
                    print(f"Não encontramos nenhum cadastro no CNPJ '{excluir}'.")
            
            continuar = input("\nDeseja excluir outro cadastro? [S/N] ").upper()
            if continuar == 'N':
                break

    else:
        timer = ['.']*3
        print(f"\nPrograma será encerrado em",end="")
        for i in range(len(timer)):
            print(f'{timer[i]}',end="", flush=True)
            sleep(0.5)
        print()

        timer = 'Programa encerrado com sucesso! :)'
        mensagemFimBranco = ''*len(timer)
        a = math.floor((61 - len(mensagemFimBranco)) / 4)
        print("=-" *30 + '=')
        print(' ' * a, end='')
        for i in range(len(timer)):
            print(f'{timer[i]}',end='', flush=True)
            sleep(0.1)
        print("\n" + "=-" * 30 + '=')
    return op

#main
animais = []
clientes = []

#pessoas já "cadastradas" na CliniPpet
p1 = PessoaFísica('José','1106', 'S', "069") #nome contato convenio cpf
king = Animal('King','M','Cachorro',7,'Vira-Lata',9,['DoençaTeste1', 'DoençaTeste2','DoençaTeste3'],1,1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
p1.addPet(king)
clientes.append(p1)

p2 = PessoaJurídica('VicBusiness','7777', 'N', '123') #nome contato convenio cnpj              
nina = Animal('Nina','F','Gato', 15, 'Meow',4,[],2,1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
donaIzilda = Animal('Dona Izilda', 'F', 'Gato', 15, 'MeowMeow',2,['DoençaTeste4','DoençaTeste5'],1,1)
mustafah = Animal('Mustafáh', 'M', 'Gato', 15, 'MeowMeowMeow', 4,[],2,2 )
p2.addPet(nina)
p2.addPet(donaIzilda)
p2.addPet(mustafah)
clientes.append(p2)

p3 = PessoaFísica('Lucas','0793', 'S', "333") #nome contato convenio cnpj
lua = Animal('Lua', 'F', 'Gato', 4, 'Persa', 5.5, [], 2, 1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
lual = Animal('Sol', 'M', 'Gato', 5, 'Siamês', 6, ['DoençaTeste6','DoençaTeste7'], 2, 1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
p3.addPet(lua)
p3.addPet(lual)
clientes.append(p3)

'''
timer = 'Boas Vindas a CliniPet'
mensagemFimBranco = ''*len(timer)
a = math.floor((61 - len(mensagemFimBranco)) / 4)
print("=-" *30 + '=')
print(' ' * a, end='')
for i in range(len(timer)):
    print(f'{timer[i]}',end='', flush=True)
    sleep(0.1)
print()
'''

while True: #menu da CliniPet
    os.system('cls')
    printTituloBonitinho('Menu da CliniPet')
    print("\nO que deseja fazer?" +
          "\n   1) Realizar novo cadastro" +
          "\n   2) Alterar informações de um cadastro"
          "\n   3) Consultar dados" +
          "\n   4) Relação de todos os cadastros na Clinipet" +
          "\n   5) Excluir um cadastro" +
          "\n   6) Encerrar.")
    print()
    op = menu(int(input()))
    if op == 6:
        break

