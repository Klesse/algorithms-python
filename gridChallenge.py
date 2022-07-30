def gridChallenge(grid):
    correto = True
    aux = []
    grid2 = []
    for conjunto in grid:
        aux.append(list(conjunto))
        aux[0].sort()
        grid2.append("".join(aux[0]))
        aux=[]

    grid_colunas = []

    for i in range(len(grid2[0])):
        for j in range(len(grid2)):
            aux.append(grid2[j][i])  
        aux = "".join(aux)
        grid_colunas.append(aux)
        aux = []


    for linha in grid_colunas:
        aux=[]
        aux.append(list(linha))
        aux[0].sort()
        aux[0] = "".join(aux[0])
        print(linha)
        print(aux[0])
        if (linha == aux[0]):
            correto = True
        else:
            correto=False
            break
    if (correto):
        return "YES"
    else:
        return "NO"




gride = ['mpxz','abcd','wlmf']

print(gridChallenge(gride))
    