def diagonalDifference(arr):
    diagoP = 0
    diagoS = 0
    tamanho = len(arr)
    for indexl,linha in enumerate(arr):
        for indexc,coluna in enumerate(linha):
            if (indexl == indexc):
                diagoP += coluna
            if (indexc + indexl == tamanho-1):
                print("["+ str(indexl)+":"+str(indexc) +"]= "+ str(coluna))
                diagoS += coluna
    resultado = diagoP - diagoS
    if (resultado < 0):
        resultado *= -1
    print(str(diagoP) + " " + str(diagoS))
    return resultado

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalDifference(matriz))