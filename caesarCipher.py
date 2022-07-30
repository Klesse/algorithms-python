def caesarCipher(s, k):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
    'q','r','s','t','u','v','w','x','y','z']
    rotated = []
    for letra in alphabet:
        rotated.append(letra)
    for i in range(k):
        aux = rotated[-1]
        for j in range(-1,len(rotated)-1):
            rotated[j] = rotated[j+1]
        rotated[-2]=aux
    string = ""

    for letra in s:
        contador = 0
        for index,letra_aux in enumerate(alphabet):
            if (str(letra) == (str(letra_aux).upper())):
                string += str(rotated[index].upper())
            elif(str(letra) == (str(letra_aux).lower())):
                string += str(rotated[index].lower())
            else:
                contador+=1
        if (contador == len(alphabet)):
            string += letra
    return string

print(caesarCipher("policia",1))