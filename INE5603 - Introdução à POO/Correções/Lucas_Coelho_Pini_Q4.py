#Questão 4 - Prova

#Função que analisa a lista ‘‘lista_soma_saldos‘‘ e retorna o menor dos valores dela
def saldo_final(lista_soma_saldos):    
    #Variável acumuladora para o loop que vem a seguir
    menor = 0
    #Loop que percorre a lista ‘‘lista_soma_saldos‘‘ e indica o menor valor
    for i in range(len(lista_soma_saldos)):
        if (lista_soma_saldos[menor]) > (lista_soma_saldos[i]):
            menor = i
            
    #Comando que retorna o valor calculado na função para o código principal
    return(lista_soma_saldos[menor])
  
#Entrada de dados do código principal    
numero_dias, saldo = input('Informe o número de dias do periodo de interesse e o saldo da conta no início do período: ').split(' ')
#Definição dos tipos de dados de cada variável de entrada
numero_dias = int(numero_dias)
saldo = int(saldo)

#Loop que analisa para ver se os valores de entrada estão dentro dos limites
while (numero_dias > 30) or (numero_dias < 1) or (saldo > 1000) or (saldo < -1000):
    print('Valores além dos limites')
    numero_dias, saldo = input('Informe o número de dias do periodo de interesse e o saldo da conta no início do período: ').split(' ')
    numero_dias = int(numero_dias)
    saldo = int(saldo)

#Lista_mov_dia seria a lista que armazena os valores da movimentação de cada dia
lista_mov_dia = []
#Loop que, de acordo com o número de dias previamente informado, insere uma série de inputs para a entrada dos valores da movimentação de dias diferentes
for i in range(numero_dias):
    mov_dia = int(input('Informe a movimentação de um dia: '))
    lista_mov_dia.append(mov_dia)

#Variável acumuladora usada no loop que vem a seguir
soma_saldos = saldo
#Lista que armazena a soma de todos os valores da lista ‘‘lista_mov_dia‘‘
lista_soma_saldos = []
#loop que calcula a soma de todos os valores da lista ‘‘lista_mov_dia‘‘ e insere na lista ‘‘lista_soma_saldos‘‘
for i in range(numero_dias):
    soma_saldos = soma_saldos + lista_mov_dia[i]
    lista_soma_saldos.append(soma_saldos)

#Variável resultado recebe o valor retornado pelo comando ‘‘return‘‘ dentro da função
resultado = saldo_final(lista_soma_saldos)

#Condições que, dependendo do menor valor encontrado na lista ‘‘lista_soma_saldos‘‘, vai analisar se deverá acrescentar o juros ou não e, então, imprimirá o saldo final e o menor valor (aquele utilizado para verificar o quanto seria de juros)
#Condição se tiver juros de 10%
if resultado < -1000:
    valor_final = soma_saldos + (resultado*(10/100))
    print(valor_final, resultado)
#Condição se não tiver juros de 10%
else:
    print(soma_saldos, resultado)


