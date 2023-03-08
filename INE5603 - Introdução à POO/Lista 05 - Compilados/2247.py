contTeste = 0
soma = 0

while True:
    testes = int(input("Insira a quantidade de testes: "))
    if testes == 0:
        print("Loop cancelado.")
        break
    contTeste += 1
    print("Teste ",contTeste)
    for i in range(testes):
        dinheiroX, dinheiroY = input("Digite o dinhero - separado por um espaço: ").split()
        dinheiroX = int(dinheiroX)
        dinheiroY = int(dinheiroY)
        soma += dinheiroX - dinheiroY
        print(soma)
    