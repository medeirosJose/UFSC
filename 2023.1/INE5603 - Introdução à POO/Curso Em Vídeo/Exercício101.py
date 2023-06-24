def voto(ano):
    idade = 2022 - ano
    if idade < 16:
        return 'Voto negado'
    elif idade > 16 and idade < 18:
        return 'Voto opcional'
    elif idade > 18:
        return 'Voto obrigatório'


#main
nasc = int(input("Ano q vc nasceu: "))
print(voto(nasc))