import os

def recortar(lista):
    b=[]

    for i, palabraA in enumerate(lista):
        maxc = 0

        for j, otraP in enumerate(lista):
            if i == j:
                continue

            prefijo = os.path.commonprefix([palabraA,otraP])
            maxc = max(maxc, len(prefijo))

        b.append(palabraA[:maxc +1])
    return b
n = int(input())
a=[]


for i in range(n):
    x = input()
    if len(x)<=8:
        a.append(x)
    else:
        break

resultado = recortar(a)
resultadoord = sorted(resultado)

for i in resultadoord:
    print (i)