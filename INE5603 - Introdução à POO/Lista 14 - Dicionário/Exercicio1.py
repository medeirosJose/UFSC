from datetime import datetime

def menu(op):
    if op ==1:
        #cadastrar
        while True:
            dados['nome']= str(input("Nome: "))
            nasc = int(input('Ano de Nascimento: '))
            dados['idade'] = ((datetime.now().year)-nasc)
            dados['ctps']=int(input('Carteira de trabalho (0 - não tem):'))
            if dados['ctps'] !=0:
                dados['contratacao']= int(input("Ano de Contratação: "))
                dados['salario'] = float(input("Salário: R$ "))
                #verifica a idade que a pessoa terá quando se aposentar (considerando 35 anos de contribuição)
                dados['aposentadoria']= dados['idade'] + ( (dados['contratacao']+35) - datetime.now().year)
            #insere usuário na lista de dicionários
            lista.append(dados.copy())
            print(lista)                              
            novamente = str(input('Cadastrar outra pessoa? [S/N] ')).upper()
            if novamente == 'N':
                break
            
    elif op==2:
        flag = False
        nome = input("Digite o nome: ")
        
        for j in range(len(lista)):               # percorre a lista de pessoas cadastradas
            if lista[j]['nome'] == nome:
                e = lista[j]
                for v in e.values():
                    print(v, end=' ')
                flag = True
        if flag == False:
            print("Nome não encontrado no cadastro.")

    elif op==3:
        #imprimindo o conteudo da estrutura completa (por linha)
        
         for e in lista:
            for v in e.values():
                print(v, end=' ')
            print()
         
    else:
        print("Programa encerrado com sucesso")
    
    return op

#main
dados = dict()
lista = list()

while True:
    print("\nBem vindo ao Sistema de Cadastro")
    print("\nDigite a opção desejada:" +
          "\n1)Cadastrar usuário" +
          "\n2)Pesquisar dados(pelo nome)" +
          "\n3)Imprimir todos os cadastros" +
          "\n4)Encerrar o programa")
    op = menu(int(input()))
    if op == 4:
        break