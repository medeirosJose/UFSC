
#modulos & classes
from classesCliniVetV import *
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

def Procedimento(cliente):
    procedimento = int(input("Qual o tipo de procedimento foi realizado?\n"
                            "1 - Consulta\n"
                            "2 - Exame\n"
                            "3 - Cirurgia\n"
                            "4 - Vacina\n"
                            "5 - Internação\n"))

    # inserir valores dos objetos de acordo com o procedimento realizado

    profissional = (input("Qual o nome do profissional responsável: ")).capitalize()
    convenio = cliente.getConvenio()

    if procedimento == 1:
        tipo = int(input("Qual tipo de consulta foi realizada?\n"
                        "1 - Geral\n"
                        "2 - Especialista\n"
                        "3 - Retorno\n"))
        if tipo == 1:
            tipo = "Consulta Geral"
            valor = tiposConsultas["geral"]
        elif tipo == 2:
            tipo = "Consulta com Especialista"
            valor = tiposConsultas["especialista"]
        else:
            tipo = "Consulta de Retorno"
            valor = tiposConsultas["retorno"]

        usuario = Consulta(tipo, profissional, valor, convenio)
        usuario.custo_procedimento()
        
    elif procedimento == 2:
        tipo = int(input("Qual tipo de exame foi realizado?\n"
                         "1 - Sangue\n"
                         "2 - Ultrassom\n"
                         "3 - Raio X\n"))
        if tipo == 1:
            tipo = "Exame de Sangue"
            valor = tiposExames["sangue"]
        elif tipo == 2:
            tipo = "Exame de Ultrassom"
            valor = tiposExames["ultrassom"]
        else:
            tipo = "Exame de Raio X"
            valor = tiposExames["raioX"]
        usuario = Exame(tipo, profissional, valor, convenio)
        usuario.custo_procedimento()

    elif procedimento == 3:
        tipo = input(f"Digite o tipo da cirurgia: ").capitalize()
        valor = (tiposProcedimentos["cirurgia"])
        usuario = Cirurgia(tipo, profissional, valor, convenio)
        usuario.custo_procedimento()

    elif procedimento == 4:
        tipo = input(f"Digite o tipo da vacina: ").capitalize()
        valor = tiposProcedimentos["vacina"]
        usuario = Vacina(tipo, profissional, valor, convenio)
        usuario.custo_procedimento()

    else:
        tipo = "Internação"
        valor = tiposProcedimentos["internacao"]
        qtd_dias = int(input(f"Quantos dias ficou internado(a)? "))
        usuario = Internacao(tipo, profissional, valor, qtd_dias, convenio)
        usuario.custo_procedimento()

    return usuario

def CadastrarProcedimento():
    procedimentosEmAberto = []

    while True:
        flag1 = False
        flagAux = False
        consulta = input('Digite o CPF ou CNPJ que deseja buscar: ')

        for i in clientes:
            if consulta == i.getNome() or consulta == i.getCod():
                print(f'Cliente {i.getNome()} encontrado!\n')
                flag1 = True
                
                while True:
                    # lista de procedimentos que não foram pagos ainda
                    procedimentosEmAberto.append(Procedimento(i))
                    
                    while True:
                        pet = input('Digite o nome do animal: ').capitalize()
                        flag2 = False
                        for a in i.getAnimais():
                            if pet == a.getNome():
                                print('Animal encontrado! Procedimento registrado com sucesso.')
                                flag2 = True
                                flagAux = True #verifica se tem pelo menos um item na lista
                                break
                        if flag2 == False:
                            print(f'Animal "{pet}" não encontrado!')
                            tentarDeNovo = input('Deseja tentar novamente? [S/N] ').upper()
                            if tentarDeNovo == 'N':
                                break
                        else:
                            break
                    continuar = input("Deseja cadastrar outro procedimento? [S/N] ").upper()
                    if continuar == "N":
                        break
        if flag1 == False:
            continuar = input('Cliente não encontrado! Tentar novamente? [S/N] ').upper()
            if continuar == 'N':
                break
        else:
            break
    if flagAux == True:
        total = 0.00

        for proced in procedimentosEmAberto:
            a.setProcedimento(proced)
            total += float(proced.get_valor())

        print(f"\n      O valor total a pagar é de R${total}\n")    
        input("Pressione algo para voltar ao menu... ")

def menu(op):
    #Realizar novo cadastro
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
        nome = input("Informe o nome do dono/responsável: ").capitalize()

        if tipo == 1:
            cpf = input("Informe o CPF (somente números): ")
        else: # tipo == 2:
            cnpj = input("Informe o CNPJ (somente números): ")

        contato = int(input("Informe um telefone de contato (somente números): "))

        while True:
            convenio = input("Possui convênio? [S/N]").upper()
            if convenio == 'S' or convenio == 'N':
                break
        
        if tipo == 1:
            pessoa = PessoaFísica(nome, contato, convenio, cpf)
        if tipo == 2:
            pessoa = PessoaJurídica(nome, contato, convenio, cnpj)
        
        print()
        
        #cadastrar pet (vinculado ao dono)
        while True:
            os.system('cls')
            printTituloBonitinho('Cadastro Pet')
            nomePet = input('Informe o nome do pet: ').capitalize()

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
                    break
            if doençaCronica == 'S':
                listaDoenças = []
                while True:
                    doençaCronica = input('Qual(is) doença(s) crônica(s)? Digite 0 para terminar de inserir. ').capitalize()
                    if doençaCronica == '0':
                        break
                    else:
                        listaDoenças.append(doençaCronica)
                doençaCronica = listaDoenças
            else:
                doençaCronica = []
            
            #TODO Desenvolver a sessão de Vacinas, pensar no que elaborar propriamente
            '''vacinas = int(input('As vacinas estão em dia? \n1 - Sim | 2 - Não\n'))
            if vacinas == 2:
                if especie == 'Cachorro':
                    print('Qual(is) da(s) vacina(s) abaixo seu Pet não tomou? ')
                    print('1 - Raiva')
                    print('2 - Vacina Polivalente')
                    print('3 - Gripe Canina')
                elif especie == 'Gato':
                    print('1 - Panleucopenia')
                    print('2 - Raiva')
                    print('3 - Leucemia Felina')'''

            while True:
                motivo = int(input("Qual o motivo da visita na CliniPet?\n1 - Presença de Sintomas \n2 - Exames de Rotina \n3 - Medicamentos\n4 - Cirurgia"))
                if motivo >= 1 and motivo <= 4:
                    break
                print('Digite uma opção válida. [1...4] ')

            if motivo == 1:
                motivo = 'Presença de Sintomas'
            elif motivo == 2:
                motivo = 'Exames de Rotina'
            elif motivo == 3:
                motivo = 'Medicamentos'
            else:
                motivo = 'Cirurgia'
            
            pet = Animal(nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, motivo) #foi-se o atributo vacinas tchau
            pessoa.addPet(pet)
            
            continuar = input(f'Deseja cadastrar outro pet para o cliente {nome}? [S/N]').upper()
            if continuar == 'N':
                print('\n                 ***Cadastro realizado com sucesso!***                 ')
                clientes.append(pessoa)
                input("\nPressione algo para voltar ao menu... ") #apenas pra segurar nessa tela e não ir direto ao menu
                break
    #Alterar informações de um cadastro
    elif op == 2: #TODO Fazer quebra do loop
        os.system('cls')
        while True: #TODO Fazer quebra do loop #TODO Fazer quebra do loop #TODO Fazer quebra do loop #TODO Fazer quebra do loop
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

                        print('\n         ***Alterações do cadastro realizadas com sucesso!***         ')

                if flag == False:
                    print(f"\nNão foi encontrado nenhum cliente registrado no CPF '{id}'")

            else: #buscar == 2
                id = input('Digite o CNPJ do cadastro: ')
                flag = False
                for pj in clientes:
                    if id == pj.getCod() and not pj.isFisica():
                
                        print(f'\nDigite as novas informações do usuário {pj.getNome()}:')
                        nome = input('Nome: ').capitalize()
                        cnpj = input('CNPJ: ')
                        contato = int(input('Contato: '))
                        convenio = input('Convênio [S/N]').upper()
                            
                        pj.setNome(nome)
                        pj.setCod(cnpj)
                        pj.setContato(contato)
                        pj.setConvenio(convenio)
                        flag = True

                        print('         ***Alterações do cadastro realizadas com sucesso!***         ')

                if flag == False:
                    print(f"\nNão foi encontrado nenhum cliente registrado no CNPJ '{id}'")
            
    #Consultar dados
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
                consulta = input('Digite o nome que deseja buscar: ').capitalize()
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
    #Relação de todos os cadastros na Clinipet
    elif op == 4:
        os.system('cls')
        printTituloBonitinho('Relação dos Cadastrados na Clínica')
        for i in clientes:
            i.info_cliente()
            for a in i.animais:
                a.infoPet()

        input("Pressione algo para voltar ao menu... ")

    #Excluir um cadastro
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
    #exibir histórico de procedimentos de um animal
    elif op == 6:
        while True:
            flag1 = False
            consulta = input('Digite o CPF ou CNPJ que deseja buscar: ')
            for i in clientes:
                if consulta == i.getNome() or consulta == i.getCod():
                    print(f'Cliente {i.getNome()} encontrado!')
                    flag1 = True
                    while True:
                        flag2 = False
                        pet = input('\nDigite o nome do animal: ').capitalize()
                        for a in i.getAnimais():
                            if pet == a.getNome():
                                print('Animal encontrado!')
                                flag2 = True
                                a.historicoProcedimentos()
                                break
                        if flag2 == False:
                            print('Animal não encontrado!')
                            tentarDeNovo = ('Deseja tentar novamente? [S/N] ').upper()
                            if tentarDeNovo == 'N':
                                break
                        else:
                            break
            if flag1 == False:
                continuar = input('Cliente não encontrado! Tentar novamente? [S/N]')
                if continuar == 'N':
                    break
            else:
                break
        input("\nPressione algo para voltar ao menu... ")

    # cadastrar novo procedimento
    elif op == 7:
        CadastrarProcedimento()
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
king = Animal('King','M','Cachorro',7,'Vira-Lata',9,['DoençaTeste1', 'DoençaTeste2','DoençaTeste3'],1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
p1.addPet(king)
clientes.append(p1)

p2 = PessoaJurídica('VicBusiness','7777', 'N', '123') #nome contato convenio cnpj              
nina = Animal('Nina','F','Gato', 15, 'Meow',4,[],1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
donaIzilda = Animal('Dona Izilda', 'F', 'Gato', 15, 'MeowMeow',2,['DoençaTeste4','DoençaTeste5'],1)
mustafah = Animal('Mustafáh', 'M', 'Gato', 15, 'MeowMeowMeow', 4,[],2 )
p2.addPet(nina)
p2.addPet(donaIzilda)
p2.addPet(mustafah)
clientes.append(p2)

p3 = PessoaFísica('Lucas','0793', 'S', "333") #nome contato convenio cnpj
lua = Animal('Lua', 'F', 'Gato', 4, 'Persa', 5.5, [], 1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
lual = Animal('Sol', 'M', 'Gato', 5, 'Siamês', 6, ['DoençaTeste6','DoençaTeste7'], 1) #nomePet, sexo, especie, idadePet, raça, peso, doençaCronica, vacinas, motivo):
p3.addPet(lua)
p3.addPet(lual)
clientes.append(p3)

while True: #menu da CliniPet
    #os.system('cls')
    print()
    printTituloBonitinho('Menu da CliniPet')
    print("\nO que deseja fazer?" +
          "\n   1) Realizar novo cadastro" +
          "\n   2) Alterar informações de um cadastro" +
          "\n   3) Consultar dados" +
          "\n   4) Relação de todos os cadastros na Clinipet" +
          "\n   5) Excluir um cadastro" +
          "\n   6) Verificar histórico de procedimentos de um animal" +
          "\n   7) Cadastrar novo procedimento" +
          "\n   8) Encerrar.")
    print()
    op = menu(int(input()))
    if op == 8:
        break

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

