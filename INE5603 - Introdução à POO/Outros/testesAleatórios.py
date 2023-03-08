def transitiveClosure (matrix):
    matrix = [1,1,1][1,1,1][1,1,0]
    result = ""
    length = 4
    for k in range(0, length):
        for row in range(0, length):
            for col in range(0, length):
                matrix[row] [col] = matrix[row][col] or (matrix[row][k] and matrix[k][col])
        result += ("\n W" + str(k) +" is: \n" + str(matrix).replace("]," , "] \n") + "\n")
    result += ("\n Transitive closure is \n" + str(matrix).replace("]," , "]\n"))
    print(result)
    return result