import time

def superDigit(n, k):
    if k!=0:
        n=n*k
    if(len(n)!=1):
        soma = 0
        for letra in n:
            soma += int(letra)
        return superDigit(str(soma),0)
    return n



print(superDigit('148',1))