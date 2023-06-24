while True:
    soma = 0

    nAlgarismos, mNumero= input("Informe a quantidade de algarismos: ").split()
    nAlgarismos = int(nAlgarismos)

    for i in range(nAlgarismos):
        soma += int(mNumero[i])

    if soma % 3 == 0:
        print(soma,'- Sim')
    else:
        print(soma,'- Não')

    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == 'N':
        break



