def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

contPar = 0

for i in range(10):
    num = int(input("Digite o número: "))
    numPar = par(num)

    if numPar:
        contPar += 1

print("Há {} número(s) par(es) e {} número(s) ímpar(es)".format(contPar, 10 - contPar))