def elevador(s,e):
    soma = 0
    for i in range(n):
        s, e = [int(x) for x in input("Insira a quantidade de pessoas que sairam e que entraram: ").split()]
        soma = soma + (e - s)
        if soma > c:
            print("S")
            break
        if soma <= c:
            print("N")
 
s = 0
e = 0

n, c = [int(x) for x in input("Digite a quantidade de leituras e a capacidade máxima: ").split()]

elevador(s,e)
