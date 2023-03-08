n1, n2, n3 = [int(x) for x in input("Digite trẽs valores inteiro, um ao lado do outro: ").split()]

if (n1 <= n2 and n2 <= n3):
    print("A ordem crescente é -> ",n1, n2, n3)
    
elif (n1 <= n3 and n3 <= n2):
    print("A ordem crescente é -> ",n1, n3, n2)
    
elif (n2 <= n1 and n1 <= n3):
    print("A ordem crescente é -> ",n2, n1, n3)
    
elif (n2 <= n3 and n3 <= n1):
    print("A ordem crescente é -> ",n2, n3, n1)
    
elif n3 <= n1 and n1 <= n2:
    print("A ordem crescente é -> ",n3, n1, n2)

else:
    print("A ordem crescente é -> ",n3, n2, n1)
    