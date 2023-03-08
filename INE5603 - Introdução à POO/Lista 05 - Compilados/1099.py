n = int(input("Digite a quantidade de testes: "))
aux = 0
#soma = 0
somaAux = 0

for i in range(n):
    x, y = input("Digite os valores - separados por um espaço: ").split()
    x = int(x)
    y = int(y)
    
    if x > y:
        aux = x
        x = y
        y = aux
    soma = 0
    for i in range(x+1,y):
        if i % 2 != 0:
            soma += i
    print(soma)
            
