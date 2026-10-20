mod = 10**9 + 7

n,k= input().split()

a=[]
b=[]

for x in range(int(n)) :
    l,p= input().split()

    a.append(int(l))
    b.append(int(p))

cantidad = [0] * (int(k) +1)

for i in range (int(n)):
    cantidad [b[i]] +=a[i]

respuesta = 1

for dificultad in range (1, int(k) +1):
    respuesta = (respuesta * cantidad[dificultad]) %mod

print(respuesta)