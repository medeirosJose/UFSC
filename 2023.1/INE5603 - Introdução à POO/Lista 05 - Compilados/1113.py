while True:
    x, y = input("Digite dois valores - separados por um espaço: ").split()
    x = int(x)
    y = int(y)
    if x < y:
        print("Crescente")
    elif x > y:
        print("Decrescente")
    elif x == y:
        print("-")
        break