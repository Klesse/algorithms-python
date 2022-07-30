def superDigit1(n, k):
    if k==0:
        return 0
    soma = 0
    for letra in n:
        soma += int(letra)
    return soma + superDigit1(n,k-1)


def superDigit2(n, k):
    if k!=0:
        n=n*k
    if(len(n)!=1):
        soma = 0
        for letra in n:
            soma += int(letra)
        return superDigit2(str(soma),0)
    return n


print(superDigit2('9875',4))