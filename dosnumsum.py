
n = int(input())
numeros = list(map(int, input().split()))
t = int(input())

vistos = set()
encontrado = False

for num in numeros:
    complemento = t - num

    if complemento in vistos:
        encontrado = True
        break

    vistos.add(num)

if encontrado:
    print("SI")
else:
    print("NO")
