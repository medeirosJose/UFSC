nDias = int(input("Informe a quantidade de dias: "))
casa = trabalho = 0
CasaExtra = TrabalhoExtra = 0

for i in range(nDias):
    sd, sn = input("Informe a previsão: ").split()
    if sd == 'chuva' and CasaExtra == 0:
        casa += 1
        TrabalhoExtra += 1
    elif sd == 'chuva' and CasaExtra > 0:
        CasaExtra -= 1
        TrabalhoExtra += 1

    if sn == 'chuva' and TrabalhoExtra == 0:
        trabalho += 1
        CasaExtra += 1
    elif sn == 'chuva' and TrabalhoExtra > 0:
        TrabalhoExtra -= 1
        CasaExtra += 1

print("Rafael deverá comprar",casa,"guarda-chuvas para casa e",trabalho,"para o trabalho.")

