def serie(tamanho):
    n = 0
    m = 0
    resultado = 0

    for i in range(tamanho):
        if i == 0:
            n = n + 1
            m = m + 1
        else:
            n = n + 1
            m = m + 2
        
        resultado += n / m
        print(n, m)
    print("{:.3f}".format(resultado))

tamanho = int(input("Insira o tamanho da série: "))
serie(tamanho)
