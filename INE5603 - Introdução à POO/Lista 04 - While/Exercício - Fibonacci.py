t1 = 0
t2 = 1

n = int(input("Digite um número inteiro: "))

if n == 0:
    print('-')

'''for i in range(n):

    print(t2)
    t3 = t2 + t1
    t1 = t2
    t2 = t3'''

i = 0
while i < n:
    print(t2)
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    i = i+1