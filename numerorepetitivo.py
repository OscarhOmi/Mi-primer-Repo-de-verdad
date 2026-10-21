x = int(input())
y = list(map(int, input().split()))

if len(y) == x:
    num = min(set(y), key = lambda n: (-y.count(n),n))
    print (num)