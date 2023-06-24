#Exercício2417

cv, ce, cs, fv, fe, fs = input("Digite as pontuações: ").split()

cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

cv = 3*cv
fv = 3*fv

cormengo = int(cv + ce + cs)
flaminthians = int(fv + fe + fs)

if cormengo > flaminthians:
    print("C")
elif cormengo < flaminthians:
    print("F")
else:
    print("=")
    
#corrigir a questão dos empates