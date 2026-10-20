p, d= input().split()



x= 2*(int(p))+(100-int(d))

y= x/3

if y >= 70:
    print("FRENADO FUERTE ",int(y))

else:
    print("FRENADO MODERADO ",int(y))