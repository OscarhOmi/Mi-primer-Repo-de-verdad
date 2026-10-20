x= int(input())
a = input()
y = a.split()
if len(y) <= x:
    z = list(map(int,y))
    total = sum(z)
    print(total)