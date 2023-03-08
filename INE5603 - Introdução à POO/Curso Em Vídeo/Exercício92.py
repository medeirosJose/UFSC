pessoa = {}
trabalhadores = []

def menu(op):
    if op == 1:
        while True:
            pessoa['nome'] = str(input('Digite o nome: '))
            nascimento = int(input("Digite o ano de seu nascimento: "))
            pessoa['idade'] = 2022 - nascimento
            pessoa['ctps'] = int(input('Digite sua carteira de trabalho - se não tiver, digite 0: '))

            if pessoa['ctps'] != 0:
                pessoa['anoContratação'] = int(input('Digite o ano de contratação: '))
                pessoa['salario'] = int(input('Digite seu salário em reais: R$ '))
                pessoa['aposentadoria'] = pessoa['anoContratação'] + 35
            else:
                pessoa['anoContratação'] = 0
                pessoa['salario'] = 0
                pessoa['aposentadoria'] = 0

            trabalhadores.append(pessoa.copy())
            print()

    if op == 2:
        check = False
        nome = str(input("Digite o nome que deseja pesquisar: "))
        print()
        for i in range(len(trabalhadores)):
            if trabalhadores[i]['nome'] == nome:
                e = trabalhadores[i]
                for v in e.values():
                    print(v,end=' ')
                    check = True
        if check == False:
            print("Nenhum usuário encontrado.")
    if op == 3:
        for i in trabalhadores:
            print(i)

#main
while True:
    print("\nBem vindo ao Sistema de Cadastro")
    print("\nDigite a opção desejada:" +
          "\n1)Cadastrar usuário" +
          "\n2)Pesquisar dados(pelo nome)" +
          "\n3)Imprimir todos os cadastros" +
          "\n4)Encerrar o programa")
    
    op = menu(int(input('\n')))
    if op == 4:
        break