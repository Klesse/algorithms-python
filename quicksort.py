def troca(v,i,j):
    v3 = [1]
    v3[0]=v[i]
    v[i]=v[j]
    v[j]=v3[0]


def separa1(v,p,r):
    i=p 
    j=r-1
    c=v[r]
    while (1):
        while(i<r and v[i]<=c): i+=1
        while(j>i and v[j] > c): j-=1
        if (i >= j): break
        troca(v,i,j)
    troca(v,i,r)
    return i

    


def quickSortR(v,p,r):
    i = 0
    if (p < r):
        i = separa1(v,p,r) #i sendo a posição do pivô após separação
        quickSortR(v,p,i-1)
        quickSortR(v,i+1,r)

vetor = [141,4040,4855,874410,74141,3454]
quickSortR(vetor,0,5)
print(vetor)