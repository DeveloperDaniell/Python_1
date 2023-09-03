def transponoi(matriisi: list):
    dim = len(matriisi) 
    for i in range(dim):
        for j in range(i+1,dim):
            tmp = matriisi[i][j]
            matriisi[i][j] = matriisi[j][i]
            matriisi[j][i] = tmp
    return



