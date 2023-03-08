# estruturar o código usando funções (def)

'''
Aula 18 | URI 1281
Dicionário
Ian Macedo/Luciana

Dona Parcinova costuma ir regularmente à feira para
comprar frutas e legumes. Ela pediu então à sua filha,
Mangojata, que a ajudasse com as contas e que fizesse
um programa que calculasse o valor que precisa levar
para poder comprar tudo que está em sua lista de
compras, considerando a quantidade de cada tipo de
fruta ou legume e os preços destes itens.

A primeira linha de entrada contém um inteiro N que
indica a quantidade de idas à feira de dona Parcinova
(que nada mais é do que o número de casos de teste que
vem a seguir). Cada caso de teste inicia com um
inteiro M que indica a quantidade de produtos que
estão disponíveis para venda na feira. Seguem os M
produtos com seus preços respectivos por unidade ou Kg.
A próxima linha de entrada contém um inteiro
P (1 ≤ P ≤ M) que indica a quantidade de diferentes
produtos que dona Parcinova deseja comprar. Seguem P
linhas contendo cada uma delas um texto
(com até 50 caracteres) e um valor inteiro, que
indicam respectivamente o nome de cada produto e a
quantidade deste produto.

Para cada caso de teste, imprima o valor que será
gasto por dona Parcinova no seguinte formato:
R$ seguido de um espaço e seguido do valor, com 2
casas decimais, conforme o exemplo abaixo.

'''
# lê a quantidade N de idas à feira (num de casos de teste)
# lê a quantidade M de produtos disponíveis na feira, naquela ida
# lê o nome e preço dos produtos
# lê a quantidade P de produtos que Parcinova quer comprar
# lê P entradas, contendo o nome e a quantidade compradas
# imprima o valor gasto por Parcinova na ida à feira

N = int(input('Quantas vezes Parcinova foi à feira: '))  # número de casos de teste

produtos = [{'nome': 'mamao' , 'preco': 2.19},
            {'nome': 'cebola', 'preco': 3.10},
            {'nome': 'tomate', 'preco': 2.80},
            {'nome': 'uva', 'preco': 2.73}]

for ida in range(N):
    
    M = int(input('Quantos produtos estão disponíveis? '))
    #produtos = []

    for i in range(M):
        # preenche uma lista de dicionários, com nome e preço dos produtos da feira
        produto = input(f'Produto {i} - Nome e preço: ').split()
        info = {'nome': produto[0], 'preco': float(produto[1])}
        produtos.append(info.copy())
    

    P = int(input('Quantos produtos Parcinova quer comprar? '))
    comprou = []
    
    for e in produtos:
        for v in e.values():
            print(v, end=' ')
        print()
    
    for i in range(P):  # lista de dicionários, com nome e quantidade dos produtos a ser comprados
        produto = input(f'Produto {i} - Nome e quantidade: ').split()
        info = {'nome': produto[0], 'quantidade': int(produto[1])}
        comprou.append(info.copy())
    
    valorCompra = 0  # determina o valor final da compra
    for c in comprou:  # percorre a lista de itens comprados
        for p in produtos: # percorre a lista de produtos disponíveis na feira
            if c['nome'] == p['nome']:  # encontra, pelo nome, o produto comprado
                valorCompra += c['quantidade'] * p['preco']  # multiplica a quantidade comprada pelo preço e
                                                             # acumula esse valor com os valores prévios
    
    print('R$:', valorCompra)
                