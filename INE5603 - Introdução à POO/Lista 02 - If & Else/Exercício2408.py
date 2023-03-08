pontA, pontB, pontC = [int(x) for x in input("Digite as pontuações: ").split()]

vice = 0
if (pontA > pontB and pontA < pontC) or (pontA > pontC and pontA < pontB):
    vice = pontA
elif (pontB > pontA and pontB < pontC) or (pontB > pontC and pontB < pontA):
    vice = pontB
else:
    vice = pontC

print(vice)
