def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
 
 
# Driver Code
if __name__ == "__main__":
    A = int(input('Valor A - '))
    M = int(input('Valor Módulo - ')) 
 
    # Function call
    print(modInverse(A, M))