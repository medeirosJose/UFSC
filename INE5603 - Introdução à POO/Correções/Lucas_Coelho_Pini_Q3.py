#Questão 3 - Prova 

#Função com vários loops que criam diversas listas e por fim imprime o resultado
def cálculo(tamanho):
    #Lista que armazena todos os valores calculados no loop que vem a seguir
    lista_n = []
    n = 0
    #Loop que armazena todos os valores de n em uma progressão aritmética de razão = 1 e a1 = 0 em uma lista
    for i in range(tamanho):
        n = n + 1
        lista_n.append(n)
        
    #Lista que armazena todos os valores calculados no loop que vem a seguir
    lista_m = []
    m = -1
    #Loop que armazena todos os valores de m em uma progressão aritmética de razão = 2 e a1 = -1 em uma lista
    for i in range(tamanho):
        m = m + 2
        lista_m.append(m)

    #Lista que armazena todos os valores calculados no loop que vem a seguir
    lista_termos = []
    #Loop que armazena todos os valores da divisão de n/m previamente calculados em uma lista
    for i in range(tamanho):
        s = (lista_n[i])/(lista_m[i])
        lista_termos.append(s)

    soma = 0
    #Loop que faz a soma de todos termos da lista que armazenou todas as divisões de n/m
    for i in range(len(lista_termos)):
        soma = soma + lista_termos[i]

    #Loop que imprime todos os valores de n e m
    for i in range(len(lista_termos)):
        print(lista_n[i], lista_m[i])

    #Impressão da soma
    print("Soma = {:.4f}".format(soma))


#Entrada do tamanho da soma
tamanho = int(input("Informe o número de parcelas da soma: "))

#Envia o ‘‘tamanho‘‘ para a função ‘‘cálculo‘‘
cálculo(tamanho)
    
    