'''
Aula 18 | Exercício do Slide

Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista.

No final mostre:
    A) quantas pessoas foram cadastradas;
    B) a média de idade do grupo;
    C) uma lista com todas as mulheres;
    D) uma lista com todas as pessoas com idade acima
    da média.
'''

def media_idade(lista): # função que calcula e retorna a média de idade  
    soma = 0  
    for i in range (len(lista)):     # percorre a lista
        soma += lista[i]['idade']    # soma a idade de cada membro da lista
        
    return round(soma/len(lista))    # calcula a média de idade e retorna o valor arredondado


def lista_mulheres(lista):  # função que seleciona apenas as mulheres da lista
    mulheres = []   
    for j in range(len(lista)):                  # percorre a lista de pessoas cadastradas
        if lista[j]['sexo'] == 'F':              # seleciona apenas os membros da lista registrado como sexo F
            mulheres.append(lista[j].copy())     # salva uma cópia dos dados da pessoa em uma outra lista   
    return mulheres        # retorna a lista que contém apenas as mulheres registradas

def idade_acima_media(lista):  # seleciona apenas os membros com idade acima da média  
    media = int(media_idade(lista))   # calcula a média de idade usando a def media_idade(lista)
                                      # converte o valor retornado para int
    acima_media = []
    
    for n in range(len(lista)):                  # percorre a lista de pessoas cadastradas
        if lista[n]['idade'] > media:            # verifica quem está com a idade acima da média
            acima_media.append(lista[n].copy())  # armazena uma cópia dos dados da pessoa em outra lista
    
    return acima_media    # retorna a lista com as pessoas de idade acima da média

#main
pessoa = {}
pessoas = []

while True:
    print('Sobre a pessoa, informe os dados a seguir:')
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa.copy())

    novamente = str(input('Cadastrar outra pessoa? [S/N] ')).upper()
    if novamente == 'N':
        break

#print(pessoas)

print('Total de pessoas cadastradas:', len(pessoas))

# funções próprias foram utilizadas para atingir os objetivos do exercício
print('Média de idade do grupo:', media_idade(pessoas))
print('Lista com todas as mulheres:', lista_mulheres(pessoas))
print('Lista de pessoas com idade acima da média:', idade_acima_media(pessoas))
